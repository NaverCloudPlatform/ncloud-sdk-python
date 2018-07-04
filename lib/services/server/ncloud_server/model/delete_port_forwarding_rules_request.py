# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-07-02T09:06:17Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_server.model.port_forwarding_rule_parameter import PortForwardingRuleParameter  # noqa: F401,E501


class DeletePortForwardingRulesRequest(object):
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
        'port_forwarding_configuration_no': 'str',
        'port_forwarding_rule_list': 'list[PortForwardingRuleParameter]'
    }

    attribute_map = {
        'port_forwarding_configuration_no': 'portForwardingConfigurationNo',
        'port_forwarding_rule_list': 'portForwardingRuleList'
    }

    def __init__(self, port_forwarding_configuration_no=None, port_forwarding_rule_list=None):  # noqa: E501
        """DeletePortForwardingRulesRequest - a model defined in Swagger"""  # noqa: E501

        self._port_forwarding_configuration_no = None
        self._port_forwarding_rule_list = None
        self.discriminator = None

        self.port_forwarding_configuration_no = port_forwarding_configuration_no
        self.port_forwarding_rule_list = port_forwarding_rule_list

    @property
    def port_forwarding_configuration_no(self):
        """Gets the port_forwarding_configuration_no of this DeletePortForwardingRulesRequest.  # noqa: E501

        포트포워딩설정번호  # noqa: E501

        :return: The port_forwarding_configuration_no of this DeletePortForwardingRulesRequest.  # noqa: E501
        :rtype: str
        """
        return self._port_forwarding_configuration_no

    @port_forwarding_configuration_no.setter
    def port_forwarding_configuration_no(self, port_forwarding_configuration_no):
        """Sets the port_forwarding_configuration_no of this DeletePortForwardingRulesRequest.

        포트포워딩설정번호  # noqa: E501

        :param port_forwarding_configuration_no: The port_forwarding_configuration_no of this DeletePortForwardingRulesRequest.  # noqa: E501
        :type: str
        """
        if port_forwarding_configuration_no is None:
            raise ValueError("Invalid value for `port_forwarding_configuration_no`, must not be `None`")  # noqa: E501

        self._port_forwarding_configuration_no = port_forwarding_configuration_no

    @property
    def port_forwarding_rule_list(self):
        """Gets the port_forwarding_rule_list of this DeletePortForwardingRulesRequest.  # noqa: E501

        포트포워딩RULE리스트  # noqa: E501

        :return: The port_forwarding_rule_list of this DeletePortForwardingRulesRequest.  # noqa: E501
        :rtype: list[PortForwardingRuleParameter]
        """
        return self._port_forwarding_rule_list

    @port_forwarding_rule_list.setter
    def port_forwarding_rule_list(self, port_forwarding_rule_list):
        """Sets the port_forwarding_rule_list of this DeletePortForwardingRulesRequest.

        포트포워딩RULE리스트  # noqa: E501

        :param port_forwarding_rule_list: The port_forwarding_rule_list of this DeletePortForwardingRulesRequest.  # noqa: E501
        :type: list[PortForwardingRuleParameter]
        """
        if port_forwarding_rule_list is None:
            raise ValueError("Invalid value for `port_forwarding_rule_list`, must not be `None`")  # noqa: E501

        self._port_forwarding_rule_list = port_forwarding_rule_list

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
        if not isinstance(other, DeletePortForwardingRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
