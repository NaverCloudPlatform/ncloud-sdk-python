# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-10-17T10:28:43Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_server.model.common_code import CommonCode  # noqa: F401,E501
from ncloud_server.model.region import Region  # noqa: F401,E501
from ncloud_server.model.zone import Zone  # noqa: F401,E501


class PrivateSubnetInstance(object):
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
        'private_subnet_instance_no': 'str',
        'subnet': 'str',
        'private_subnet_description': 'str',
        'create_date': 'str',
        'private_subnet_instance_status': 'CommonCode',
        'private_subnet_instance_operation': 'CommonCode',
        'private_subnet_instance_status_name': 'str',
        'region': 'Region',
        'zone': 'Zone'
    }

    attribute_map = {
        'private_subnet_instance_no': 'privateSubnetInstanceNo',
        'subnet': 'subnet',
        'private_subnet_description': 'privateSubnetDescription',
        'create_date': 'createDate',
        'private_subnet_instance_status': 'privateSubnetInstanceStatus',
        'private_subnet_instance_operation': 'privateSubnetInstanceOperation',
        'private_subnet_instance_status_name': 'privateSubnetInstanceStatusName',
        'region': 'region',
        'zone': 'zone'
    }

    def __init__(self, private_subnet_instance_no=None, subnet=None, private_subnet_description=None, create_date=None, private_subnet_instance_status=None, private_subnet_instance_operation=None, private_subnet_instance_status_name=None, region=None, zone=None):  # noqa: E501
        """PrivateSubnetInstance - a model defined in Swagger"""  # noqa: E501

        self._private_subnet_instance_no = None
        self._subnet = None
        self._private_subnet_description = None
        self._create_date = None
        self._private_subnet_instance_status = None
        self._private_subnet_instance_operation = None
        self._private_subnet_instance_status_name = None
        self._region = None
        self._zone = None
        self.discriminator = None

        if private_subnet_instance_no is not None:
            self.private_subnet_instance_no = private_subnet_instance_no
        if subnet is not None:
            self.subnet = subnet
        if private_subnet_description is not None:
            self.private_subnet_description = private_subnet_description
        if create_date is not None:
            self.create_date = create_date
        if private_subnet_instance_status is not None:
            self.private_subnet_instance_status = private_subnet_instance_status
        if private_subnet_instance_operation is not None:
            self.private_subnet_instance_operation = private_subnet_instance_operation
        if private_subnet_instance_status_name is not None:
            self.private_subnet_instance_status_name = private_subnet_instance_status_name
        if region is not None:
            self.region = region
        if zone is not None:
            self.zone = zone

    @property
    def private_subnet_instance_no(self):
        """Gets the private_subnet_instance_no of this PrivateSubnetInstance.  # noqa: E501

        Private Subnet인스턴스번호  # noqa: E501

        :return: The private_subnet_instance_no of this PrivateSubnetInstance.  # noqa: E501
        :rtype: str
        """
        return self._private_subnet_instance_no

    @private_subnet_instance_no.setter
    def private_subnet_instance_no(self, private_subnet_instance_no):
        """Sets the private_subnet_instance_no of this PrivateSubnetInstance.

        Private Subnet인스턴스번호  # noqa: E501

        :param private_subnet_instance_no: The private_subnet_instance_no of this PrivateSubnetInstance.  # noqa: E501
        :type: str
        """

        self._private_subnet_instance_no = private_subnet_instance_no

    @property
    def subnet(self):
        """Gets the subnet of this PrivateSubnetInstance.  # noqa: E501

        서브넷  # noqa: E501

        :return: The subnet of this PrivateSubnetInstance.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this PrivateSubnetInstance.

        서브넷  # noqa: E501

        :param subnet: The subnet of this PrivateSubnetInstance.  # noqa: E501
        :type: str
        """

        self._subnet = subnet

    @property
    def private_subnet_description(self):
        """Gets the private_subnet_description of this PrivateSubnetInstance.  # noqa: E501

        Private Subnet설명  # noqa: E501

        :return: The private_subnet_description of this PrivateSubnetInstance.  # noqa: E501
        :rtype: str
        """
        return self._private_subnet_description

    @private_subnet_description.setter
    def private_subnet_description(self, private_subnet_description):
        """Sets the private_subnet_description of this PrivateSubnetInstance.

        Private Subnet설명  # noqa: E501

        :param private_subnet_description: The private_subnet_description of this PrivateSubnetInstance.  # noqa: E501
        :type: str
        """

        self._private_subnet_description = private_subnet_description

    @property
    def create_date(self):
        """Gets the create_date of this PrivateSubnetInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this PrivateSubnetInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PrivateSubnetInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this PrivateSubnetInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def private_subnet_instance_status(self):
        """Gets the private_subnet_instance_status of this PrivateSubnetInstance.  # noqa: E501

        Private Subnet인스턴스상태  # noqa: E501

        :return: The private_subnet_instance_status of this PrivateSubnetInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._private_subnet_instance_status

    @private_subnet_instance_status.setter
    def private_subnet_instance_status(self, private_subnet_instance_status):
        """Sets the private_subnet_instance_status of this PrivateSubnetInstance.

        Private Subnet인스턴스상태  # noqa: E501

        :param private_subnet_instance_status: The private_subnet_instance_status of this PrivateSubnetInstance.  # noqa: E501
        :type: CommonCode
        """

        self._private_subnet_instance_status = private_subnet_instance_status

    @property
    def private_subnet_instance_operation(self):
        """Gets the private_subnet_instance_operation of this PrivateSubnetInstance.  # noqa: E501

        Private Subnet OP  # noqa: E501

        :return: The private_subnet_instance_operation of this PrivateSubnetInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._private_subnet_instance_operation

    @private_subnet_instance_operation.setter
    def private_subnet_instance_operation(self, private_subnet_instance_operation):
        """Sets the private_subnet_instance_operation of this PrivateSubnetInstance.

        Private Subnet OP  # noqa: E501

        :param private_subnet_instance_operation: The private_subnet_instance_operation of this PrivateSubnetInstance.  # noqa: E501
        :type: CommonCode
        """

        self._private_subnet_instance_operation = private_subnet_instance_operation

    @property
    def private_subnet_instance_status_name(self):
        """Gets the private_subnet_instance_status_name of this PrivateSubnetInstance.  # noqa: E501

        Private Subnet상태이름  # noqa: E501

        :return: The private_subnet_instance_status_name of this PrivateSubnetInstance.  # noqa: E501
        :rtype: str
        """
        return self._private_subnet_instance_status_name

    @private_subnet_instance_status_name.setter
    def private_subnet_instance_status_name(self, private_subnet_instance_status_name):
        """Sets the private_subnet_instance_status_name of this PrivateSubnetInstance.

        Private Subnet상태이름  # noqa: E501

        :param private_subnet_instance_status_name: The private_subnet_instance_status_name of this PrivateSubnetInstance.  # noqa: E501
        :type: str
        """

        self._private_subnet_instance_status_name = private_subnet_instance_status_name

    @property
    def region(self):
        """Gets the region of this PrivateSubnetInstance.  # noqa: E501

        리전  # noqa: E501

        :return: The region of this PrivateSubnetInstance.  # noqa: E501
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PrivateSubnetInstance.

        리전  # noqa: E501

        :param region: The region of this PrivateSubnetInstance.  # noqa: E501
        :type: Region
        """

        self._region = region

    @property
    def zone(self):
        """Gets the zone of this PrivateSubnetInstance.  # noqa: E501

        ZONE  # noqa: E501

        :return: The zone of this PrivateSubnetInstance.  # noqa: E501
        :rtype: Zone
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this PrivateSubnetInstance.

        ZONE  # noqa: E501

        :param zone: The zone of this PrivateSubnetInstance.  # noqa: E501
        :type: Zone
        """

        self._zone = zone

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
        if not isinstance(other, PrivateSubnetInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
