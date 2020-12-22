# coding: utf-8

"""
    server

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateNetworkInterfaceRequest(object):
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
        'private_subnet_instance_no': 'str',
        'network_interface_name': 'str',
        'network_interface_ip': 'str',
        'network_interface_description': 'str',
        'region_no': 'str',
        'zone_no': 'str',
        'server_instance_no': 'str'
    }

    attribute_map = {
        'private_subnet_instance_no': 'privateSubnetInstanceNo',
        'network_interface_name': 'networkInterfaceName',
        'network_interface_ip': 'networkInterfaceIp',
        'network_interface_description': 'networkInterfaceDescription',
        'region_no': 'regionNo',
        'zone_no': 'zoneNo',
        'server_instance_no': 'serverInstanceNo'
    }

    def __init__(self, private_subnet_instance_no=None, network_interface_name=None, network_interface_ip=None, network_interface_description=None, region_no=None, zone_no=None, server_instance_no=None):  # noqa: E501
        """CreateNetworkInterfaceRequest - a model defined in Swagger"""  # noqa: E501

        self._private_subnet_instance_no = None
        self._network_interface_name = None
        self._network_interface_ip = None
        self._network_interface_description = None
        self._region_no = None
        self._zone_no = None
        self._server_instance_no = None
        self.discriminator = None

        self.private_subnet_instance_no = private_subnet_instance_no
        self.network_interface_name = network_interface_name
        self.network_interface_ip = network_interface_ip
        if network_interface_description is not None:
            self.network_interface_description = network_interface_description
        if region_no is not None:
            self.region_no = region_no
        if zone_no is not None:
            self.zone_no = zone_no
        if server_instance_no is not None:
            self.server_instance_no = server_instance_no

    @property
    def private_subnet_instance_no(self):
        """Gets the private_subnet_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        Private Subnet인스턴스번호  # noqa: E501

        :return: The private_subnet_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_subnet_instance_no

    @private_subnet_instance_no.setter
    def private_subnet_instance_no(self, private_subnet_instance_no):
        """Sets the private_subnet_instance_no of this CreateNetworkInterfaceRequest.

        Private Subnet인스턴스번호  # noqa: E501

        :param private_subnet_instance_no: The private_subnet_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if private_subnet_instance_no is None:
            raise ValueError("Invalid value for `private_subnet_instance_no`, must not be `None`")  # noqa: E501

        self._private_subnet_instance_no = private_subnet_instance_no

    @property
    def network_interface_name(self):
        """Gets the network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501

        Network Interface이름  # noqa: E501

        :return: The network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_name

    @network_interface_name.setter
    def network_interface_name(self, network_interface_name):
        """Sets the network_interface_name of this CreateNetworkInterfaceRequest.

        Network Interface이름  # noqa: E501

        :param network_interface_name: The network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if network_interface_name is None:
            raise ValueError("Invalid value for `network_interface_name`, must not be `None`")  # noqa: E501

        self._network_interface_name = network_interface_name

    @property
    def network_interface_ip(self):
        """Gets the network_interface_ip of this CreateNetworkInterfaceRequest.  # noqa: E501

        Network Interface IP  # noqa: E501

        :return: The network_interface_ip of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_ip

    @network_interface_ip.setter
    def network_interface_ip(self, network_interface_ip):
        """Sets the network_interface_ip of this CreateNetworkInterfaceRequest.

        Network Interface IP  # noqa: E501

        :param network_interface_ip: The network_interface_ip of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if network_interface_ip is None:
            raise ValueError("Invalid value for `network_interface_ip`, must not be `None`")  # noqa: E501

        self._network_interface_ip = network_interface_ip

    @property
    def network_interface_description(self):
        """Gets the network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501

        Network Interface설명  # noqa: E501

        :return: The network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_description

    @network_interface_description.setter
    def network_interface_description(self, network_interface_description):
        """Sets the network_interface_description of this CreateNetworkInterfaceRequest.

        Network Interface설명  # noqa: E501

        :param network_interface_description: The network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_description = network_interface_description

    @property
    def region_no(self):
        """Gets the region_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this CreateNetworkInterfaceRequest.

        리전번호  # noqa: E501

        :param region_no: The region_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

    @property
    def zone_no(self):
        """Gets the zone_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        ZONE번호  # noqa: E501

        :return: The zone_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_no

    @zone_no.setter
    def zone_no(self, zone_no):
        """Sets the zone_no of this CreateNetworkInterfaceRequest.

        ZONE번호  # noqa: E501

        :param zone_no: The zone_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._zone_no = zone_no

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this CreateNetworkInterfaceRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, CreateNetworkInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
