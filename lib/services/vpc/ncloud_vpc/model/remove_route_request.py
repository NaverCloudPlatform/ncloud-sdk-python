# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.route_parameter import RouteParameter  # noqa: F401,E501


class RemoveRouteRequest(object):
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
        'route_list': 'list[RouteParameter]',
        'route_table_no': 'str',
        'vpc_no': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'route_list': 'routeList',
        'route_table_no': 'routeTableNo',
        'vpc_no': 'vpcNo'
    }

    def __init__(self, region_code=None, route_list=None, route_table_no=None, vpc_no=None):  # noqa: E501
        """RemoveRouteRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._route_list = None
        self._route_table_no = None
        self._vpc_no = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.route_list = route_list
        self.route_table_no = route_table_no
        self.vpc_no = vpc_no

    @property
    def region_code(self):
        """Gets the region_code of this RemoveRouteRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this RemoveRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this RemoveRouteRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this RemoveRouteRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def route_list(self):
        """Gets the route_list of this RemoveRouteRequest.  # noqa: E501

        라우트리스트  # noqa: E501

        :return: The route_list of this RemoveRouteRequest.  # noqa: E501
        :rtype: list[RouteParameter]
        """
        return self._route_list

    @route_list.setter
    def route_list(self, route_list):
        """Sets the route_list of this RemoveRouteRequest.

        라우트리스트  # noqa: E501

        :param route_list: The route_list of this RemoveRouteRequest.  # noqa: E501
        :type: list[RouteParameter]
        """
        if route_list is None:
            raise ValueError("Invalid value for `route_list`, must not be `None`")  # noqa: E501

        self._route_list = route_list

    @property
    def route_table_no(self):
        """Gets the route_table_no of this RemoveRouteRequest.  # noqa: E501

        라우트테이블번호  # noqa: E501

        :return: The route_table_no of this RemoveRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_table_no

    @route_table_no.setter
    def route_table_no(self, route_table_no):
        """Sets the route_table_no of this RemoveRouteRequest.

        라우트테이블번호  # noqa: E501

        :param route_table_no: The route_table_no of this RemoveRouteRequest.  # noqa: E501
        :type: str
        """
        if route_table_no is None:
            raise ValueError("Invalid value for `route_table_no`, must not be `None`")  # noqa: E501

        self._route_table_no = route_table_no

    @property
    def vpc_no(self):
        """Gets the vpc_no of this RemoveRouteRequest.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this RemoveRouteRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this RemoveRouteRequest.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this RemoveRouteRequest.  # noqa: E501
        :type: str
        """
        if vpc_no is None:
            raise ValueError("Invalid value for `vpc_no`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, RemoveRouteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
