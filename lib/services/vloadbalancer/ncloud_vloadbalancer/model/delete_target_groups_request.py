# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeleteTargetGroupsRequest(object):
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
        'region_code': 'str',
        'target_group_no_list': 'list[str]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'target_group_no_list': 'targetGroupNoList'
    }

    def __init__(self, region_code=None, target_group_no_list=None):  # noqa: E501
        """DeleteTargetGroupsRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._target_group_no_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.target_group_no_list = target_group_no_list

    @property
    def region_code(self):
        """Gets the region_code of this DeleteTargetGroupsRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this DeleteTargetGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this DeleteTargetGroupsRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this DeleteTargetGroupsRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def target_group_no_list(self):
        """Gets the target_group_no_list of this DeleteTargetGroupsRequest.  # noqa: E501

        타겟그룹번호리스트  # noqa: E501

        :return: The target_group_no_list of this DeleteTargetGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_group_no_list

    @target_group_no_list.setter
    def target_group_no_list(self, target_group_no_list):
        """Sets the target_group_no_list of this DeleteTargetGroupsRequest.

        타겟그룹번호리스트  # noqa: E501

        :param target_group_no_list: The target_group_no_list of this DeleteTargetGroupsRequest.  # noqa: E501
        :type: list[str]
        """
        if target_group_no_list is None:
            raise ValueError("Invalid value for `target_group_no_list`, must not be `None`")  # noqa: E501

        self._target_group_no_list = target_group_no_list

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
        if not isinstance(other, DeleteTargetGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
