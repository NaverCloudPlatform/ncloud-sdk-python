# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeleteLoginKeysRequest(object):
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
        'key_name_list': 'list[str]'
    }

    attribute_map = {
        'key_name_list': 'keyNameList'
    }

    def __init__(self, key_name_list=None):  # noqa: E501
        """DeleteLoginKeysRequest - a model defined in Swagger"""  # noqa: E501

        self._key_name_list = None
        self.discriminator = None

        self.key_name_list = key_name_list

    @property
    def key_name_list(self):
        """Gets the key_name_list of this DeleteLoginKeysRequest.  # noqa: E501

        키이름리스트  # noqa: E501

        :return: The key_name_list of this DeleteLoginKeysRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_name_list

    @key_name_list.setter
    def key_name_list(self, key_name_list):
        """Sets the key_name_list of this DeleteLoginKeysRequest.

        키이름리스트  # noqa: E501

        :param key_name_list: The key_name_list of this DeleteLoginKeysRequest.  # noqa: E501
        :type: list[str]
        """
        if key_name_list is None:
            raise ValueError("Invalid value for `key_name_list`, must not be `None`")  # noqa: E501

        self._key_name_list = key_name_list

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
        if not isinstance(other, DeleteLoginKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
