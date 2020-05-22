# coding: utf-8

"""
    monitoring

    OpenAPI spec version: 2020-05-22T05:53:06Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Metric(object):
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
        'metric_name': 'str'
    }

    attribute_map = {
        'instance_no': 'instanceNo',
        'metric_name': 'metricName'
    }

    def __init__(self, instance_no=None, metric_name=None):  # noqa: E501
        """Metric - a model defined in Swagger"""  # noqa: E501

        self._instance_no = None
        self._metric_name = None
        self.discriminator = None

        if instance_no is not None:
            self.instance_no = instance_no
        if metric_name is not None:
            self.metric_name = metric_name

    @property
    def instance_no(self):
        """Gets the instance_no of this Metric.  # noqa: E501


        :return: The instance_no of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._instance_no

    @instance_no.setter
    def instance_no(self, instance_no):
        """Sets the instance_no of this Metric.


        :param instance_no: The instance_no of this Metric.  # noqa: E501
        :type: str
        """

        self._instance_no = instance_no

    @property
    def metric_name(self):
        """Gets the metric_name of this Metric.  # noqa: E501


        :return: The metric_name of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Metric.


        :param metric_name: The metric_name of this Metric.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
