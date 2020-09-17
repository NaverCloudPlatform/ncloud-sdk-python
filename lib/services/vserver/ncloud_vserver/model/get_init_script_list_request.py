# coding: utf-8

"""
    vserver

    OpenAPI spec version: 2020-09-17T02:28:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetInitScriptListRequest(object):
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
        'os_type_code': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'sorted_by': 'str',
        'sorting_order': 'str',
        'init_script_name': 'str',
        'init_script_no_list': 'list[str]'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'os_type_code': 'osTypeCode',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder',
        'init_script_name': 'initScriptName',
        'init_script_no_list': 'initScriptNoList'
    }

    def __init__(self, region_code=None, os_type_code=None, page_no=None, page_size=None, sorted_by=None, sorting_order=None, init_script_name=None, init_script_no_list=None):  # noqa: E501
        """GetInitScriptListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._os_type_code = None
        self._page_no = None
        self._page_size = None
        self._sorted_by = None
        self._sorting_order = None
        self._init_script_name = None
        self._init_script_no_list = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if os_type_code is not None:
            self.os_type_code = os_type_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order
        if init_script_name is not None:
            self.init_script_name = init_script_name
        if init_script_no_list is not None:
            self.init_script_no_list = init_script_no_list

    @property
    def region_code(self):
        """Gets the region_code of this GetInitScriptListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetInitScriptListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetInitScriptListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetInitScriptListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def os_type_code(self):
        """Gets the os_type_code of this GetInitScriptListRequest.  # noqa: E501

        OS유형코드  # noqa: E501

        :return: The os_type_code of this GetInitScriptListRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_type_code

    @os_type_code.setter
    def os_type_code(self, os_type_code):
        """Sets the os_type_code of this GetInitScriptListRequest.

        OS유형코드  # noqa: E501

        :param os_type_code: The os_type_code of this GetInitScriptListRequest.  # noqa: E501
        :type: str
        """

        self._os_type_code = os_type_code

    @property
    def page_no(self):
        """Gets the page_no of this GetInitScriptListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetInitScriptListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetInitScriptListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetInitScriptListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetInitScriptListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetInitScriptListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetInitScriptListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetInitScriptListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetInitScriptListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetInitScriptListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetInitScriptListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetInitScriptListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetInitScriptListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetInitScriptListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetInitScriptListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetInitScriptListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

    @property
    def init_script_name(self):
        """Gets the init_script_name of this GetInitScriptListRequest.  # noqa: E501

        초기화스크립트이름  # noqa: E501

        :return: The init_script_name of this GetInitScriptListRequest.  # noqa: E501
        :rtype: str
        """
        return self._init_script_name

    @init_script_name.setter
    def init_script_name(self, init_script_name):
        """Sets the init_script_name of this GetInitScriptListRequest.

        초기화스크립트이름  # noqa: E501

        :param init_script_name: The init_script_name of this GetInitScriptListRequest.  # noqa: E501
        :type: str
        """

        self._init_script_name = init_script_name

    @property
    def init_script_no_list(self):
        """Gets the init_script_no_list of this GetInitScriptListRequest.  # noqa: E501

        초기화스크립트번호리스트  # noqa: E501

        :return: The init_script_no_list of this GetInitScriptListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._init_script_no_list

    @init_script_no_list.setter
    def init_script_no_list(self, init_script_no_list):
        """Sets the init_script_no_list of this GetInitScriptListRequest.

        초기화스크립트번호리스트  # noqa: E501

        :param init_script_no_list: The init_script_no_list of this GetInitScriptListRequest.  # noqa: E501
        :type: list[str]
        """

        self._init_script_no_list = init_script_no_list

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
        if not isinstance(other, GetInitScriptListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
