# coding: utf-8

import os
import datetime
import threading
from dateutil.parser import parse
from dateutil.tz import tzlocal
from collections import namedtuple
from metadata_api import MetadataApiClient


def _serialize_if_needed(value, iso=False):
    if isinstance(value, datetime.datetime):
        if iso:
            return value.isoformat()
        return value.strftime('%Y-%m-%dT%H:%M:%S%Z')
    return value


def _local_now():
    return datetime.datetime.now(tzlocal())


class Credentials(object):
    def __init__(self, access_key, secret_key, expiration=None):
        self.access_key = access_key
        self.secret_key = secret_key
        self.expiration = expiration


class CredentialProvider(object):
    def load(self):
        return True


class EnvProvider(CredentialProvider):
    PROVIDER_NAME = 'EnvProvider'
    ACCESS_KEY = 'NCLOUD_ACCESS_KEY_ID'
    SECRET_KEY = 'NCLOUD_SECRET_ACCESS_KEY'

    def __init__(self, environ=None, mapping=None):
        if environ is None:
            environ = os.environ
        self.environ = environ
        self._mapping = self._build_mapping(mapping)

    def _build_mapping(self, mapping):
        # Mapping of variable name to env var name.
        var_mapping = {}
        if mapping is None:
            # Use the class var default.
            var_mapping['access_key'] = self.ACCESS_KEY
            var_mapping['secret_key'] = self.SECRET_KEY
        else:
            var_mapping['access_key'] = mapping.get('access_key', self.ACCESS_KEY)
            var_mapping['secret_key'] = mapping.get('secret_key', self.SECRET_KEY)
        return var_mapping

    def load(self):
        access_key = self.environ.get(self._mapping['access_key'], '')

        if access_key:
            # logger.info('Found credentials in environment variables.')
            fetcher = self._create_credentials_fetcher()
            credentials = fetcher()

            return Credentials(credentials['access_key'], credentials['secret_key'])
        else:
            return None

    def _create_credentials_fetcher(self):
        mapping = self._mapping
        environ = self.environ

        def fetch_credentials():
            credentials = {}
            access_key = environ.get(mapping['access_key'], '')
            if not access_key:
                raise Exception('Variable ' + mapping['access_key'] + ' not set')
            credentials['access_key'] = access_key
            secret_key = environ.get(mapping['secret_key'], '')
            if not secret_key:
                raise Exception('Variable ' + mapping['secret_key'] + ' not set')
            credentials['secret_key'] = secret_key
            return credentials

        return fetch_credentials


class ConfigFileProvider(CredentialProvider):
    PROVIDER_NAME = 'ConfigFileProvider'

    def __init__(self):
        self._config_filepath = self._get_configure_filepath()

    @staticmethod
    def _get_configure_filepath():
        return os.path.join(
            os.path.expanduser('~'),
            '.ncloud',
            'configure')

    def parse(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()

            prop_list = []
            for line in lines:
                if line == '' or len(line) < 3 or line[0] == "#":
                    continue

                split_str = line.strip().split('=')

                if len(split_str) < 2:
                    continue

                prop_list.append((split_str[0].strip(), split_str[1].strip()))

        return prop_list

    def load(self):
        if not os.path.exists(self._config_filepath):
            return None

        prop_list = self.parse(self._config_filepath)
        prop_dict = {}
        for k, v in prop_list:
            prop_dict[k] = v
        access_key = prop_dict['ncloud_access_key_id']
        secret_key = prop_dict['ncloud_secret_access_key']
        if access_key:
            return Credentials(access_key, secret_key)
        else:
            return None


class ServerRoleProvider(CredentialProvider):
    PROVIDER_NAME = 'ServerRoleProvider'

    def __init__(self):
        self._metadata_api_client = MetadataApiClient()

    def retrieve_iam_role_credentials(self):
        role_id = self._metadata_api_client.fetch_iam_role()
        if role_id:
            creds = self._metadata_api_client.fetch_iam_role_credentials(role_id)
            expiration = _serialize_if_needed(creds['Expiration'], iso=True)
            return Credentials(creds['AccessKeyId'], creds['SecretAccessKey'], expiration)

    def load(self):
        metadata_creds = self.retrieve_iam_role_credentials()
        if metadata_creds:
            return RefreshableCredentials.create_from_metadata(metadata_creds,
                                                               refresh_using=self.retrieve_iam_role_credentials)
        return None


def total_seconds(delta):
    return delta.total_seconds()


ReadOnlyCredentials = namedtuple('ReadOnlyCredentials',
                                 ['access_key', 'secret_key'])


class RefreshableCredentials(Credentials):
    """
    [_advisory_refresh_timeout] - [_mandatory_refresh_timeout] - [expire time]
    [before 15 min]             - [ before 5 min]              - [expire]
    """

    _advisory_refresh_timeout = 15 * 60

    _mandatory_refresh_timeout = 5 * 60

    def __init__(self, access_key, secret_key, expiration, refresh_using, time_fetcher=_local_now):
        self._refresh_using = refresh_using
        self._access_key = access_key
        self._secret_key = secret_key
        self._expiration = expiration
        self._time_fetcher = time_fetcher
        self._refresh_lock = threading.Lock()
        self._frozen_credentials = ReadOnlyCredentials(access_key, secret_key)

    @classmethod
    def create_from_metadata(cls, metadata, refresh_using):
        instance = cls(
            access_key=metadata.access_key,
            secret_key=metadata.secret_key,
            expiration=cls._expiry_datetime(metadata.expiration),
            refresh_using=refresh_using
        )
        return instance

    @property
    def access_key(self):
        self._refresh()
        return self._access_key

    @access_key.setter
    def access_key(self, value):
        self._access_key = value

    @property
    def secret_key(self):
        self._refresh()
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value

    def _seconds_remaining(self):
        delta = self._expiration - self._time_fetcher()
        return total_seconds(delta)

    def refresh_needed(self, refresh_in=None):
        """Check if a refresh is needed.
        """
        if self._expiration is None:
            return False
        if refresh_in is None:
            refresh_in = self._advisory_refresh_timeout
        if self._seconds_remaining() >= refresh_in:
            return False
        return True

    def _is_expired(self):
        return self.refresh_needed(refresh_in=0)

    def _refresh(self):
        if not self.refresh_needed(self._advisory_refresh_timeout):
            return

        if self._refresh_lock.acquire(False):
            try:
                if not self.refresh_needed(self._advisory_refresh_timeout):
                    return
                is_mandatory_refresh = self.refresh_needed(self._mandatory_refresh_timeout)
                self._protected_refresh(is_mandatory=is_mandatory_refresh)
                return
            finally:
                self._refresh_lock.release()
        elif self.refresh_needed(self._mandatory_refresh_timeout):
            with self._refresh_lock:
                if not self.refresh_needed(self._mandatory_refresh_timeout):
                    return
                self._protected_refresh(is_mandatory=True)

    def _protected_refresh(self, is_mandatory):
        try:
            metadata = self._refresh_using()
        except Exception as e:
            if is_mandatory:
                raise
            return
        self._set_from_data(metadata)
        self._frozen_credentials = ReadOnlyCredentials(self._access_key, self._secret_key)
        # if self._is_expired():
        #     raise RuntimeError("Credentials were refreshed, but the refreshed credentials are still expired.")

    @staticmethod
    def _expiry_datetime(time_str):
        return parse(time_str)

    def _set_from_data(self, creds):
        self.access_key = creds.access_key
        self.secret_key = creds.secret_key
        self.expiration = parse(creds.expiration)

    def get_frozen_credentials(self):
        self._refresh()
        return self._frozen_credentials


default_providers = [
    EnvProvider(),
    ConfigFileProvider(),
    ServerRoleProvider(),
]


class CredentialsResolver(object):

    def __init__(self, providers=None):
        if providers is None:
            providers = default_providers
        self.providers = providers

    def load_credentials(self):
        for provider in self.providers:
            credentials = provider.load()
            if credentials is not None:
                return credentials
        return None
