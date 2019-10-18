# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-01-25T05:09:58Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetRootPasswordRequest(object):
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
        'private_key': 'str',
        'server_instance_no': 'str'
    }

    attribute_map = {
        'private_key': 'privateKey',
        'server_instance_no': 'serverInstanceNo'
    }

    def __init__(self, private_key=None, server_instance_no=None):  # noqa: E501
        """GetRootPasswordRequest - a model defined in Swagger"""  # noqa: E501

        self._private_key = None
        self._server_instance_no = None
        self.discriminator = None

        if private_key is not None:
            self.private_key = private_key
        self.server_instance_no = server_instance_no

    @property
    def private_key(self):
        """Gets the private_key of this GetRootPasswordRequest.  # noqa: E501

        개인키  # noqa: E501

        :return: The private_key of this GetRootPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this GetRootPasswordRequest.

        개인키  # noqa: E501

        :param private_key: The private_key of this GetRootPasswordRequest.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this GetRootPasswordRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this GetRootPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this GetRootPasswordRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this GetRootPasswordRequest.  # noqa: E501
        :type: str
        """
        if server_instance_no is None:
            raise ValueError("Invalid value for `server_instance_no`, must not be `None`")  # noqa: E501

        self._server_instance_no = server_instance_no

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
        if not isinstance(other, GetRootPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
