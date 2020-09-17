# coding: utf-8

"""
    vpc

    OpenAPI spec version: 2020-09-17T10:29:55Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.route import Route  # noqa: F401,E501


class GetRouteListResponse(object):
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
        'total_rows': 'int',
        'route_list': 'list[Route]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'return_code': 'returnCode',
        'return_message': 'returnMessage',
        'total_rows': 'totalRows',
        'route_list': 'routeList'
    }

    def __init__(self, request_id=None, return_code=None, return_message=None, total_rows=None, route_list=None):  # noqa: E501
        """GetRouteListResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._return_code = None
        self._return_message = None
        self._total_rows = None
        self._route_list = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if return_code is not None:
            self.return_code = return_code
        if return_message is not None:
            self.return_message = return_message
        if total_rows is not None:
            self.total_rows = total_rows
        if route_list is not None:
            self.route_list = route_list

    @property
    def request_id(self):
        """Gets the request_id of this GetRouteListResponse.  # noqa: E501


        :return: The request_id of this GetRouteListResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GetRouteListResponse.


        :param request_id: The request_id of this GetRouteListResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def return_code(self):
        """Gets the return_code of this GetRouteListResponse.  # noqa: E501


        :return: The return_code of this GetRouteListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this GetRouteListResponse.


        :param return_code: The return_code of this GetRouteListResponse.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this GetRouteListResponse.  # noqa: E501


        :return: The return_message of this GetRouteListResponse.  # noqa: E501
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this GetRouteListResponse.


        :param return_message: The return_message of this GetRouteListResponse.  # noqa: E501
        :type: str
        """

        self._return_message = return_message

    @property
    def total_rows(self):
        """Gets the total_rows of this GetRouteListResponse.  # noqa: E501


        :return: The total_rows of this GetRouteListResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this GetRouteListResponse.


        :param total_rows: The total_rows of this GetRouteListResponse.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def route_list(self):
        """Gets the route_list of this GetRouteListResponse.  # noqa: E501


        :return: The route_list of this GetRouteListResponse.  # noqa: E501
        :rtype: list[Route]
        """
        return self._route_list

    @route_list.setter
    def route_list(self, route_list):
        """Sets the route_list of this GetRouteListResponse.


        :param route_list: The route_list of this GetRouteListResponse.  # noqa: E501
        :type: list[Route]
        """

        self._route_list = route_list

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
        if not isinstance(other, GetRouteListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
