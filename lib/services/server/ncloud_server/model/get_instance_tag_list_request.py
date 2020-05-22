# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-10-17T10:28:43Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetInstanceTagListRequest(object):
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
        'instance_no_list': 'list[str]',
        'tag_key_list': 'list[str]',
        'tag_value_list': 'list[str]',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'instance_no_list': 'instanceNoList',
        'tag_key_list': 'tagKeyList',
        'tag_value_list': 'tagValueList',
        'page_no': 'pageNo',
        'page_size': 'pageSize'
    }

    def __init__(self, instance_no_list=None, tag_key_list=None, tag_value_list=None, page_no=None, page_size=None):  # noqa: E501
        """GetInstanceTagListRequest - a model defined in Swagger"""  # noqa: E501

        self._instance_no_list = None
        self._tag_key_list = None
        self._tag_value_list = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if instance_no_list is not None:
            self.instance_no_list = instance_no_list
        if tag_key_list is not None:
            self.tag_key_list = tag_key_list
        if tag_value_list is not None:
            self.tag_value_list = tag_value_list
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def instance_no_list(self):
        """Gets the instance_no_list of this GetInstanceTagListRequest.  # noqa: E501

        인스턴스번호리스트  # noqa: E501

        :return: The instance_no_list of this GetInstanceTagListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_no_list

    @instance_no_list.setter
    def instance_no_list(self, instance_no_list):
        """Sets the instance_no_list of this GetInstanceTagListRequest.

        인스턴스번호리스트  # noqa: E501

        :param instance_no_list: The instance_no_list of this GetInstanceTagListRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_no_list = instance_no_list

    @property
    def tag_key_list(self):
        """Gets the tag_key_list of this GetInstanceTagListRequest.  # noqa: E501

        태그키리스트  # noqa: E501

        :return: The tag_key_list of this GetInstanceTagListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_key_list

    @tag_key_list.setter
    def tag_key_list(self, tag_key_list):
        """Sets the tag_key_list of this GetInstanceTagListRequest.

        태그키리스트  # noqa: E501

        :param tag_key_list: The tag_key_list of this GetInstanceTagListRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag_key_list = tag_key_list

    @property
    def tag_value_list(self):
        """Gets the tag_value_list of this GetInstanceTagListRequest.  # noqa: E501

        태그값리스트  # noqa: E501

        :return: The tag_value_list of this GetInstanceTagListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_value_list

    @tag_value_list.setter
    def tag_value_list(self, tag_value_list):
        """Sets the tag_value_list of this GetInstanceTagListRequest.

        태그값리스트  # noqa: E501

        :param tag_value_list: The tag_value_list of this GetInstanceTagListRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag_value_list = tag_value_list

    @property
    def page_no(self):
        """Gets the page_no of this GetInstanceTagListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetInstanceTagListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetInstanceTagListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetInstanceTagListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetInstanceTagListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetInstanceTagListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetInstanceTagListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetInstanceTagListRequest.  # noqa: E501
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
        if not isinstance(other, GetInstanceTagListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other