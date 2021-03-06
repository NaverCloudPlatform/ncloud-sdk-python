# coding: utf-8

"""
    server

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ChangeBlockStorageVolumeSizeRequest(object):
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
        'block_storage_instance_no': 'str',
        'block_storage_size': 'int'
    }

    attribute_map = {
        'block_storage_instance_no': 'blockStorageInstanceNo',
        'block_storage_size': 'blockStorageSize'
    }

    def __init__(self, block_storage_instance_no=None, block_storage_size=None):  # noqa: E501
        """ChangeBlockStorageVolumeSizeRequest - a model defined in Swagger"""  # noqa: E501

        self._block_storage_instance_no = None
        self._block_storage_size = None
        self.discriminator = None

        self.block_storage_instance_no = block_storage_instance_no
        self.block_storage_size = block_storage_size

    @property
    def block_storage_instance_no(self):
        """Gets the block_storage_instance_no of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501

        블록스토리지인스턴스번호  # noqa: E501

        :return: The block_storage_instance_no of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_instance_no

    @block_storage_instance_no.setter
    def block_storage_instance_no(self, block_storage_instance_no):
        """Sets the block_storage_instance_no of this ChangeBlockStorageVolumeSizeRequest.

        블록스토리지인스턴스번호  # noqa: E501

        :param block_storage_instance_no: The block_storage_instance_no of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501
        :type: str
        """
        if block_storage_instance_no is None:
            raise ValueError("Invalid value for `block_storage_instance_no`, must not be `None`")  # noqa: E501

        self._block_storage_instance_no = block_storage_instance_no

    @property
    def block_storage_size(self):
        """Gets the block_storage_size of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501

        블록스토리지사이즈  # noqa: E501

        :return: The block_storage_size of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501
        :rtype: int
        """
        return self._block_storage_size

    @block_storage_size.setter
    def block_storage_size(self, block_storage_size):
        """Sets the block_storage_size of this ChangeBlockStorageVolumeSizeRequest.

        블록스토리지사이즈  # noqa: E501

        :param block_storage_size: The block_storage_size of this ChangeBlockStorageVolumeSizeRequest.  # noqa: E501
        :type: int
        """
        if block_storage_size is None:
            raise ValueError("Invalid value for `block_storage_size`, must not be `None`")  # noqa: E501

        self._block_storage_size = block_storage_size

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
        if not isinstance(other, ChangeBlockStorageVolumeSizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
