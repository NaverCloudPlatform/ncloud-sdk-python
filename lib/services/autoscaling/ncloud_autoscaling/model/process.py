# coding: utf-8

"""
    autoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_autoscaling.model.common_code import CommonCode  # noqa: F401,E501


class Process(object):
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
        'process': 'CommonCode'
    }

    attribute_map = {
        'process': 'process'
    }

    def __init__(self, process=None):  # noqa: E501
        """Process - a model defined in Swagger"""  # noqa: E501

        self._process = None
        self.discriminator = None

        if process is not None:
            self.process = process

    @property
    def process(self):
        """Gets the process of this Process.  # noqa: E501


        :return: The process of this Process.  # noqa: E501
        :rtype: CommonCode
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this Process.


        :param process: The process of this Process.  # noqa: E501
        :type: CommonCode
        """

        self._process = process

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
        if not isinstance(other, Process):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
