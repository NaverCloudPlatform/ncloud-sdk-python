# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetMemberServerImageInstanceListRequest(object):
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
        'member_server_image_name': 'str',
        'member_server_image_instance_status_code': 'str',
        'member_server_image_instance_no_list': 'list[str]',
        'platform_type_code_list': 'list[str]',
        'page_no': 'int',
        'page_size': 'int',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'member_server_image_name': 'memberServerImageName',
        'member_server_image_instance_status_code': 'memberServerImageInstanceStatusCode',
        'member_server_image_instance_no_list': 'memberServerImageInstanceNoList',
        'platform_type_code_list': 'platformTypeCodeList',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, region_code=None, member_server_image_name=None, member_server_image_instance_status_code=None, member_server_image_instance_no_list=None, platform_type_code_list=None, page_no=None, page_size=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetMemberServerImageInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._member_server_image_name = None
        self._member_server_image_instance_status_code = None
        self._member_server_image_instance_no_list = None
        self._platform_type_code_list = None
        self._page_no = None
        self._page_size = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if member_server_image_name is not None:
            self.member_server_image_name = member_server_image_name
        if member_server_image_instance_status_code is not None:
            self.member_server_image_instance_status_code = member_server_image_instance_status_code
        if member_server_image_instance_no_list is not None:
            self.member_server_image_instance_no_list = member_server_image_instance_no_list
        if platform_type_code_list is not None:
            self.platform_type_code_list = platform_type_code_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def region_code(self):
        """Gets the region_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetMemberServerImageInstanceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def member_server_image_name(self):
        """Gets the member_server_image_name of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        회원서버이미지이름  # noqa: E501

        :return: The member_server_image_name of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_name

    @member_server_image_name.setter
    def member_server_image_name(self, member_server_image_name):
        """Sets the member_server_image_name of this GetMemberServerImageInstanceListRequest.

        회원서버이미지이름  # noqa: E501

        :param member_server_image_name: The member_server_image_name of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._member_server_image_name = member_server_image_name

    @property
    def member_server_image_instance_status_code(self):
        """Gets the member_server_image_instance_status_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        회원서버이미지인스턴스상태코드  # noqa: E501

        :return: The member_server_image_instance_status_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_instance_status_code

    @member_server_image_instance_status_code.setter
    def member_server_image_instance_status_code(self, member_server_image_instance_status_code):
        """Sets the member_server_image_instance_status_code of this GetMemberServerImageInstanceListRequest.

        회원서버이미지인스턴스상태코드  # noqa: E501

        :param member_server_image_instance_status_code: The member_server_image_instance_status_code of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._member_server_image_instance_status_code = member_server_image_instance_status_code

    @property
    def member_server_image_instance_no_list(self):
        """Gets the member_server_image_instance_no_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        회원서버이미지인스턴스번호리스트  # noqa: E501

        :return: The member_server_image_instance_no_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_server_image_instance_no_list

    @member_server_image_instance_no_list.setter
    def member_server_image_instance_no_list(self, member_server_image_instance_no_list):
        """Sets the member_server_image_instance_no_list of this GetMemberServerImageInstanceListRequest.

        회원서버이미지인스턴스번호리스트  # noqa: E501

        :param member_server_image_instance_no_list: The member_server_image_instance_no_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._member_server_image_instance_no_list = member_server_image_instance_no_list

    @property
    def platform_type_code_list(self):
        """Gets the platform_type_code_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        플랫폼유형코드리스트  # noqa: E501

        :return: The platform_type_code_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._platform_type_code_list

    @platform_type_code_list.setter
    def platform_type_code_list(self, platform_type_code_list):
        """Sets the platform_type_code_list of this GetMemberServerImageInstanceListRequest.

        플랫폼유형코드리스트  # noqa: E501

        :param platform_type_code_list: The platform_type_code_list of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._platform_type_code_list = platform_type_code_list

    @property
    def page_no(self):
        """Gets the page_no of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetMemberServerImageInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetMemberServerImageInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetMemberServerImageInstanceListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetMemberServerImageInstanceListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetMemberServerImageInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetMemberServerImageInstanceListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetMemberServerImageInstanceListRequest.  # noqa: E501
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
        if not isinstance(other, GetMemberServerImageInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other