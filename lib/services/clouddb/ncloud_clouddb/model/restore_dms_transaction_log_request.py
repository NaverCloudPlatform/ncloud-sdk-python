# coding: utf-8

"""
    clouddb

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RestoreDmsTransactionLogRequest(object):
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
        'cloud_db_instance_no': 'str',
        'file_name': 'str',
        'is_recovery': 'bool',
        'new_database_name': 'str',
        'stop_time': 'str'
    }

    attribute_map = {
        'cloud_db_instance_no': 'cloudDBInstanceNo',
        'file_name': 'fileName',
        'is_recovery': 'isRecovery',
        'new_database_name': 'newDatabaseName',
        'stop_time': 'stopTime'
    }

    def __init__(self, cloud_db_instance_no=None, file_name=None, is_recovery=None, new_database_name=None, stop_time=None):  # noqa: E501
        """RestoreDmsTransactionLogRequest - a model defined in Swagger"""  # noqa: E501

        self._cloud_db_instance_no = None
        self._file_name = None
        self._is_recovery = None
        self._new_database_name = None
        self._stop_time = None
        self.discriminator = None

        self.cloud_db_instance_no = cloud_db_instance_no
        self.file_name = file_name
        self.is_recovery = is_recovery
        self.new_database_name = new_database_name
        if stop_time is not None:
            self.stop_time = stop_time

    @property
    def cloud_db_instance_no(self):
        """Gets the cloud_db_instance_no of this RestoreDmsTransactionLogRequest.  # noqa: E501

        클라우드DB인스턴스번호  # noqa: E501

        :return: The cloud_db_instance_no of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_db_instance_no

    @cloud_db_instance_no.setter
    def cloud_db_instance_no(self, cloud_db_instance_no):
        """Sets the cloud_db_instance_no of this RestoreDmsTransactionLogRequest.

        클라우드DB인스턴스번호  # noqa: E501

        :param cloud_db_instance_no: The cloud_db_instance_no of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :type: str
        """
        if cloud_db_instance_no is None:
            raise ValueError("Invalid value for `cloud_db_instance_no`, must not be `None`")  # noqa: E501

        self._cloud_db_instance_no = cloud_db_instance_no

    @property
    def file_name(self):
        """Gets the file_name of this RestoreDmsTransactionLogRequest.  # noqa: E501

        파일이름  # noqa: E501

        :return: The file_name of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this RestoreDmsTransactionLogRequest.

        파일이름  # noqa: E501

        :param file_name: The file_name of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def is_recovery(self):
        """Gets the is_recovery of this RestoreDmsTransactionLogRequest.  # noqa: E501

        복구용여부  # noqa: E501

        :return: The is_recovery of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_recovery

    @is_recovery.setter
    def is_recovery(self, is_recovery):
        """Sets the is_recovery of this RestoreDmsTransactionLogRequest.

        복구용여부  # noqa: E501

        :param is_recovery: The is_recovery of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :type: bool
        """
        if is_recovery is None:
            raise ValueError("Invalid value for `is_recovery`, must not be `None`")  # noqa: E501

        self._is_recovery = is_recovery

    @property
    def new_database_name(self):
        """Gets the new_database_name of this RestoreDmsTransactionLogRequest.  # noqa: E501

        새로운데이터베이스이름  # noqa: E501

        :return: The new_database_name of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_database_name

    @new_database_name.setter
    def new_database_name(self, new_database_name):
        """Sets the new_database_name of this RestoreDmsTransactionLogRequest.

        새로운데이터베이스이름  # noqa: E501

        :param new_database_name: The new_database_name of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :type: str
        """
        if new_database_name is None:
            raise ValueError("Invalid value for `new_database_name`, must not be `None`")  # noqa: E501

        self._new_database_name = new_database_name

    @property
    def stop_time(self):
        """Gets the stop_time of this RestoreDmsTransactionLogRequest.  # noqa: E501

        중지시간  # noqa: E501

        :return: The stop_time of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this RestoreDmsTransactionLogRequest.

        중지시간  # noqa: E501

        :param stop_time: The stop_time of this RestoreDmsTransactionLogRequest.  # noqa: E501
        :type: str
        """

        self._stop_time = stop_time

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
        if not isinstance(other, RestoreDmsTransactionLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other