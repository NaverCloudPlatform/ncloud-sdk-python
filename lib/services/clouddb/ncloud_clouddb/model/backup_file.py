# coding: utf-8

"""
    clouddb

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_clouddb.model.common_code import CommonCode  # noqa: F401,E501


class BackupFile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'host_name': 'str',
        'file_name': 'str',
        'database_name': 'str',
        'first_lsn': 'str',
        'last_lsn': 'str',
        'backup_type': 'CommonCode',
        'backup_start_time': 'str',
        'backup_end_time': 'str'
    }

    attribute_map = {
        'host_name': 'hostName',
        'file_name': 'fileName',
        'database_name': 'databaseName',
        'first_lsn': 'firstLsn',
        'last_lsn': 'LastLsn',
        'backup_type': 'backupType',
        'backup_start_time': 'backupStartTime',
        'backup_end_time': 'backupEndTime'
    }

    def __init__(self, host_name=None, file_name=None, database_name=None, first_lsn=None, last_lsn=None, backup_type=None, backup_start_time=None, backup_end_time=None):  # noqa: E501
        """BackupFile - a model defined in Swagger"""  # noqa: E501

        self._host_name = None
        self._file_name = None
        self._database_name = None
        self._first_lsn = None
        self._last_lsn = None
        self._backup_type = None
        self._backup_start_time = None
        self._backup_end_time = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if file_name is not None:
            self.file_name = file_name
        if database_name is not None:
            self.database_name = database_name
        if first_lsn is not None:
            self.first_lsn = first_lsn
        if last_lsn is not None:
            self.last_lsn = last_lsn
        if backup_type is not None:
            self.backup_type = backup_type
        if backup_start_time is not None:
            self.backup_start_time = backup_start_time
        if backup_end_time is not None:
            self.backup_end_time = backup_end_time

    @property
    def host_name(self):
        """Gets the host_name of this BackupFile.  # noqa: E501

        호스트이름  # noqa: E501

        :return: The host_name of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this BackupFile.

        호스트이름  # noqa: E501

        :param host_name: The host_name of this BackupFile.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def file_name(self):
        """Gets the file_name of this BackupFile.  # noqa: E501

        파일이름  # noqa: E501

        :return: The file_name of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this BackupFile.

        파일이름  # noqa: E501

        :param file_name: The file_name of this BackupFile.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def database_name(self):
        """Gets the database_name of this BackupFile.  # noqa: E501

        데이터베이스이름  # noqa: E501

        :return: The database_name of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this BackupFile.

        데이터베이스이름  # noqa: E501

        :param database_name: The database_name of this BackupFile.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

    @property
    def first_lsn(self):
        """Gets the first_lsn of this BackupFile.  # noqa: E501

        시작LSN  # noqa: E501

        :return: The first_lsn of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._first_lsn

    @first_lsn.setter
    def first_lsn(self, first_lsn):
        """Sets the first_lsn of this BackupFile.

        시작LSN  # noqa: E501

        :param first_lsn: The first_lsn of this BackupFile.  # noqa: E501
        :type: str
        """

        self._first_lsn = first_lsn

    @property
    def last_lsn(self):
        """Gets the last_lsn of this BackupFile.  # noqa: E501

        마지막LSN  # noqa: E501

        :return: The last_lsn of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._last_lsn

    @last_lsn.setter
    def last_lsn(self, last_lsn):
        """Sets the last_lsn of this BackupFile.

        마지막LSN  # noqa: E501

        :param last_lsn: The last_lsn of this BackupFile.  # noqa: E501
        :type: str
        """

        self._last_lsn = last_lsn

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupFile.  # noqa: E501

        백업유형  # noqa: E501

        :return: The backup_type of this BackupFile.  # noqa: E501
        :rtype: CommonCode
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupFile.

        백업유형  # noqa: E501

        :param backup_type: The backup_type of this BackupFile.  # noqa: E501
        :type: CommonCode
        """

        self._backup_type = backup_type

    @property
    def backup_start_time(self):
        """Gets the backup_start_time of this BackupFile.  # noqa: E501

        백업시작시간  # noqa: E501

        :return: The backup_start_time of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._backup_start_time

    @backup_start_time.setter
    def backup_start_time(self, backup_start_time):
        """Sets the backup_start_time of this BackupFile.

        백업시작시간  # noqa: E501

        :param backup_start_time: The backup_start_time of this BackupFile.  # noqa: E501
        :type: str
        """

        self._backup_start_time = backup_start_time

    @property
    def backup_end_time(self):
        """Gets the backup_end_time of this BackupFile.  # noqa: E501

        백업종료시간  # noqa: E501

        :return: The backup_end_time of this BackupFile.  # noqa: E501
        :rtype: str
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        """Sets the backup_end_time of this BackupFile.

        백업종료시간  # noqa: E501

        :param backup_end_time: The backup_end_time of this BackupFile.  # noqa: E501
        :type: str
        """

        self._backup_end_time = backup_end_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackupFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
