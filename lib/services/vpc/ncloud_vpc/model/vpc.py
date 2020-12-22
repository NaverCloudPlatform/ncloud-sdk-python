# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.common_code import CommonCode  # noqa: F401,E501


class Vpc(object):
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
        'vpc_no': 'str',
        'vpc_name': 'str',
        'ipv4_cidr_block': 'str',
        'vpc_status': 'CommonCode',
        'region_code': 'str',
        'create_date': 'str'
    }

    attribute_map = {
        'vpc_no': 'vpcNo',
        'vpc_name': 'vpcName',
        'ipv4_cidr_block': 'ipv4CidrBlock',
        'vpc_status': 'vpcStatus',
        'region_code': 'regionCode',
        'create_date': 'createDate'
    }

    def __init__(self, vpc_no=None, vpc_name=None, ipv4_cidr_block=None, vpc_status=None, region_code=None, create_date=None):  # noqa: E501
        """Vpc - a model defined in Swagger"""  # noqa: E501

        self._vpc_no = None
        self._vpc_name = None
        self._ipv4_cidr_block = None
        self._vpc_status = None
        self._region_code = None
        self._create_date = None
        self.discriminator = None

        if vpc_no is not None:
            self.vpc_no = vpc_no
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if ipv4_cidr_block is not None:
            self.ipv4_cidr_block = ipv4_cidr_block
        if vpc_status is not None:
            self.vpc_status = vpc_status
        if region_code is not None:
            self.region_code = region_code
        if create_date is not None:
            self.create_date = create_date

    @property
    def vpc_no(self):
        """Gets the vpc_no of this Vpc.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this Vpc.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this Vpc.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this Vpc.  # noqa: E501
        :type: str
        """

        self._vpc_no = vpc_no

    @property
    def vpc_name(self):
        """Gets the vpc_name of this Vpc.  # noqa: E501

        VPC이름  # noqa: E501

        :return: The vpc_name of this Vpc.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this Vpc.

        VPC이름  # noqa: E501

        :param vpc_name: The vpc_name of this Vpc.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

    @property
    def ipv4_cidr_block(self):
        """Gets the ipv4_cidr_block of this Vpc.  # noqa: E501

        IPv4 CIDR블록  # noqa: E501

        :return: The ipv4_cidr_block of this Vpc.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_cidr_block

    @ipv4_cidr_block.setter
    def ipv4_cidr_block(self, ipv4_cidr_block):
        """Sets the ipv4_cidr_block of this Vpc.

        IPv4 CIDR블록  # noqa: E501

        :param ipv4_cidr_block: The ipv4_cidr_block of this Vpc.  # noqa: E501
        :type: str
        """

        self._ipv4_cidr_block = ipv4_cidr_block

    @property
    def vpc_status(self):
        """Gets the vpc_status of this Vpc.  # noqa: E501

        VPC상태  # noqa: E501

        :return: The vpc_status of this Vpc.  # noqa: E501
        :rtype: CommonCode
        """
        return self._vpc_status

    @vpc_status.setter
    def vpc_status(self, vpc_status):
        """Sets the vpc_status of this Vpc.

        VPC상태  # noqa: E501

        :param vpc_status: The vpc_status of this Vpc.  # noqa: E501
        :type: CommonCode
        """

        self._vpc_status = vpc_status

    @property
    def region_code(self):
        """Gets the region_code of this Vpc.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this Vpc.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this Vpc.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this Vpc.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def create_date(self):
        """Gets the create_date of this Vpc.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this Vpc.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Vpc.

        생성일시  # noqa: E501

        :param create_date: The create_date of this Vpc.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other