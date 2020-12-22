# coding: utf-8

"""
    vserver

    
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
        'region_code': 'str',
        'access_control_group_no_list': 'list[str]',
        'access_control_group_name': 'str',
        'access_control_group_status_code': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'vpc_no': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'access_control_group_no_list': 'accessControlGroupNoList',
        'access_control_group_name': 'accessControlGroupName',
        'access_control_group_status_code': 'accessControlGroupStatusCode',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'vpc_no': 'vpcNo'
    }

    def __init__(self, region_code=None, access_control_group_no_list=None, access_control_group_name=None, access_control_group_status_code=None, page_no=None, page_size=None, vpc_no=None):  # noqa: E501
        """GetAccessControlGroupListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._access_control_group_no_list = None
        self._access_control_group_name = None
        self._access_control_group_status_code = None
        self._page_no = None
        self._page_size = None
        self._vpc_no = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if access_control_group_no_list is not None:
            self.access_control_group_no_list = access_control_group_no_list
        if access_control_group_name is not None:
            self.access_control_group_name = access_control_group_name
        if access_control_group_status_code is not None:
            self.access_control_group_status_code = access_control_group_status_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if vpc_no is not None:
            self.vpc_no = vpc_no

    @property
    def region_code(self):
        """Gets the region_code of this GetAccessControlGroupListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetAccessControlGroupListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def access_control_group_no_list(self):
        """Gets the access_control_group_no_list of this GetAccessControlGroupListRequest.  # noqa: E501

        ACG번호리스트  # noqa: E501

        :return: The access_control_group_no_list of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_control_group_no_list

    @access_control_group_no_list.setter
    def access_control_group_no_list(self, access_control_group_no_list):
        """Sets the access_control_group_no_list of this GetAccessControlGroupListRequest.

        ACG번호리스트  # noqa: E501

        :param access_control_group_no_list: The access_control_group_no_list of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: list[str]
        """

        self._access_control_group_no_list = access_control_group_no_list

    @property
    def access_control_group_name(self):
        """Gets the access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501

        ACG이름  # noqa: E501

        :return: The access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_name

    @access_control_group_name.setter
    def access_control_group_name(self, access_control_group_name):
        """Sets the access_control_group_name of this GetAccessControlGroupListRequest.

        ACG이름  # noqa: E501

        :param access_control_group_name: The access_control_group_name of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: str
        """

        self._access_control_group_name = access_control_group_name

    @property
    def access_control_group_status_code(self):
        """Gets the access_control_group_status_code of this GetAccessControlGroupListRequest.  # noqa: E501

        ACG상태코드  # noqa: E501

        :return: The access_control_group_status_code of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_control_group_status_code

    @access_control_group_status_code.setter
    def access_control_group_status_code(self, access_control_group_status_code):
        """Sets the access_control_group_status_code of this GetAccessControlGroupListRequest.

        ACG상태코드  # noqa: E501

        :param access_control_group_status_code: The access_control_group_status_code of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: str
        """

        self._access_control_group_status_code = access_control_group_status_code

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

    @property
    def vpc_no(self):
        """Gets the vpc_no of this GetAccessControlGroupListRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this GetAccessControlGroupListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this GetAccessControlGroupListRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this GetAccessControlGroupListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_no = vpc_no

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
