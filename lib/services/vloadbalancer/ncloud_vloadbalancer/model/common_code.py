# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CommonCode(object):
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
        'code': 'str',
        'code_name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'code_name': 'codeName'
    }

    def __init__(self, code=None, code_name=None):  # noqa: E501
        """CommonCode - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._code_name = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if code_name is not None:
            self.code_name = code_name

    @property
    def code(self):
        """Gets the code of this CommonCode.  # noqa: E501

        코드  # noqa: E501

        :return: The code of this CommonCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CommonCode.

        코드  # noqa: E501

        :param code: The code of this CommonCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def code_name(self):
        """Gets the code_name of this CommonCode.  # noqa: E501

        코드명  # noqa: E501

        :return: The code_name of this CommonCode.  # noqa: E501
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        """Sets the code_name of this CommonCode.

        코드명  # noqa: E501

        :param code_name: The code_name of this CommonCode.  # noqa: E501
        :type: str
        """

        self._code_name = code_name

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
        if not isinstance(other, CommonCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
