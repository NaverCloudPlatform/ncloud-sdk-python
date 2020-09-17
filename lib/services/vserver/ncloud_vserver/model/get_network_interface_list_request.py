# coding: utf-8

"""
    vserver

    OpenAPI spec version: 2020-09-17T02:28:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetNetworkInterfaceListRequest(object):
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
        'network_interface_no_list': 'list[str]',
        'ip': 'str',
        'network_interface_name': 'str',
        'server_name': 'str',
        'subnet_name': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'network_interface_no_list': 'networkInterfaceNoList',
        'ip': 'ip',
        'network_interface_name': 'networkInterfaceName',
        'server_name': 'serverName',
        'subnet_name': 'subnetName',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, region_code=None, network_interface_no_list=None, ip=None, network_interface_name=None, server_name=None, subnet_name=None, page_no=None, page_size=None):  # noqa: E501
        """GetNetworkInterfaceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._network_interface_no_list = None
        self._ip = None
        self._network_interface_name = None
        self._server_name = None
        self._subnet_name = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if network_interface_no_list is not None:
            self.network_interface_no_list = network_interface_no_list
        if ip is not None:
            self.ip = ip
        if network_interface_name is not None:
            self.network_interface_name = network_interface_name
        if server_name is not None:
            self.server_name = server_name
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def region_code(self):
        """Gets the region_code of this GetNetworkInterfaceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetNetworkInterfaceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def network_interface_no_list(self):
        """Gets the network_interface_no_list of this GetNetworkInterfaceListRequest.  # noqa: E501

        네트워크인터페이스번호리스트  # noqa: E501

        :return: The network_interface_no_list of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_interface_no_list

    @network_interface_no_list.setter
    def network_interface_no_list(self, network_interface_no_list):
        """Sets the network_interface_no_list of this GetNetworkInterfaceListRequest.

        네트워크인터페이스번호리스트  # noqa: E501

        :param network_interface_no_list: The network_interface_no_list of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._network_interface_no_list = network_interface_no_list

    @property
    def ip(self):
        """Gets the ip of this GetNetworkInterfaceListRequest.  # noqa: E501

        IP주소  # noqa: E501

        :return: The ip of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetNetworkInterfaceListRequest.

        IP주소  # noqa: E501

        :param ip: The ip of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def network_interface_name(self):
        """Gets the network_interface_name of this GetNetworkInterfaceListRequest.  # noqa: E501

        네트워크인터페이스이름  # noqa: E501

        :return: The network_interface_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_name

    @network_interface_name.setter
    def network_interface_name(self, network_interface_name):
        """Sets the network_interface_name of this GetNetworkInterfaceListRequest.

        네트워크인터페이스이름  # noqa: E501

        :param network_interface_name: The network_interface_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_name = network_interface_name

    @property
    def server_name(self):
        """Gets the server_name of this GetNetworkInterfaceListRequest.  # noqa: E501

        서버이름  # noqa: E501

        :return: The server_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this GetNetworkInterfaceListRequest.

        서버이름  # noqa: E501

        :param server_name: The server_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def subnet_name(self):
        """Gets the subnet_name of this GetNetworkInterfaceListRequest.  # noqa: E501

        서브넷이름  # noqa: E501

        :return: The subnet_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this GetNetworkInterfaceListRequest.

        서브넷이름  # noqa: E501

        :param subnet_name: The subnet_name of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def page_no(self):
        """Gets the page_no of this GetNetworkInterfaceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetNetworkInterfaceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetNetworkInterfaceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetNetworkInterfaceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetNetworkInterfaceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetNetworkInterfaceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if not isinstance(other, GetNetworkInterfaceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
