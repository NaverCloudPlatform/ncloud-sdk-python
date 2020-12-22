# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.common_code import CommonCode  # noqa: F401,E501


class NatGatewayInstance(object):
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
        'nat_gateway_instance_no': 'str',
        'nat_gateway_name': 'str',
        'public_ip': 'str',
        'nat_gateway_instance_status': 'CommonCode',
        'nat_gateway_instance_status_name': 'str',
        'nat_gateway_instance_operation': 'CommonCode',
        'create_date': 'str',
        'nat_gateway_description': 'str',
        'zone_code': 'str'
    }

    attribute_map = {
        'vpc_no': 'vpcNo',
        'vpc_name': 'vpcName',
        'nat_gateway_instance_no': 'natGatewayInstanceNo',
        'nat_gateway_name': 'natGatewayName',
        'public_ip': 'publicIp',
        'nat_gateway_instance_status': 'natGatewayInstanceStatus',
        'nat_gateway_instance_status_name': 'natGatewayInstanceStatusName',
        'nat_gateway_instance_operation': 'natGatewayInstanceOperation',
        'create_date': 'createDate',
        'nat_gateway_description': 'natGatewayDescription',
        'zone_code': 'zoneCode'
    }

    def __init__(self, vpc_no=None, vpc_name=None, nat_gateway_instance_no=None, nat_gateway_name=None, public_ip=None, nat_gateway_instance_status=None, nat_gateway_instance_status_name=None, nat_gateway_instance_operation=None, create_date=None, nat_gateway_description=None, zone_code=None):  # noqa: E501
        """NatGatewayInstance - a model defined in Swagger"""  # noqa: E501

        self._vpc_no = None
        self._vpc_name = None
        self._nat_gateway_instance_no = None
        self._nat_gateway_name = None
        self._public_ip = None
        self._nat_gateway_instance_status = None
        self._nat_gateway_instance_status_name = None
        self._nat_gateway_instance_operation = None
        self._create_date = None
        self._nat_gateway_description = None
        self._zone_code = None
        self.discriminator = None

        if vpc_no is not None:
            self.vpc_no = vpc_no
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if nat_gateway_instance_no is not None:
            self.nat_gateway_instance_no = nat_gateway_instance_no
        if nat_gateway_name is not None:
            self.nat_gateway_name = nat_gateway_name
        if public_ip is not None:
            self.public_ip = public_ip
        if nat_gateway_instance_status is not None:
            self.nat_gateway_instance_status = nat_gateway_instance_status
        if nat_gateway_instance_status_name is not None:
            self.nat_gateway_instance_status_name = nat_gateway_instance_status_name
        if nat_gateway_instance_operation is not None:
            self.nat_gateway_instance_operation = nat_gateway_instance_operation
        if create_date is not None:
            self.create_date = create_date
        if nat_gateway_description is not None:
            self.nat_gateway_description = nat_gateway_description
        if zone_code is not None:
            self.zone_code = zone_code

    @property
    def vpc_no(self):
        """Gets the vpc_no of this NatGatewayInstance.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this NatGatewayInstance.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._vpc_no = vpc_no

    @property
    def vpc_name(self):
        """Gets the vpc_name of this NatGatewayInstance.  # noqa: E501

        VPC이름  # noqa: E501

        :return: The vpc_name of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this NatGatewayInstance.

        VPC이름  # noqa: E501

        :param vpc_name: The vpc_name of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

    @property
    def nat_gateway_instance_no(self):
        """Gets the nat_gateway_instance_no of this NatGatewayInstance.  # noqa: E501

        NATGateway인스턴스번호  # noqa: E501

        :return: The nat_gateway_instance_no of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_instance_no

    @nat_gateway_instance_no.setter
    def nat_gateway_instance_no(self, nat_gateway_instance_no):
        """Sets the nat_gateway_instance_no of this NatGatewayInstance.

        NATGateway인스턴스번호  # noqa: E501

        :param nat_gateway_instance_no: The nat_gateway_instance_no of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._nat_gateway_instance_no = nat_gateway_instance_no

    @property
    def nat_gateway_name(self):
        """Gets the nat_gateway_name of this NatGatewayInstance.  # noqa: E501

        NATGateway이름  # noqa: E501

        :return: The nat_gateway_name of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_name

    @nat_gateway_name.setter
    def nat_gateway_name(self, nat_gateway_name):
        """Sets the nat_gateway_name of this NatGatewayInstance.

        NATGateway이름  # noqa: E501

        :param nat_gateway_name: The nat_gateway_name of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._nat_gateway_name = nat_gateway_name

    @property
    def public_ip(self):
        """Gets the public_ip of this NatGatewayInstance.  # noqa: E501

        공인IP주소  # noqa: E501

        :return: The public_ip of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this NatGatewayInstance.

        공인IP주소  # noqa: E501

        :param public_ip: The public_ip of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def nat_gateway_instance_status(self):
        """Gets the nat_gateway_instance_status of this NatGatewayInstance.  # noqa: E501

        NATGateway인스턴스상태  # noqa: E501

        :return: The nat_gateway_instance_status of this NatGatewayInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._nat_gateway_instance_status

    @nat_gateway_instance_status.setter
    def nat_gateway_instance_status(self, nat_gateway_instance_status):
        """Sets the nat_gateway_instance_status of this NatGatewayInstance.

        NATGateway인스턴스상태  # noqa: E501

        :param nat_gateway_instance_status: The nat_gateway_instance_status of this NatGatewayInstance.  # noqa: E501
        :type: CommonCode
        """

        self._nat_gateway_instance_status = nat_gateway_instance_status

    @property
    def nat_gateway_instance_status_name(self):
        """Gets the nat_gateway_instance_status_name of this NatGatewayInstance.  # noqa: E501

        NATGateway인스턴스상태이름  # noqa: E501

        :return: The nat_gateway_instance_status_name of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_instance_status_name

    @nat_gateway_instance_status_name.setter
    def nat_gateway_instance_status_name(self, nat_gateway_instance_status_name):
        """Sets the nat_gateway_instance_status_name of this NatGatewayInstance.

        NATGateway인스턴스상태이름  # noqa: E501

        :param nat_gateway_instance_status_name: The nat_gateway_instance_status_name of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._nat_gateway_instance_status_name = nat_gateway_instance_status_name

    @property
    def nat_gateway_instance_operation(self):
        """Gets the nat_gateway_instance_operation of this NatGatewayInstance.  # noqa: E501

        NATGateway인스턴스OP  # noqa: E501

        :return: The nat_gateway_instance_operation of this NatGatewayInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._nat_gateway_instance_operation

    @nat_gateway_instance_operation.setter
    def nat_gateway_instance_operation(self, nat_gateway_instance_operation):
        """Sets the nat_gateway_instance_operation of this NatGatewayInstance.

        NATGateway인스턴스OP  # noqa: E501

        :param nat_gateway_instance_operation: The nat_gateway_instance_operation of this NatGatewayInstance.  # noqa: E501
        :type: CommonCode
        """

        self._nat_gateway_instance_operation = nat_gateway_instance_operation

    @property
    def create_date(self):
        """Gets the create_date of this NatGatewayInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this NatGatewayInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def nat_gateway_description(self):
        """Gets the nat_gateway_description of this NatGatewayInstance.  # noqa: E501

        NATGateway설명  # noqa: E501

        :return: The nat_gateway_description of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_description

    @nat_gateway_description.setter
    def nat_gateway_description(self, nat_gateway_description):
        """Sets the nat_gateway_description of this NatGatewayInstance.

        NATGateway설명  # noqa: E501

        :param nat_gateway_description: The nat_gateway_description of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._nat_gateway_description = nat_gateway_description

    @property
    def zone_code(self):
        """Gets the zone_code of this NatGatewayInstance.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this NatGatewayInstance.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this NatGatewayInstance.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this NatGatewayInstance.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

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
        if not isinstance(other, NatGatewayInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
