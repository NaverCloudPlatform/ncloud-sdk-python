# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-07-02T07:25:18Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PortForwardingRuleParameter(object):
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
        'port_forwarding_external_port': 'int',
        'port_forwarding_internal_port': 'int',
        'server_instance_no': 'str'
    }

    attribute_map = {
        'port_forwarding_external_port': 'portForwardingExternalPort',
        'port_forwarding_internal_port': 'portForwardingInternalPort',
        'server_instance_no': 'serverInstanceNo'
    }

    def __init__(self, port_forwarding_external_port=None, port_forwarding_internal_port=None, server_instance_no=None):  # noqa: E501
        """PortForwardingRuleParameter - a model defined in Swagger"""  # noqa: E501

        self._port_forwarding_external_port = None
        self._port_forwarding_internal_port = None
        self._server_instance_no = None
        self.discriminator = None

        self.port_forwarding_external_port = port_forwarding_external_port
        self.port_forwarding_internal_port = port_forwarding_internal_port
        self.server_instance_no = server_instance_no

    @property
    def port_forwarding_external_port(self):
        """Gets the port_forwarding_external_port of this PortForwardingRuleParameter.  # noqa: E501

        포트포워딩외부포트  # noqa: E501

        :return: The port_forwarding_external_port of this PortForwardingRuleParameter.  # noqa: E501
        :rtype: int
        """
        return self._port_forwarding_external_port

    @port_forwarding_external_port.setter
    def port_forwarding_external_port(self, port_forwarding_external_port):
        """Sets the port_forwarding_external_port of this PortForwardingRuleParameter.

        포트포워딩외부포트  # noqa: E501

        :param port_forwarding_external_port: The port_forwarding_external_port of this PortForwardingRuleParameter.  # noqa: E501
        :type: int
        """
        if port_forwarding_external_port is None:
            raise ValueError("Invalid value for `port_forwarding_external_port`, must not be `None`")  # noqa: E501

        self._port_forwarding_external_port = port_forwarding_external_port

    @property
    def port_forwarding_internal_port(self):
        """Gets the port_forwarding_internal_port of this PortForwardingRuleParameter.  # noqa: E501

        포트포워딩내부포트  # noqa: E501

        :return: The port_forwarding_internal_port of this PortForwardingRuleParameter.  # noqa: E501
        :rtype: int
        """
        return self._port_forwarding_internal_port

    @port_forwarding_internal_port.setter
    def port_forwarding_internal_port(self, port_forwarding_internal_port):
        """Sets the port_forwarding_internal_port of this PortForwardingRuleParameter.

        포트포워딩내부포트  # noqa: E501

        :param port_forwarding_internal_port: The port_forwarding_internal_port of this PortForwardingRuleParameter.  # noqa: E501
        :type: int
        """
        if port_forwarding_internal_port is None:
            raise ValueError("Invalid value for `port_forwarding_internal_port`, must not be `None`")  # noqa: E501

        self._port_forwarding_internal_port = port_forwarding_internal_port

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this PortForwardingRuleParameter.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this PortForwardingRuleParameter.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this PortForwardingRuleParameter.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this PortForwardingRuleParameter.  # noqa: E501
        :type: str
        """
        if server_instance_no is None:
            raise ValueError("Invalid value for `server_instance_no`, must not be `None`")  # noqa: E501

        self._server_instance_no = server_instance_no

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
        if not isinstance(other, PortForwardingRuleParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
