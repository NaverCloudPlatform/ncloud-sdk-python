# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateVpcRequest(object):
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
        'ipv4_cidr_block': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'ipv4_cidr_block': 'ipv4CidrBlock',
        'vpc_name': 'vpcName'
    }

    def __init__(self, region_code=None, ipv4_cidr_block=None, vpc_name=None):  # noqa: E501
        """CreateVpcRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._ipv4_cidr_block = None
        self._vpc_name = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.ipv4_cidr_block = ipv4_cidr_block
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def region_code(self):
        """Gets the region_code of this CreateVpcRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateVpcRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateVpcRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def ipv4_cidr_block(self):
        """Gets the ipv4_cidr_block of this CreateVpcRequest.  # noqa: E501

        IPv4 CIDR블록  # noqa: E501

        :return: The ipv4_cidr_block of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_cidr_block

    @ipv4_cidr_block.setter
    def ipv4_cidr_block(self, ipv4_cidr_block):
        """Sets the ipv4_cidr_block of this CreateVpcRequest.

        IPv4 CIDR블록  # noqa: E501

        :param ipv4_cidr_block: The ipv4_cidr_block of this CreateVpcRequest.  # noqa: E501
        :type: str
        """
        if ipv4_cidr_block is None:
            raise ValueError("Invalid value for `ipv4_cidr_block`, must not be `None`")  # noqa: E501

        self._ipv4_cidr_block = ipv4_cidr_block

    @property
    def vpc_name(self):
        """Gets the vpc_name of this CreateVpcRequest.  # noqa: E501

        VPC이름  # noqa: E501

        :return: The vpc_name of this CreateVpcRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this CreateVpcRequest.

        VPC이름  # noqa: E501

        :param vpc_name: The vpc_name of this CreateVpcRequest.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

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
        if not isinstance(other, CreateVpcRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other