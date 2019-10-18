# coding: utf-8

"""
    clouddb

    OpenAPI spec version: 2018-11-13T06:30:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CloudDBConfig(object):
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
        'config_name': 'str',
        'config_value': 'str'
    }

    attribute_map = {
        'config_name': 'configName',
        'config_value': 'configValue'
    }

    def __init__(self, config_name=None, config_value=None):  # noqa: E501
        """CloudDBConfig - a model defined in Swagger"""  # noqa: E501

        self._config_name = None
        self._config_value = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value

    @property
    def config_name(self):
        """Gets the config_name of this CloudDBConfig.  # noqa: E501

        설정명  # noqa: E501

        :return: The config_name of this CloudDBConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this CloudDBConfig.

        설정명  # noqa: E501

        :param config_name: The config_name of this CloudDBConfig.  # noqa: E501
        :type: str
        """

        self._config_name = config_name

    @property
    def config_value(self):
        """Gets the config_value of this CloudDBConfig.  # noqa: E501

        설정값  # noqa: E501

        :return: The config_value of this CloudDBConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this CloudDBConfig.

        설정값  # noqa: E501

        :param config_value: The config_value of this CloudDBConfig.  # noqa: E501
        :type: str
        """

        self._config_value = config_value

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
        if not isinstance(other, CloudDBConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
