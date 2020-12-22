# coding: utf-8

"""
    vserver

    
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
        'region_code': 'str',
        'access_control_group_no_list': 'list[str]',
        'network_interface_description': 'str',
        'network_interface_name': 'str',
        'subnet_no': 'str',
        'vpc_no': 'str',
        'server_instance_no': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'access_control_group_no_list': 'accessControlGroupNoList',
        'network_interface_description': 'networkInterfaceDescription',
        'network_interface_name': 'networkInterfaceName',
        'subnet_no': 'subnetNo',
        'vpc_no': 'vpcNo',
        'server_instance_no': 'serverInstanceNo',
        'ip': 'ip'
    }

    def __init__(self, region_code=None, access_control_group_no_list=None, network_interface_description=None, network_interface_name=None, subnet_no=None, vpc_no=None, server_instance_no=None, ip=None):  # noqa: E501
        """CreateNetworkInterfaceRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._access_control_group_no_list = None
        self._network_interface_description = None
        self._network_interface_name = None
        self._subnet_no = None
        self._vpc_no = None
        self._server_instance_no = None
        self._ip = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.access_control_group_no_list = access_control_group_no_list
        if network_interface_description is not None:
            self.network_interface_description = network_interface_description
        if network_interface_name is not None:
            self.network_interface_name = network_interface_name
        self.subnet_no = subnet_no
        self.vpc_no = vpc_no
        if server_instance_no is not None:
            self.server_instance_no = server_instance_no
        if ip is not None:
            self.ip = ip

    @property
    def region_code(self):
        """Gets the region_code of this CreateNetworkInterfaceRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateNetworkInterfaceRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def access_control_group_no_list(self):
        """Gets the access_control_group_no_list of this CreateNetworkInterfaceRequest.  # noqa: E501

        ACG번호리스트  # noqa: E501

        :return: The access_control_group_no_list of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_control_group_no_list

    @access_control_group_no_list.setter
    def access_control_group_no_list(self, access_control_group_no_list):
        """Sets the access_control_group_no_list of this CreateNetworkInterfaceRequest.

        ACG번호리스트  # noqa: E501

        :param access_control_group_no_list: The access_control_group_no_list of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: list[str]
        """
        if access_control_group_no_list is None:
            raise ValueError("Invalid value for `access_control_group_no_list`, must not be `None`")  # noqa: E501

        self._access_control_group_no_list = access_control_group_no_list

    @property
    def network_interface_description(self):
        """Gets the network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501

        네트워크인터페이스설명  # noqa: E501

        :return: The network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_description

    @network_interface_description.setter
    def network_interface_description(self, network_interface_description):
        """Sets the network_interface_description of this CreateNetworkInterfaceRequest.

        네트워크인터페이스설명  # noqa: E501

        :param network_interface_description: The network_interface_description of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_description = network_interface_description

    @property
    def network_interface_name(self):
        """Gets the network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501

        네트워크인터페이스이름  # noqa: E501

        :return: The network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_name

    @network_interface_name.setter
    def network_interface_name(self, network_interface_name):
        """Sets the network_interface_name of this CreateNetworkInterfaceRequest.

        네트워크인터페이스이름  # noqa: E501

        :param network_interface_name: The network_interface_name of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_name = network_interface_name

    @property
    def subnet_no(self):
        """Gets the subnet_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        서브넷번호  # noqa: E501

        :return: The subnet_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_no

    @subnet_no.setter
    def subnet_no(self, subnet_no):
        """Sets the subnet_no of this CreateNetworkInterfaceRequest.

        서브넷번호  # noqa: E501

        :param subnet_no: The subnet_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if subnet_no is None:
            raise ValueError("Invalid value for `subnet_no`, must not be `None`")  # noqa: E501

        self._subnet_no = subnet_no

    @property
    def vpc_no(self):
        """Gets the vpc_no of this CreateNetworkInterfaceRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this CreateNetworkInterfaceRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """
        if vpc_no is None:
            raise ValueError("Invalid value for `vpc_no`, must not be `None`")  # noqa: E501

        self._vpc_no = vpc_no

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

    @property
    def ip(self):
        """Gets the ip of this CreateNetworkInterfaceRequest.  # noqa: E501

        IP주소  # noqa: E501

        :return: The ip of this CreateNetworkInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CreateNetworkInterfaceRequest.

        IP주소  # noqa: E501

        :param ip: The ip of this CreateNetworkInterfaceRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

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