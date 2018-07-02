# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-07-02T07:25:18Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetBlockStorageInstanceListRequest(object):
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
        'server_instance_no': 'str',
        'block_storage_instance_no_list': 'list[str]',
        'search_filter_name': 'str',
        'search_filter_value': 'str',
        'block_storage_type_code_list': 'list[str]',
        'page_no': 'int',
        'page_size': 'int',
        'block_storage_instance_status_code': 'str',
        'disk_type_code': 'str',
        'disk_detail_type_code': 'str',
        'region_no': 'str',
        'zone_no': 'str',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'server_instance_no': 'serverInstanceNo',
        'block_storage_instance_no_list': 'blockStorageInstanceNoList',
        'search_filter_name': 'searchFilterName',
        'search_filter_value': 'searchFilterValue',
        'block_storage_type_code_list': 'blockStorageTypeCodeList',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'block_storage_instance_status_code': 'blockStorageInstanceStatusCode',
        'disk_type_code': 'diskTypeCode',
        'disk_detail_type_code': 'diskDetailTypeCode',
        'region_no': 'regionNo',
        'zone_no': 'zoneNo',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, server_instance_no=None, block_storage_instance_no_list=None, search_filter_name=None, search_filter_value=None, block_storage_type_code_list=None, page_no=None, page_size=None, block_storage_instance_status_code=None, disk_type_code=None, disk_detail_type_code=None, region_no=None, zone_no=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetBlockStorageInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._server_instance_no = None
        self._block_storage_instance_no_list = None
        self._search_filter_name = None
        self._search_filter_value = None
        self._block_storage_type_code_list = None
        self._page_no = None
        self._page_size = None
        self._block_storage_instance_status_code = None
        self._disk_type_code = None
        self._disk_detail_type_code = None
        self._region_no = None
        self._zone_no = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if server_instance_no is not None:
            self.server_instance_no = server_instance_no
        if block_storage_instance_no_list is not None:
            self.block_storage_instance_no_list = block_storage_instance_no_list
        if search_filter_name is not None:
            self.search_filter_name = search_filter_name
        if search_filter_value is not None:
            self.search_filter_value = search_filter_value
        if block_storage_type_code_list is not None:
            self.block_storage_type_code_list = block_storage_type_code_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if block_storage_instance_status_code is not None:
            self.block_storage_instance_status_code = block_storage_instance_status_code
        if disk_type_code is not None:
            self.disk_type_code = disk_type_code
        if disk_detail_type_code is not None:
            self.disk_detail_type_code = disk_detail_type_code
        if region_no is not None:
            self.region_no = region_no
        if zone_no is not None:
            self.zone_no = zone_no
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this GetBlockStorageInstanceListRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this GetBlockStorageInstanceListRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._server_instance_no = server_instance_no

    @property
    def block_storage_instance_no_list(self):
        """Gets the block_storage_instance_no_list of this GetBlockStorageInstanceListRequest.  # noqa: E501

        블록스토리지인스턴스번호리스트  # noqa: E501

        :return: The block_storage_instance_no_list of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._block_storage_instance_no_list

    @block_storage_instance_no_list.setter
    def block_storage_instance_no_list(self, block_storage_instance_no_list):
        """Sets the block_storage_instance_no_list of this GetBlockStorageInstanceListRequest.

        블록스토리지인스턴스번호리스트  # noqa: E501

        :param block_storage_instance_no_list: The block_storage_instance_no_list of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._block_storage_instance_no_list = block_storage_instance_no_list

    @property
    def search_filter_name(self):
        """Gets the search_filter_name of this GetBlockStorageInstanceListRequest.  # noqa: E501

        검색할필터명  # noqa: E501

        :return: The search_filter_name of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_filter_name

    @search_filter_name.setter
    def search_filter_name(self, search_filter_name):
        """Sets the search_filter_name of this GetBlockStorageInstanceListRequest.

        검색할필터명  # noqa: E501

        :param search_filter_name: The search_filter_name of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._search_filter_name = search_filter_name

    @property
    def search_filter_value(self):
        """Gets the search_filter_value of this GetBlockStorageInstanceListRequest.  # noqa: E501

        검색할필터값  # noqa: E501

        :return: The search_filter_value of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_filter_value

    @search_filter_value.setter
    def search_filter_value(self, search_filter_value):
        """Sets the search_filter_value of this GetBlockStorageInstanceListRequest.

        검색할필터값  # noqa: E501

        :param search_filter_value: The search_filter_value of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._search_filter_value = search_filter_value

    @property
    def block_storage_type_code_list(self):
        """Gets the block_storage_type_code_list of this GetBlockStorageInstanceListRequest.  # noqa: E501

        블록스토리지구분코드리스트  # noqa: E501

        :return: The block_storage_type_code_list of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._block_storage_type_code_list

    @block_storage_type_code_list.setter
    def block_storage_type_code_list(self, block_storage_type_code_list):
        """Sets the block_storage_type_code_list of this GetBlockStorageInstanceListRequest.

        블록스토리지구분코드리스트  # noqa: E501

        :param block_storage_type_code_list: The block_storage_type_code_list of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._block_storage_type_code_list = block_storage_type_code_list

    @property
    def page_no(self):
        """Gets the page_no of this GetBlockStorageInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetBlockStorageInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetBlockStorageInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetBlockStorageInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def block_storage_instance_status_code(self):
        """Gets the block_storage_instance_status_code of this GetBlockStorageInstanceListRequest.  # noqa: E501

        블록스토리지인스턴스상태코드  # noqa: E501

        :return: The block_storage_instance_status_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_instance_status_code

    @block_storage_instance_status_code.setter
    def block_storage_instance_status_code(self, block_storage_instance_status_code):
        """Sets the block_storage_instance_status_code of this GetBlockStorageInstanceListRequest.

        블록스토리지인스턴스상태코드  # noqa: E501

        :param block_storage_instance_status_code: The block_storage_instance_status_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_instance_status_code = block_storage_instance_status_code

    @property
    def disk_type_code(self):
        """Gets the disk_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501

        디스크유형코드  # noqa: E501

        :return: The disk_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._disk_type_code

    @disk_type_code.setter
    def disk_type_code(self, disk_type_code):
        """Sets the disk_type_code of this GetBlockStorageInstanceListRequest.

        디스크유형코드  # noqa: E501

        :param disk_type_code: The disk_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._disk_type_code = disk_type_code

    @property
    def disk_detail_type_code(self):
        """Gets the disk_detail_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501

        디스크유형상세코드  # noqa: E501

        :return: The disk_detail_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._disk_detail_type_code

    @disk_detail_type_code.setter
    def disk_detail_type_code(self, disk_detail_type_code):
        """Sets the disk_detail_type_code of this GetBlockStorageInstanceListRequest.

        디스크유형상세코드  # noqa: E501

        :param disk_detail_type_code: The disk_detail_type_code of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._disk_detail_type_code = disk_detail_type_code

    @property
    def region_no(self):
        """Gets the region_no of this GetBlockStorageInstanceListRequest.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this GetBlockStorageInstanceListRequest.

        리전번호  # noqa: E501

        :param region_no: The region_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

    @property
    def zone_no(self):
        """Gets the zone_no of this GetBlockStorageInstanceListRequest.  # noqa: E501

        ZONE번호  # noqa: E501

        :return: The zone_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_no

    @zone_no.setter
    def zone_no(self, zone_no):
        """Sets the zone_no of this GetBlockStorageInstanceListRequest.

        ZONE번호  # noqa: E501

        :param zone_no: The zone_no of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._zone_no = zone_no

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetBlockStorageInstanceListRequest.  # noqa: E501

        소팅대상  # noqa: E501

        :return: The sorted_by of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetBlockStorageInstanceListRequest.

        소팅대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetBlockStorageInstanceListRequest.  # noqa: E501

        소팅순서  # noqa: E501

        :return: The sorting_order of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetBlockStorageInstanceListRequest.

        소팅순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetBlockStorageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

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
        if not isinstance(other, GetBlockStorageInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
