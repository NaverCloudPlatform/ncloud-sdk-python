# coding: utf-8

"""
    server

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StartServerInstancesRequest(object):
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
        'server_instance_no_list': 'list[str]'
    }

    attribute_map = {
        'server_instance_no_list': 'serverInstanceNoList'
    }

    def __init__(self, server_instance_no_list=None):  # noqa: E501
        """StartServerInstancesRequest - a model defined in Swagger"""  # noqa: E501

        self._server_instance_no_list = None
        self.discriminator = None

        self.server_instance_no_list = server_instance_no_list

    @property
    def server_instance_no_list(self):
        """Gets the server_instance_no_list of this StartServerInstancesRequest.  # noqa: E501

        서버인스턴스번호리스트  # noqa: E501

        :return: The server_instance_no_list of this StartServerInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_instance_no_list

    @server_instance_no_list.setter
    def server_instance_no_list(self, server_instance_no_list):
        """Sets the server_instance_no_list of this StartServerInstancesRequest.

        서버인스턴스번호리스트  # noqa: E501

        :param server_instance_no_list: The server_instance_no_list of this StartServerInstancesRequest.  # noqa: E501
        :type: list[str]
        """
        if server_instance_no_list is None:
            raise ValueError("Invalid value for `server_instance_no_list`, must not be `None`")  # noqa: E501

        self._server_instance_no_list = server_instance_no_list

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
        if not isinstance(other, StartServerInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
