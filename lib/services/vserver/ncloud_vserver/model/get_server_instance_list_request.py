# coding: utf-8

"""
    vserver

    OpenAPI spec version: 2020-09-17T02:28:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetServerInstanceListRequest(object):
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
        'server_instance_no_list': 'list[str]',
        'vpc_no': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'server_instance_status_code': 'str',
        'base_block_storage_disk_type_code': 'str',
        'base_block_storage_disk_detail_type_code': 'str',
        'server_name': 'str',
        'ip': 'str',
        'sorted_by': 'str',
        'sorting_order': 'str',
        'placement_group_no_list': 'list[str]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'server_instance_no_list': 'serverInstanceNoList',
        'vpc_no': 'vpcNo',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'server_instance_status_code': 'serverInstanceStatusCode',
        'base_block_storage_disk_type_code': 'baseBlockStorageDiskTypeCode',
        'base_block_storage_disk_detail_type_code': 'baseBlockStorageDiskDetailTypeCode',
        'server_name': 'serverName',
        'ip': 'ip',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder',
        'placement_group_no_list': 'placementGroupNoList'
    }

    def __init__(self, region_code=None, server_instance_no_list=None, vpc_no=None, page_no=None, page_size=None, server_instance_status_code=None, base_block_storage_disk_type_code=None, base_block_storage_disk_detail_type_code=None, server_name=None, ip=None, sorted_by=None, sorting_order=None, placement_group_no_list=None):  # noqa: E501
        """GetServerInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._server_instance_no_list = None
        self._vpc_no = None
        self._page_no = None
        self._page_size = None
        self._server_instance_status_code = None
        self._base_block_storage_disk_type_code = None
        self._base_block_storage_disk_detail_type_code = None
        self._server_name = None
        self._ip = None
        self._sorted_by = None
        self._sorting_order = None
        self._placement_group_no_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if server_instance_no_list is not None:
            self.server_instance_no_list = server_instance_no_list
        if vpc_no is not None:
            self.vpc_no = vpc_no
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if server_instance_status_code is not None:
            self.server_instance_status_code = server_instance_status_code
        if base_block_storage_disk_type_code is not None:
            self.base_block_storage_disk_type_code = base_block_storage_disk_type_code
        if base_block_storage_disk_detail_type_code is not None:
            self.base_block_storage_disk_detail_type_code = base_block_storage_disk_detail_type_code
        if server_name is not None:
            self.server_name = server_name
        if ip is not None:
            self.ip = ip
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order
        if placement_group_no_list is not None:
            self.placement_group_no_list = placement_group_no_list

    @property
    def region_code(self):
        """Gets the region_code of this GetServerInstanceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetServerInstanceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def server_instance_no_list(self):
        """Gets the server_instance_no_list of this GetServerInstanceListRequest.  # noqa: E501

        서버인스턴스번호리스트  # noqa: E501

        :return: The server_instance_no_list of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_instance_no_list

    @server_instance_no_list.setter
    def server_instance_no_list(self, server_instance_no_list):
        """Sets the server_instance_no_list of this GetServerInstanceListRequest.

        서버인스턴스번호리스트  # noqa: E501

        :param server_instance_no_list: The server_instance_no_list of this GetServerInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._server_instance_no_list = server_instance_no_list

    @property
    def vpc_no(self):
        """Gets the vpc_no of this GetServerInstanceListRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this GetServerInstanceListRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_no = vpc_no

    @property
    def page_no(self):
        """Gets the page_no of this GetServerInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetServerInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetServerInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetServerInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetServerInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetServerInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def server_instance_status_code(self):
        """Gets the server_instance_status_code of this GetServerInstanceListRequest.  # noqa: E501

        서버인스턴스상태코드  # noqa: E501

        :return: The server_instance_status_code of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_status_code

    @server_instance_status_code.setter
    def server_instance_status_code(self, server_instance_status_code):
        """Sets the server_instance_status_code of this GetServerInstanceListRequest.

        서버인스턴스상태코드  # noqa: E501

        :param server_instance_status_code: The server_instance_status_code of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._server_instance_status_code = server_instance_status_code

    @property
    def base_block_storage_disk_type_code(self):
        """Gets the base_block_storage_disk_type_code of this GetServerInstanceListRequest.  # noqa: E501

        기본블록스토리지디스크유형코드  # noqa: E501

        :return: The base_block_storage_disk_type_code of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_block_storage_disk_type_code

    @base_block_storage_disk_type_code.setter
    def base_block_storage_disk_type_code(self, base_block_storage_disk_type_code):
        """Sets the base_block_storage_disk_type_code of this GetServerInstanceListRequest.

        기본블록스토리지디스크유형코드  # noqa: E501

        :param base_block_storage_disk_type_code: The base_block_storage_disk_type_code of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._base_block_storage_disk_type_code = base_block_storage_disk_type_code

    @property
    def base_block_storage_disk_detail_type_code(self):
        """Gets the base_block_storage_disk_detail_type_code of this GetServerInstanceListRequest.  # noqa: E501

        기본블록스토리지디스크상세유형코드  # noqa: E501

        :return: The base_block_storage_disk_detail_type_code of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_block_storage_disk_detail_type_code

    @base_block_storage_disk_detail_type_code.setter
    def base_block_storage_disk_detail_type_code(self, base_block_storage_disk_detail_type_code):
        """Sets the base_block_storage_disk_detail_type_code of this GetServerInstanceListRequest.

        기본블록스토리지디스크상세유형코드  # noqa: E501

        :param base_block_storage_disk_detail_type_code: The base_block_storage_disk_detail_type_code of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._base_block_storage_disk_detail_type_code = base_block_storage_disk_detail_type_code

    @property
    def server_name(self):
        """Gets the server_name of this GetServerInstanceListRequest.  # noqa: E501

        서버인스턴스이름  # noqa: E501

        :return: The server_name of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this GetServerInstanceListRequest.

        서버인스턴스이름  # noqa: E501

        :param server_name: The server_name of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def ip(self):
        """Gets the ip of this GetServerInstanceListRequest.  # noqa: E501

        IP주소  # noqa: E501

        :return: The ip of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetServerInstanceListRequest.

        IP주소  # noqa: E501

        :param ip: The ip of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetServerInstanceListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetServerInstanceListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetServerInstanceListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetServerInstanceListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetServerInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

    @property
    def placement_group_no_list(self):
        """Gets the placement_group_no_list of this GetServerInstanceListRequest.  # noqa: E501

        물리배치그룹번호리스트  # noqa: E501

        :return: The placement_group_no_list of this GetServerInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._placement_group_no_list

    @placement_group_no_list.setter
    def placement_group_no_list(self, placement_group_no_list):
        """Sets the placement_group_no_list of this GetServerInstanceListRequest.

        물리배치그룹번호리스트  # noqa: E501

        :param placement_group_no_list: The placement_group_no_list of this GetServerInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._placement_group_no_list = placement_group_no_list

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
        if not isinstance(other, GetServerInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
