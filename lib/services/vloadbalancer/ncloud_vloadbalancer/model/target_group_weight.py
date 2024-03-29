# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TargetGroupWeight(object):
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
        'target_group_no': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'target_group_no': 'targetGroupNo',
        'weight': 'weight'
    }

    def __init__(self, target_group_no=None, weight=None):  # noqa: E501
        """TargetGroupWeight - a model defined in Swagger"""  # noqa: E501

        self._target_group_no = None
        self._weight = None
        self.discriminator = None

        if target_group_no is not None:
            self.target_group_no = target_group_no
        if weight is not None:
            self.weight = weight

    @property
    def target_group_no(self):
        """Gets the target_group_no of this TargetGroupWeight.  # noqa: E501

        타겟그룹번호  # noqa: E501

        :return: The target_group_no of this TargetGroupWeight.  # noqa: E501
        :rtype: str
        """
        return self._target_group_no

    @target_group_no.setter
    def target_group_no(self, target_group_no):
        """Sets the target_group_no of this TargetGroupWeight.

        타겟그룹번호  # noqa: E501

        :param target_group_no: The target_group_no of this TargetGroupWeight.  # noqa: E501
        :type: str
        """

        self._target_group_no = target_group_no

    @property
    def weight(self):
        """Gets the weight of this TargetGroupWeight.  # noqa: E501

        가중치  # noqa: E501

        :return: The weight of this TargetGroupWeight.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TargetGroupWeight.

        가중치  # noqa: E501

        :param weight: The weight of this TargetGroupWeight.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if not isinstance(other, TargetGroupWeight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
