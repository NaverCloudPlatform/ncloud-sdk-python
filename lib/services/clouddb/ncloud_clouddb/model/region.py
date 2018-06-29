# coding: utf-8

"""
    clouddb

    OpenAPI spec version: 2018-06-21T02:28:05Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Region(object):
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
        'region_no': 'str',
        'region_code': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'region_no': 'regionNo',
        'region_code': 'regionCode',
        'region_name': 'regionName'
    }

    def __init__(self, region_no=None, region_code=None, region_name=None):  # noqa: E501
        """Region - a model defined in Swagger"""  # noqa: E501

        self._region_no = None
        self._region_code = None
        self._region_name = None
        self.discriminator = None

        if region_no is not None:
            self.region_no = region_no
        if region_code is not None:
            self.region_code = region_code
        if region_name is not None:
            self.region_name = region_name

    @property
    def region_no(self):
        """Gets the region_no of this Region.  # noqa: E501


        :return: The region_no of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this Region.


        :param region_no: The region_no of this Region.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

    @property
    def region_code(self):
        """Gets the region_code of this Region.  # noqa: E501


        :return: The region_code of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this Region.


        :param region_code: The region_code of this Region.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def region_name(self):
        """Gets the region_name of this Region.  # noqa: E501


        :return: The region_name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this Region.


        :param region_name: The region_name of this Region.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
