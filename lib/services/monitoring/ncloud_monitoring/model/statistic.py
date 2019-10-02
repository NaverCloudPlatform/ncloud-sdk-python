# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2018-11-13T06:28:28Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_monitoring.model.data_points import DataPoints  # noqa: F401,E501


class Statistic(object):
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
        'instance_no': 'str',
        'data_points_list': 'list[DataPoints]'
    }

    attribute_map = {
        'instance_no': 'instanceNo',
        'data_points_list': 'dataPointsList'
    }

    def __init__(self, instance_no=None, data_points_list=None):  # noqa: E501
        """Statistic - a model defined in Swagger"""  # noqa: E501

        self._instance_no = None
        self._data_points_list = None
        self.discriminator = None

        if instance_no is not None:
            self.instance_no = instance_no
        if data_points_list is not None:
            self.data_points_list = data_points_list

    @property
    def instance_no(self):
        """Gets the instance_no of this Statistic.  # noqa: E501


        :return: The instance_no of this Statistic.  # noqa: E501
        :rtype: str
        """
        return self._instance_no

    @instance_no.setter
    def instance_no(self, instance_no):
        """Sets the instance_no of this Statistic.


        :param instance_no: The instance_no of this Statistic.  # noqa: E501
        :type: str
        """

        self._instance_no = instance_no

    @property
    def data_points_list(self):
        """Gets the data_points_list of this Statistic.  # noqa: E501


        :return: The data_points_list of this Statistic.  # noqa: E501
        :rtype: list[DataPoints]
        """
        return self._data_points_list

    @data_points_list.setter
    def data_points_list(self, data_points_list):
        """Sets the data_points_list of this Statistic.


        :param data_points_list: The data_points_list of this Statistic.  # noqa: E501
        :type: list[DataPoints]
        """

        self._data_points_list = data_points_list

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
        if not isinstance(other, Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
