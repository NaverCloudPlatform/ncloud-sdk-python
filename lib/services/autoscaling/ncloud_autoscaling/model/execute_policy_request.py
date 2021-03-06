# coding: utf-8

"""
    autoscaling

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExecutePolicyRequest(object):
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
        'honor_cooldown': 'bool',
        'policy_name': 'str'
    }

    attribute_map = {
        'auto_scaling_group_name': 'autoScalingGroupName',
        'honor_cooldown': 'honorCooldown',
        'policy_name': 'policyName'
    }

    def __init__(self, auto_scaling_group_name=None, honor_cooldown=None, policy_name=None):  # noqa: E501
        """ExecutePolicyRequest - a model defined in Swagger"""  # noqa: E501

        self._auto_scaling_group_name = None
        self._honor_cooldown = None
        self._policy_name = None
        self.discriminator = None

        self.auto_scaling_group_name = auto_scaling_group_name
        if honor_cooldown is not None:
            self.honor_cooldown = honor_cooldown
        self.policy_name = policy_name

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this ExecutePolicyRequest.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this ExecutePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this ExecutePolicyRequest.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this ExecutePolicyRequest.  # noqa: E501
        :type: str
        """
        if auto_scaling_group_name is None:
            raise ValueError("Invalid value for `auto_scaling_group_name`, must not be `None`")  # noqa: E501

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def honor_cooldown(self):
        """Gets the honor_cooldown of this ExecutePolicyRequest.  # noqa: E501

        쿨타운타임존중여부  # noqa: E501

        :return: The honor_cooldown of this ExecutePolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._honor_cooldown

    @honor_cooldown.setter
    def honor_cooldown(self, honor_cooldown):
        """Sets the honor_cooldown of this ExecutePolicyRequest.

        쿨타운타임존중여부  # noqa: E501

        :param honor_cooldown: The honor_cooldown of this ExecutePolicyRequest.  # noqa: E501
        :type: bool
        """

        self._honor_cooldown = honor_cooldown

    @property
    def policy_name(self):
        """Gets the policy_name of this ExecutePolicyRequest.  # noqa: E501

        정책명  # noqa: E501

        :return: The policy_name of this ExecutePolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ExecutePolicyRequest.

        정책명  # noqa: E501

        :param policy_name: The policy_name of this ExecutePolicyRequest.  # noqa: E501
        :type: str
        """
        if policy_name is None:
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

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
        if not isinstance(other, ExecutePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
