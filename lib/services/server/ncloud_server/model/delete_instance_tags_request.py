# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-10-17T10:28:43Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_server.model.instance_tag_parameter import InstanceTagParameter  # noqa: F401,E501


class DeleteInstanceTagsRequest(object):
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
        'instance_tag_list': 'list[InstanceTagParameter]'
    }

    attribute_map = {
        'instance_no_list': 'instanceNoList',
        'instance_tag_list': 'instanceTagList'
    }

    def __init__(self, instance_no_list=None, instance_tag_list=None):  # noqa: E501
        """DeleteInstanceTagsRequest - a model defined in Swagger"""  # noqa: E501

        self._instance_no_list = None
        self._instance_tag_list = None
        self.discriminator = None

        self.instance_no_list = instance_no_list
        if instance_tag_list is not None:
            self.instance_tag_list = instance_tag_list

    @property
    def instance_no_list(self):
        """Gets the instance_no_list of this DeleteInstanceTagsRequest.  # noqa: E501

        인스턴스번호리스트  # noqa: E501

        :return: The instance_no_list of this DeleteInstanceTagsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_no_list

    @instance_no_list.setter
    def instance_no_list(self, instance_no_list):
        """Sets the instance_no_list of this DeleteInstanceTagsRequest.

        인스턴스번호리스트  # noqa: E501

        :param instance_no_list: The instance_no_list of this DeleteInstanceTagsRequest.  # noqa: E501
        :type: list[str]
        """
        if instance_no_list is None:
            raise ValueError("Invalid value for `instance_no_list`, must not be `None`")  # noqa: E501

        self._instance_no_list = instance_no_list

    @property
    def instance_tag_list(self):
        """Gets the instance_tag_list of this DeleteInstanceTagsRequest.  # noqa: E501

        인스턴스태그리스트  # noqa: E501

        :return: The instance_tag_list of this DeleteInstanceTagsRequest.  # noqa: E501
        :rtype: list[InstanceTagParameter]
        """
        return self._instance_tag_list

    @instance_tag_list.setter
    def instance_tag_list(self, instance_tag_list):
        """Sets the instance_tag_list of this DeleteInstanceTagsRequest.

        인스턴스태그리스트  # noqa: E501

        :param instance_tag_list: The instance_tag_list of this DeleteInstanceTagsRequest.  # noqa: E501
        :type: list[InstanceTagParameter]
        """

        self._instance_tag_list = instance_tag_list

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
        if not isinstance(other, DeleteInstanceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
