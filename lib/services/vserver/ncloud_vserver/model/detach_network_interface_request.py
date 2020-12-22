# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DetachNetworkInterfaceRequest(object):
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
        'server_instance_no': 'str',
        'network_interface_no': 'str',
        'subnet_no': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'server_instance_no': 'serverInstanceNo',
        'network_interface_no': 'networkInterfaceNo',
        'subnet_no': 'subnetNo'
    }

    def __init__(self, region_code=None, server_instance_no=None, network_interface_no=None, subnet_no=None):  # noqa: E501
        """DetachNetworkInterfaceRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._server_instance_no = None
        self._network_interface_no = None
        self._subnet_no = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.server_instance_no = server_instance_no
        self.network_interface_no = network_interface_no
        self.subnet_no = subnet_no

    @property
    def region_code(self):
        """Gets the region_code of this DetachNetworkInterfaceRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this DetachNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this DetachNetworkInterfaceRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this DetachNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this DetachNetworkInterfaceRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this DetachNetworkInterfaceRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if server_instance_no is None:
            raise ValueError("Invalid value for `server_instance_no`, must not be `None`")  # noqa: E501

        self._server_instance_no = server_instance_no

    @property
    def network_interface_no(self):
        """Gets the network_interface_no of this DetachNetworkInterfaceRequest.  # noqa: E501

        네트워크인터페이스번호  # noqa: E501

        :return: The network_interface_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_no

    @network_interface_no.setter
    def network_interface_no(self, network_interface_no):
        """Sets the network_interface_no of this DetachNetworkInterfaceRequest.

        네트워크인터페이스번호  # noqa: E501

        :param network_interface_no: The network_interface_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if network_interface_no is None:
            raise ValueError("Invalid value for `network_interface_no`, must not be `None`")  # noqa: E501

        self._network_interface_no = network_interface_no

    @property
    def subnet_no(self):
        """Gets the subnet_no of this DetachNetworkInterfaceRequest.  # noqa: E501

        서브넷번호  # noqa: E501

        :return: The subnet_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_no

    @subnet_no.setter
    def subnet_no(self, subnet_no):
        """Sets the subnet_no of this DetachNetworkInterfaceRequest.

        서브넷번호  # noqa: E501

        :param subnet_no: The subnet_no of this DetachNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if subnet_no is None:
            raise ValueError("Invalid value for `subnet_no`, must not be `None`")  # noqa: E501

        self._subnet_no = subnet_no

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
        if not isinstance(other, DetachNetworkInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
