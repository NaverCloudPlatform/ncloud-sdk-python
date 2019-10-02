# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2018-11-13T06:28:28Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_monitoring.model.data_point import DataPoint  # noqa: F401,E501


class DataPoints(object):
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
        'label': 'str',
        'average': 'float',
        'maximum': 'float',
        'minimum': 'float',
        'sum': 'float',
        'data_point_list': 'list[DataPoint]'
    }

    attribute_map = {
        'label': 'label',
        'average': 'average',
        'maximum': 'maximum',
        'minimum': 'minimum',
        'sum': 'sum',
        'data_point_list': 'dataPointList'
    }

    def __init__(self, label=None, average=None, maximum=None, minimum=None, sum=None, data_point_list=None):  # noqa: E501
        """DataPoints - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._average = None
        self._maximum = None
        self._minimum = None
        self._sum = None
        self._data_point_list = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if average is not None:
            self.average = average
        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum
        if sum is not None:
            self.sum = sum
        if data_point_list is not None:
            self.data_point_list = data_point_list

    @property
    def label(self):
        """Gets the label of this DataPoints.  # noqa: E501


        :return: The label of this DataPoints.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DataPoints.


        :param label: The label of this DataPoints.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def average(self):
        """Gets the average of this DataPoints.  # noqa: E501


        :return: The average of this DataPoints.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this DataPoints.


        :param average: The average of this DataPoints.  # noqa: E501
        :type: float
        """

        self._average = average

    @property
    def maximum(self):
        """Gets the maximum of this DataPoints.  # noqa: E501


        :return: The maximum of this DataPoints.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this DataPoints.


        :param maximum: The maximum of this DataPoints.  # noqa: E501
        :type: float
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this DataPoints.  # noqa: E501


        :return: The minimum of this DataPoints.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this DataPoints.


        :param minimum: The minimum of this DataPoints.  # noqa: E501
        :type: float
        """

        self._minimum = minimum

    @property
    def sum(self):
        """Gets the sum of this DataPoints.  # noqa: E501


        :return: The sum of this DataPoints.  # noqa: E501
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this DataPoints.


        :param sum: The sum of this DataPoints.  # noqa: E501
        :type: float
        """

        self._sum = sum

    @property
    def data_point_list(self):
        """Gets the data_point_list of this DataPoints.  # noqa: E501


        :return: The data_point_list of this DataPoints.  # noqa: E501
        :rtype: list[DataPoint]
        """
        return self._data_point_list

    @data_point_list.setter
    def data_point_list(self, data_point_list):
        """Sets the data_point_list of this DataPoints.


        :param data_point_list: The data_point_list of this DataPoints.  # noqa: E501
        :type: list[DataPoint]
        """

        self._data_point_list = data_point_list

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
        if not isinstance(other, DataPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
