# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2018-11-13T06:28:28Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataPoint(object):
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
        'timestamp': 'str',
        'average': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'average': 'average',
        'unit': 'unit'
    }

    def __init__(self, timestamp=None, average=None, unit=None):  # noqa: E501
        """DataPoint - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._average = None
        self._unit = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if average is not None:
            self.average = average
        if unit is not None:
            self.unit = unit

    @property
    def timestamp(self):
        """Gets the timestamp of this DataPoint.  # noqa: E501


        :return: The timestamp of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DataPoint.


        :param timestamp: The timestamp of this DataPoint.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def average(self):
        """Gets the average of this DataPoint.  # noqa: E501


        :return: The average of this DataPoint.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this DataPoint.


        :param average: The average of this DataPoint.  # noqa: E501
        :type: float
        """

        self._average = average

    @property
    def unit(self):
        """Gets the unit of this DataPoint.  # noqa: E501


        :return: The unit of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DataPoint.


        :param unit: The unit of this DataPoint.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, DataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
