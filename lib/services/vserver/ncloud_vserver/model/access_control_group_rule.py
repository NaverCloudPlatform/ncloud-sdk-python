# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.common_code import CommonCode  # noqa: F401,E501


class AccessControlGroupRule(object):
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
        'access_control_group_no': 'str',
        'protocol_type': 'CommonCode',
        'ip_block': 'str',
        'port_range': 'str',
        'access_control_group_sequence': 'str',
        'access_control_group_rule_type': 'CommonCode',
        'access_control_group_rule_description': 'str'
    }

    attribute_map = {
        'access_control_group_no': 'accessControlGroupNo',
        'protocol_type': 'protocolType',
        'ip_block': 'ipBlock',
        'port_range': 'portRange',
        'access_control_group_sequence': 'accessControlGroupSequence',
        'access_control_group_rule_type': 'accessControlGroupRuleType',
        'access_control_group_rule_description': 'accessControlGroupRuleDescription'
    }

    def __init__(self, access_control_group_no=None, protocol_type=None, ip_block=None, port_range=None, access_control_group_sequence=None, access_control_group_rule_type=None, access_control_group_rule_description=None):  # noqa: E501
        """AccessControlGroupRule - a model defined in Swagger"""  # noqa: E501

        self._access_control_group_no = None
        self._protocol_type = None
        self._ip_block = None
        self._port_range = None
        self._access_control_group_sequence = None
        self._access_control_group_rule_type = None
        self._access_control_group_rule_description = None
        self.discriminator = None

        if access_control_group_no is not None:
            self.access_control_group_no = access_control_group_no
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if ip_block is not None:
            self.ip_block = ip_block
        if port_range is not None:
            self.port_range = port_range
        if access_control_group_sequence is not None:
            self.access_control_group_sequence = access_control_group_sequence
        if access_control_group_rule_type is not None:
            self.access_control_group_rule_type = access_control_group_rule_type
        if access_control_group_rule_description is not None:
            self.access_control_group_rule_description = access_control_group_rule_description

    @property
    def access_control_group_no(self):
        """Gets the access_control_group_no of this AccessControlGroupRule.  # noqa: E501

        ACG번호  # noqa: E501

        :return: The access_control_group_no of this AccessControlGroupRule.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_no

    @access_control_group_no.setter
    def access_control_group_no(self, access_control_group_no):
        """Sets the access_control_group_no of this AccessControlGroupRule.

        ACG번호  # noqa: E501

        :param access_control_group_no: The access_control_group_no of this AccessControlGroupRule.  # noqa: E501
        :type: str
        """

        self._access_control_group_no = access_control_group_no

    @property
    def protocol_type(self):
        """Gets the protocol_type of this AccessControlGroupRule.  # noqa: E501

        프로토콜유형  # noqa: E501

        :return: The protocol_type of this AccessControlGroupRule.  # noqa: E501
        :rtype: CommonCode
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this AccessControlGroupRule.

        프로토콜유형  # noqa: E501

        :param protocol_type: The protocol_type of this AccessControlGroupRule.  # noqa: E501
        :type: CommonCode
        """

        self._protocol_type = protocol_type

    @property
    def ip_block(self):
        """Gets the ip_block of this AccessControlGroupRule.  # noqa: E501

        IP블록  # noqa: E501

        :return: The ip_block of this AccessControlGroupRule.  # noqa: E501
        :rtype: str
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        """Sets the ip_block of this AccessControlGroupRule.

        IP블록  # noqa: E501

        :param ip_block: The ip_block of this AccessControlGroupRule.  # noqa: E501
        :type: str
        """

        self._ip_block = ip_block

    @property
    def port_range(self):
        """Gets the port_range of this AccessControlGroupRule.  # noqa: E501

        포트범위  # noqa: E501

        :return: The port_range of this AccessControlGroupRule.  # noqa: E501
        :rtype: str
        """
        return self._port_range

    @port_range.setter
    def port_range(self, port_range):
        """Sets the port_range of this AccessControlGroupRule.

        포트범위  # noqa: E501

        :param port_range: The port_range of this AccessControlGroupRule.  # noqa: E501
        :type: str
        """

        self._port_range = port_range

    @property
    def access_control_group_sequence(self):
        """Gets the access_control_group_sequence of this AccessControlGroupRule.  # noqa: E501

        접근소스ACG  # noqa: E501

        :return: The access_control_group_sequence of this AccessControlGroupRule.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_sequence

    @access_control_group_sequence.setter
    def access_control_group_sequence(self, access_control_group_sequence):
        """Sets the access_control_group_sequence of this AccessControlGroupRule.

        접근소스ACG  # noqa: E501

        :param access_control_group_sequence: The access_control_group_sequence of this AccessControlGroupRule.  # noqa: E501
        :type: str
        """

        self._access_control_group_sequence = access_control_group_sequence

    @property
    def access_control_group_rule_type(self):
        """Gets the access_control_group_rule_type of this AccessControlGroupRule.  # noqa: E501

        ACGRule유형  # noqa: E501

        :return: The access_control_group_rule_type of this AccessControlGroupRule.  # noqa: E501
        :rtype: CommonCode
        """
        return self._access_control_group_rule_type

    @access_control_group_rule_type.setter
    def access_control_group_rule_type(self, access_control_group_rule_type):
        """Sets the access_control_group_rule_type of this AccessControlGroupRule.

        ACGRule유형  # noqa: E501

        :param access_control_group_rule_type: The access_control_group_rule_type of this AccessControlGroupRule.  # noqa: E501
        :type: CommonCode
        """

        self._access_control_group_rule_type = access_control_group_rule_type

    @property
    def access_control_group_rule_description(self):
        """Gets the access_control_group_rule_description of this AccessControlGroupRule.  # noqa: E501

        ACGRule설명  # noqa: E501

        :return: The access_control_group_rule_description of this AccessControlGroupRule.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_rule_description

    @access_control_group_rule_description.setter
    def access_control_group_rule_description(self, access_control_group_rule_description):
        """Sets the access_control_group_rule_description of this AccessControlGroupRule.

        ACGRule설명  # noqa: E501

        :param access_control_group_rule_description: The access_control_group_rule_description of this AccessControlGroupRule.  # noqa: E501
        :type: str
        """

        self._access_control_group_rule_description = access_control_group_rule_description

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
        if not isinstance(other, AccessControlGroupRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
