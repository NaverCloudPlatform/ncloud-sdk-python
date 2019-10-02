# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-01-25T05:09:58Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetAccessControlGroupListRequest(object):
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
        'access_control_group_configuration_no_list': 'list[str]',
        'is_default': 'bool',
        'access_control_group_name': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'access_control_group_configuration_no_list': 'accessControlGroupConfigurationNoList',
        'is_default': 'isDefault',
        'access_control_group_name': 'accessControlGroupName',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, access_control_group_configuration_no_list=None, is_default=None, access_control_group_name=None, page_no=None, page_size=None):  # noqa: E501
        """GetAccessControlGroupListRequest - a model defined in Swagger"""  # noqa: E501

        self._access_control_group_configuration_no_list = None
        self._is_default = None
        self._access_control_group_name = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if access_control_group_configuration_no_list is not None:
            self.access_control_group_configuration_no_list = access_control_group_configuration_no_list
        if is_default is not None:
            self.is_default = is_default
        if access_control_group_name is not None:
            self.access_control_group_name = access_control_group_name
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def access_control_group_configuration_no_list(self):
        """Gets the access_control_group_configuration_no_list of this GetAccessControlGroupListRequest.  # noqa: E501

        접근제어그룹설정번호리스트  # noqa: E501

        :return: The access_control_group_configuration_no_list of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_control_group_configuration_no_list

    @access_control_group_configuration_no_list.setter
    def access_control_group_configuration_no_list(self, access_control_group_configuration_no_list):
        """Sets the access_control_group_configuration_no_list of this GetAccessControlGroupListRequest.

        접근제어그룹설정번호리스트  # noqa: E501

        :param access_control_group_configuration_no_list: The access_control_group_configuration_no_list of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: list[str]
        """

        self._access_control_group_configuration_no_list = access_control_group_configuration_no_list

    @property
    def is_default(self):
        """Gets the is_default of this GetAccessControlGroupListRequest.  # noqa: E501

        디폴트여부  # noqa: E501

        :return: The is_default of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this GetAccessControlGroupListRequest.

        디폴트여부  # noqa: E501

        :param is_default: The is_default of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def access_control_group_name(self):
        """Gets the access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501

        접근제어그룹명  # noqa: E501

        :return: The access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_name

    @access_control_group_name.setter
    def access_control_group_name(self, access_control_group_name):
        """Sets the access_control_group_name of this GetAccessControlGroupListRequest.

        접근제어그룹명  # noqa: E501

        :param access_control_group_name: The access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: str
        """

        self._access_control_group_name = access_control_group_name

    @property
    def page_no(self):
        """Gets the page_no of this GetAccessControlGroupListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetAccessControlGroupListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetAccessControlGroupListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetAccessControlGroupListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetAccessControlGroupListRequest.  # noqa: E501
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
        if not isinstance(other, GetAccessControlGroupListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
