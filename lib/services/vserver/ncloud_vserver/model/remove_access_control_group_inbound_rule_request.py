# coding: utf-8

"""
    vserver

    OpenAPI spec version: 2020-09-17T02:28:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.remove_access_control_group_rule_parameter import RemoveAccessControlGroupRuleParameter  # noqa: F401,E501


class RemoveAccessControlGroupInboundRuleRequest(object):
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
        'access_control_group_no': 'str',
        'vpc_no': 'str',
        'access_control_group_rule_list': 'list[RemoveAccessControlGroupRuleParameter]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'access_control_group_no': 'accessControlGroupNo',
        'vpc_no': 'vpcNo',
        'access_control_group_rule_list': 'accessControlGroupRuleList'
    }

    def __init__(self, region_code=None, access_control_group_no=None, vpc_no=None, access_control_group_rule_list=None):  # noqa: E501
        """RemoveAccessControlGroupInboundRuleRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._access_control_group_no = None
        self._vpc_no = None
        self._access_control_group_rule_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.access_control_group_no = access_control_group_no
        self.vpc_no = vpc_no
        self.access_control_group_rule_list = access_control_group_rule_list

    @property
    def region_code(self):
        """Gets the region_code of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this RemoveAccessControlGroupInboundRuleRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def access_control_group_no(self):
        """Gets the access_control_group_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501

        ACG번호  # noqa: E501

        :return: The access_control_group_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_no

    @access_control_group_no.setter
    def access_control_group_no(self, access_control_group_no):
        """Sets the access_control_group_no of this RemoveAccessControlGroupInboundRuleRequest.

        ACG번호  # noqa: E501

        :param access_control_group_no: The access_control_group_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :type: str
        """
        if access_control_group_no is None:
            raise ValueError("Invalid value for `access_control_group_no`, must not be `None`")  # noqa: E501

        self._access_control_group_no = access_control_group_no

    @property
    def vpc_no(self):
        """Gets the vpc_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this RemoveAccessControlGroupInboundRuleRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :type: str
        """
        if vpc_no is None:
            raise ValueError("Invalid value for `vpc_no`, must not be `None`")  # noqa: E501

        self._vpc_no = vpc_no

    @property
    def access_control_group_rule_list(self):
        """Gets the access_control_group_rule_list of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501

        ACGRule리스트  # noqa: E501

        :return: The access_control_group_rule_list of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :rtype: list[RemoveAccessControlGroupRuleParameter]
        """
        return self._access_control_group_rule_list

    @access_control_group_rule_list.setter
    def access_control_group_rule_list(self, access_control_group_rule_list):
        """Sets the access_control_group_rule_list of this RemoveAccessControlGroupInboundRuleRequest.

        ACGRule리스트  # noqa: E501

        :param access_control_group_rule_list: The access_control_group_rule_list of this RemoveAccessControlGroupInboundRuleRequest.  # noqa: E501
        :type: list[RemoveAccessControlGroupRuleParameter]
        """
        if access_control_group_rule_list is None:
            raise ValueError("Invalid value for `access_control_group_rule_list`, must not be `None`")  # noqa: E501

        self._access_control_group_rule_list = access_control_group_rule_list

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
        if not isinstance(other, RemoveAccessControlGroupInboundRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
