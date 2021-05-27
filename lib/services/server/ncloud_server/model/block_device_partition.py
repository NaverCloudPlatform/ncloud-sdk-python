# coding: utf-8

"""
    server

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BlockDevicePartition(object):
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
        'mount_point': 'str',
        'partition_size': 'str'
    }

    attribute_map = {
        'mount_point': 'mountPoint',
        'partition_size': 'partitionSize'
    }

    def __init__(self, mount_point=None, partition_size=None):  # noqa: E501
        """BlockDevicePartition - a model defined in Swagger"""  # noqa: E501

        self._mount_point = None
        self._partition_size = None
        self.discriminator = None

        if mount_point is not None:
            self.mount_point = mount_point
        if partition_size is not None:
            self.partition_size = partition_size

    @property
    def mount_point(self):
        """Gets the mount_point of this BlockDevicePartition.  # noqa: E501

        마운트포인트  # noqa: E501

        :return: The mount_point of this BlockDevicePartition.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this BlockDevicePartition.

        마운트포인트  # noqa: E501

        :param mount_point: The mount_point of this BlockDevicePartition.  # noqa: E501
        :type: str
        """

        self._mount_point = mount_point

    @property
    def partition_size(self):
        """Gets the partition_size of this BlockDevicePartition.  # noqa: E501

        파티션사이즈  # noqa: E501

        :return: The partition_size of this BlockDevicePartition.  # noqa: E501
        :rtype: str
        """
        return self._partition_size

    @partition_size.setter
    def partition_size(self, partition_size):
        """Sets the partition_size of this BlockDevicePartition.

        파티션사이즈  # noqa: E501

        :param partition_size: The partition_size of this BlockDevicePartition.  # noqa: E501
        :type: str
        """

        self._partition_size = partition_size

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
        if not isinstance(other, BlockDevicePartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
