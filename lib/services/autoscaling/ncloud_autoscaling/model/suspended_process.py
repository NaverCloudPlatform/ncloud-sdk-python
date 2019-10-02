# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-11-13T06:27:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_autoscaling.model.common_code import CommonCode  # noqa: F401,E501


class SuspendedProcess(object):
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
        'process': 'CommonCode',
        'suspension_reason': 'str'
    }

    attribute_map = {
        'process': 'process',
        'suspension_reason': 'suspensionReason'
    }

    def __init__(self, process=None, suspension_reason=None):  # noqa: E501
        """SuspendedProcess - a model defined in Swagger"""  # noqa: E501

        self._process = None
        self._suspension_reason = None
        self.discriminator = None

        if process is not None:
            self.process = process
        if suspension_reason is not None:
            self.suspension_reason = suspension_reason

    @property
    def process(self):
        """Gets the process of this SuspendedProcess.  # noqa: E501

        프로세스  # noqa: E501

        :return: The process of this SuspendedProcess.  # noqa: E501
        :rtype: CommonCode
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this SuspendedProcess.

        프로세스  # noqa: E501

        :param process: The process of this SuspendedProcess.  # noqa: E501
        :type: CommonCode
        """

        self._process = process

    @property
    def suspension_reason(self):
        """Gets the suspension_reason of this SuspendedProcess.  # noqa: E501

        프로세스보류원인  # noqa: E501

        :return: The suspension_reason of this SuspendedProcess.  # noqa: E501
        :rtype: str
        """
        return self._suspension_reason

    @suspension_reason.setter
    def suspension_reason(self, suspension_reason):
        """Sets the suspension_reason of this SuspendedProcess.

        프로세스보류원인  # noqa: E501

        :param suspension_reason: The suspension_reason of this SuspendedProcess.  # noqa: E501
        :type: str
        """

        self._suspension_reason = suspension_reason

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
        if not isinstance(other, SuspendedProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
