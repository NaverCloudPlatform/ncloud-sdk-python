# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.common_code import CommonCode  # noqa: F401,E501


class NetworkAclRule(object):
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
        'network_acl_no': 'str',
        'priority': 'int',
        'protocol_type': 'CommonCode',
        'port_range': 'str',
        'rule_action': 'CommonCode',
        'create_date': 'str',
        'ip_block': 'str',
        'network_acl_rule_type': 'CommonCode',
        'network_acl_rule_description': 'str'
    }

    attribute_map = {
        'network_acl_no': 'networkAclNo',
        'priority': 'priority',
        'protocol_type': 'protocolType',
        'port_range': 'portRange',
        'rule_action': 'ruleAction',
        'create_date': 'createDate',
        'ip_block': 'ipBlock',
        'network_acl_rule_type': 'networkAclRuleType',
        'network_acl_rule_description': 'networkAclRuleDescription'
    }

    def __init__(self, network_acl_no=None, priority=None, protocol_type=None, port_range=None, rule_action=None, create_date=None, ip_block=None, network_acl_rule_type=None, network_acl_rule_description=None):  # noqa: E501
        """NetworkAclRule - a model defined in Swagger"""  # noqa: E501

        self._network_acl_no = None
        self._priority = None
        self._protocol_type = None
        self._port_range = None
        self._rule_action = None
        self._create_date = None
        self._ip_block = None
        self._network_acl_rule_type = None
        self._network_acl_rule_description = None
        self.discriminator = None

        if network_acl_no is not None:
            self.network_acl_no = network_acl_no
        if priority is not None:
            self.priority = priority
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if port_range is not None:
            self.port_range = port_range
        if rule_action is not None:
            self.rule_action = rule_action
        if create_date is not None:
            self.create_date = create_date
        if ip_block is not None:
            self.ip_block = ip_block
        if network_acl_rule_type is not None:
            self.network_acl_rule_type = network_acl_rule_type
        if network_acl_rule_description is not None:
            self.network_acl_rule_description = network_acl_rule_description

    @property
    def network_acl_no(self):
        """Gets the network_acl_no of this NetworkAclRule.  # noqa: E501

        네트워크ACL번호  # noqa: E501

        :return: The network_acl_no of this NetworkAclRule.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_no

    @network_acl_no.setter
    def network_acl_no(self, network_acl_no):
        """Sets the network_acl_no of this NetworkAclRule.

        네트워크ACL번호  # noqa: E501

        :param network_acl_no: The network_acl_no of this NetworkAclRule.  # noqa: E501
        :type: str
        """

        self._network_acl_no = network_acl_no

    @property
    def priority(self):
        """Gets the priority of this NetworkAclRule.  # noqa: E501

        우선순위  # noqa: E501

        :return: The priority of this NetworkAclRule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NetworkAclRule.

        우선순위  # noqa: E501

        :param priority: The priority of this NetworkAclRule.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol_type(self):
        """Gets the protocol_type of this NetworkAclRule.  # noqa: E501

        프로토콜유형  # noqa: E501

        :return: The protocol_type of this NetworkAclRule.  # noqa: E501
        :rtype: CommonCode
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this NetworkAclRule.

        프로토콜유형  # noqa: E501

        :param protocol_type: The protocol_type of this NetworkAclRule.  # noqa: E501
        :type: CommonCode
        """

        self._protocol_type = protocol_type

    @property
    def port_range(self):
        """Gets the port_range of this NetworkAclRule.  # noqa: E501

        포트범위  # noqa: E501

        :return: The port_range of this NetworkAclRule.  # noqa: E501
        :rtype: str
        """
        return self._port_range

    @port_range.setter
    def port_range(self, port_range):
        """Sets the port_range of this NetworkAclRule.

        포트범위  # noqa: E501

        :param port_range: The port_range of this NetworkAclRule.  # noqa: E501
        :type: str
        """

        self._port_range = port_range

    @property
    def rule_action(self):
        """Gets the rule_action of this NetworkAclRule.  # noqa: E501

        Rule액션  # noqa: E501

        :return: The rule_action of this NetworkAclRule.  # noqa: E501
        :rtype: CommonCode
        """
        return self._rule_action

    @rule_action.setter
    def rule_action(self, rule_action):
        """Sets the rule_action of this NetworkAclRule.

        Rule액션  # noqa: E501

        :param rule_action: The rule_action of this NetworkAclRule.  # noqa: E501
        :type: CommonCode
        """

        self._rule_action = rule_action

    @property
    def create_date(self):
        """Gets the create_date of this NetworkAclRule.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this NetworkAclRule.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this NetworkAclRule.

        생성일시  # noqa: E501

        :param create_date: The create_date of this NetworkAclRule.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def ip_block(self):
        """Gets the ip_block of this NetworkAclRule.  # noqa: E501

        IP블록  # noqa: E501

        :return: The ip_block of this NetworkAclRule.  # noqa: E501
        :rtype: str
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        """Sets the ip_block of this NetworkAclRule.

        IP블록  # noqa: E501

        :param ip_block: The ip_block of this NetworkAclRule.  # noqa: E501
        :type: str
        """

        self._ip_block = ip_block

    @property
    def network_acl_rule_type(self):
        """Gets the network_acl_rule_type of this NetworkAclRule.  # noqa: E501

        네트워크ACLRule유형  # noqa: E501

        :return: The network_acl_rule_type of this NetworkAclRule.  # noqa: E501
        :rtype: CommonCode
        """
        return self._network_acl_rule_type

    @network_acl_rule_type.setter
    def network_acl_rule_type(self, network_acl_rule_type):
        """Sets the network_acl_rule_type of this NetworkAclRule.

        네트워크ACLRule유형  # noqa: E501

        :param network_acl_rule_type: The network_acl_rule_type of this NetworkAclRule.  # noqa: E501
        :type: CommonCode
        """

        self._network_acl_rule_type = network_acl_rule_type

    @property
    def network_acl_rule_description(self):
        """Gets the network_acl_rule_description of this NetworkAclRule.  # noqa: E501

        네트워크ACLRule설명  # noqa: E501

        :return: The network_acl_rule_description of this NetworkAclRule.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_rule_description

    @network_acl_rule_description.setter
    def network_acl_rule_description(self, network_acl_rule_description):
        """Sets the network_acl_rule_description of this NetworkAclRule.

        네트워크ACLRule설명  # noqa: E501

        :param network_acl_rule_description: The network_acl_rule_description of this NetworkAclRule.  # noqa: E501
        :type: str
        """

        self._network_acl_rule_description = network_acl_rule_description

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
        if not isinstance(other, NetworkAclRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other