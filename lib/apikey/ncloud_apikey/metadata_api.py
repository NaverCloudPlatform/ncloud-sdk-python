# coding: utf-8

import os
import json

try:
    import urllib3
except ImportError:
    raise ImportError('ncloud-sdk requires urllib3.')


def ensure_boolean(val):
    if isinstance(val, bool):
        return val
    else:
        return val.lower() == 'true'


class MetadataApiClient(object):
    DEFAULT_METADATA_SERVICE_TIMEOUT = 3
    METADATA_BASE_URL = 'http://169.254.169.254'
    _CREDENTIALS_URL_PATH = '/latest/meta-data/iam/security-credentials/'

    def __init__(self, timeout=DEFAULT_METADATA_SERVICE_TIMEOUT,
                 num_attempts=1, base_url=METADATA_BASE_URL,
                 env=None):
        self._timeout = timeout
        self._num_attempts = num_attempts
        if env is None:
            env = os.environ.copy()
        custom_endpoint = env.get('NCLOUD_METADATA_ENDPOINT', '')
        if custom_endpoint != '':
            base_url = custom_endpoint
        self._base_url = base_url
        self._retry_count = 2
        self._connect()

    def _connect(self):
        headers = {
            'User-Agent': 'ncloud-sdk',
        }
        timeout = urllib3.Timeout(connect=self._timeout, read=self._timeout)
        client_options = {
            "num_pools": 1,
            "maxsize": 1,
            "block": True,
            "headers": headers,
            "timeout": timeout,
            "retries": self._retry_count,
        }

        self._client = urllib3.PoolManager(**client_options)

    def _get_metadata_credentials_url(self):
        return self._base_url + MetadataApiClient._CREDENTIALS_URL_PATH

    def fetch_iam_role(self):
        role_url = self._get_metadata_credentials_url()
        resp = self._client.request('GET', role_url)
        if resp.status == 200:
            return resp.data.decode('utf-8')
        elif resp.status in (404, 403, 405):
            return None
        elif resp.status_code in (400,):
            raise Exception('Unable to load iam role.')

    def fetch_iam_role_credentials(self, role_id):
        role_credentials_url = self._get_metadata_credentials_url() + role_id
        resp = self._client.request('GET', role_credentials_url)
        if resp.status == 200:
            return json.loads(resp.data.decode('utf-8'))
        elif resp.status in (404, 403, 405):
            return None
        elif resp.status_code in (400,):
            raise Exception('Unable to load role credentials.')
