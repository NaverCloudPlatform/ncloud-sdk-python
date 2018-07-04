# coding: utf-8

"""
    server

    OpenAPI spec version: 2018-07-02T09:06:17Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_server.model.product import Product  # noqa: F401,E501


class GetServerProductListResponse(object):
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
        'request_id': 'str',
        'return_code': 'str',
        'return_message': 'str',
        'product_list': 'list[Product]',
        'total_rows': 'int'
    }

    attribute_map = {
        'request_id': 'requestId',
        'return_code': 'returnCode',
        'return_message': 'returnMessage',
        'product_list': 'productList',
        'total_rows': 'totalRows'
    }

    def __init__(self, request_id=None, return_code=None, return_message=None, product_list=None, total_rows=None):  # noqa: E501
        """GetServerProductListResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._return_code = None
        self._return_message = None
        self._product_list = None
        self._total_rows = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if product_list is not None:
            self.product_list = product_list
        if total_rows is not None:
            self.total_rows = total_rows

    @property
    def request_id(self):
        """Gets the request_id of this GetServerProductListResponse.  # noqa: E501


        :return: The request_id of this GetServerProductListResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetServerProductListResponse.


        :param request_id: The request_id of this GetServerProductListResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def return_code(self):
        """Gets the return_code of this GetServerProductListResponse.  # noqa: E501


        :return: The return_code of this GetServerProductListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this GetServerProductListResponse.


        :param return_code: The return_code of this GetServerProductListResponse.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this GetServerProductListResponse.  # noqa: E501


        :return: The return_message of this GetServerProductListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this GetServerProductListResponse.


        :param return_message: The return_message of this GetServerProductListResponse.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def product_list(self):
        """Gets the product_list of this GetServerProductListResponse.  # noqa: E501


        :return: The product_list of this GetServerProductListResponse.  # noqa: E501
        :rtype: list[Product]
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list):
        """Sets the product_list of this GetServerProductListResponse.


        :param product_list: The product_list of this GetServerProductListResponse.  # noqa: E501
        :type: list[Product]
        """

        self._product_list = product_list

    @property
    def total_rows(self):
        """Gets the total_rows of this GetServerProductListResponse.  # noqa: E501


        :return: The total_rows of this GetServerProductListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this GetServerProductListResponse.


        :param total_rows: The total_rows of this GetServerProductListResponse.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

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
        if not isinstance(other, GetServerProductListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
