# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeleteScheduledActionRequest(object):
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
        'auto_scaling_group_name': 'str',
        'scheduled_action_name': 'str'
    }

    attribute_map = {
        'auto_scaling_group_name': 'autoScalingGroupName',
        'scheduled_action_name': 'scheduledActionName'
    }

    def __init__(self, auto_scaling_group_name=None, scheduled_action_name=None):  # noqa: E501
        """DeleteScheduledActionRequest - a model defined in Swagger"""  # noqa: E501

        self._auto_scaling_group_name = None
        self._scheduled_action_name = None
        self.discriminator = None

        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        self.scheduled_action_name = scheduled_action_name

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this DeleteScheduledActionRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this DeleteScheduledActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this DeleteScheduledActionRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this DeleteScheduledActionRequest.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def scheduled_action_name(self):
        """Gets the scheduled_action_name of this DeleteScheduledActionRequest.  # noqa: E501

        스케쥴액션명  # noqa: E501

        :return: The scheduled_action_name of this DeleteScheduledActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_action_name

    @scheduled_action_name.setter
    def scheduled_action_name(self, scheduled_action_name):
        """Sets the scheduled_action_name of this DeleteScheduledActionRequest.

        스케쥴액션명  # noqa: E501

        :param scheduled_action_name: The scheduled_action_name of this DeleteScheduledActionRequest.  # noqa: E501
        :type: str
        """
        if scheduled_action_name is None:
            raise ValueError("Invalid value for `scheduled_action_name`, must not be `None`")  # noqa: E501

        self._scheduled_action_name = scheduled_action_name

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
        if not isinstance(other, DeleteScheduledActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
