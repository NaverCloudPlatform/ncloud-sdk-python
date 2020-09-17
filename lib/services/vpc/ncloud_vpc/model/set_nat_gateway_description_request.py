# coding: utf-8

"""
    vpc

    OpenAPI spec version: 2020-09-17T10:29:55Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SetNatGatewayDescriptionRequest(object):
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
        'nat_gateway_instance_no': 'str',
        'nat_gateway_description': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'nat_gateway_instance_no': 'natGatewayInstanceNo',
        'nat_gateway_description': 'natGatewayDescription'
    }

    def __init__(self, region_code=None, nat_gateway_instance_no=None, nat_gateway_description=None):  # noqa: E501
        """SetNatGatewayDescriptionRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._nat_gateway_instance_no = None
        self._nat_gateway_description = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.nat_gateway_instance_no = nat_gateway_instance_no
        if nat_gateway_description is not None:
            self.nat_gateway_description = nat_gateway_description

    @property
    def region_code(self):
        """Gets the region_code of this SetNatGatewayDescriptionRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this SetNatGatewayDescriptionRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def nat_gateway_instance_no(self):
        """Gets the nat_gateway_instance_no of this SetNatGatewayDescriptionRequest.  # noqa: E501

        NATGateway인스턴스번호  # noqa: E501

        :return: The nat_gateway_instance_no of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_instance_no

    @nat_gateway_instance_no.setter
    def nat_gateway_instance_no(self, nat_gateway_instance_no):
        """Sets the nat_gateway_instance_no of this SetNatGatewayDescriptionRequest.

        NATGateway인스턴스번호  # noqa: E501

        :param nat_gateway_instance_no: The nat_gateway_instance_no of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :type: str
        """
        if nat_gateway_instance_no is None:
            raise ValueError("Invalid value for `nat_gateway_instance_no`, must not be `None`")  # noqa: E501

        self._nat_gateway_instance_no = nat_gateway_instance_no

    @property
    def nat_gateway_description(self):
        """Gets the nat_gateway_description of this SetNatGatewayDescriptionRequest.  # noqa: E501

        NATGateway설명  # noqa: E501

        :return: The nat_gateway_description of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_description

    @nat_gateway_description.setter
    def nat_gateway_description(self, nat_gateway_description):
        """Sets the nat_gateway_description of this SetNatGatewayDescriptionRequest.

        NATGateway설명  # noqa: E501

        :param nat_gateway_description: The nat_gateway_description of this SetNatGatewayDescriptionRequest.  # noqa: E501
        :type: str
        """

        self._nat_gateway_description = nat_gateway_description

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
        if not isinstance(other, SetNatGatewayDescriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
