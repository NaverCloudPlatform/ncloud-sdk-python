# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vpc.model.common_code import CommonCode  # noqa: F401,E501


class VpcPeeringInstance(object):
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
        'vpc_peering_instance_no': 'str',
        'vpc_peering_name': 'str',
        'region_code': 'str',
        'create_date': 'str',
        'last_modifiy_date': 'str',
        'vpc_peering_instance_status': 'CommonCode',
        'vpc_peering_instance_status_name': 'str',
        'vpc_peering_instance_operation': 'CommonCode',
        'source_vpc_no': 'str',
        'source_vpc_name': 'str',
        'source_vpc_ipv4_cidr_block': 'str',
        'source_vpc_login_id': 'str',
        'target_vpc_no': 'str',
        'target_vpc_name': 'str',
        'target_vpc_ipv4_cidr_block': 'str',
        'target_vpc_login_id': 'str',
        'vpc_peering_description': 'str',
        'has_reverse_vpc_peering': 'bool',
        'is_between_accounts': 'bool',
        'reverse_vpc_peering_instance_no': 'str'
    }

    attribute_map = {
        'vpc_peering_instance_no': 'vpcPeeringInstanceNo',
        'vpc_peering_name': 'vpcPeeringName',
        'region_code': 'regionCode',
        'create_date': 'createDate',
        'last_modifiy_date': 'lastModifiyDate',
        'vpc_peering_instance_status': 'vpcPeeringInstanceStatus',
        'vpc_peering_instance_status_name': 'vpcPeeringInstanceStatusName',
        'vpc_peering_instance_operation': 'vpcPeeringInstanceOperation',
        'source_vpc_no': 'sourceVpcNo',
        'source_vpc_name': 'sourceVpcName',
        'source_vpc_ipv4_cidr_block': 'sourceVpcIpv4CidrBlock',
        'source_vpc_login_id': 'sourceVpcLoginId',
        'target_vpc_no': 'targetVpcNo',
        'target_vpc_name': 'targetVpcName',
        'target_vpc_ipv4_cidr_block': 'targetVpcIpv4CidrBlock',
        'target_vpc_login_id': 'targetVpcLoginId',
        'vpc_peering_description': 'vpcPeeringDescription',
        'has_reverse_vpc_peering': 'hasReverseVpcPeering',
        'is_between_accounts': 'isBetweenAccounts',
        'reverse_vpc_peering_instance_no': 'reverseVpcPeeringInstanceNo'
    }

    def __init__(self, vpc_peering_instance_no=None, vpc_peering_name=None, region_code=None, create_date=None, last_modifiy_date=None, vpc_peering_instance_status=None, vpc_peering_instance_status_name=None, vpc_peering_instance_operation=None, source_vpc_no=None, source_vpc_name=None, source_vpc_ipv4_cidr_block=None, source_vpc_login_id=None, target_vpc_no=None, target_vpc_name=None, target_vpc_ipv4_cidr_block=None, target_vpc_login_id=None, vpc_peering_description=None, has_reverse_vpc_peering=None, is_between_accounts=None, reverse_vpc_peering_instance_no=None):  # noqa: E501
        """VpcPeeringInstance - a model defined in Swagger"""  # noqa: E501

        self._vpc_peering_instance_no = None
        self._vpc_peering_name = None
        self._region_code = None
        self._create_date = None
        self._last_modifiy_date = None
        self._vpc_peering_instance_status = None
        self._vpc_peering_instance_status_name = None
        self._vpc_peering_instance_operation = None
        self._source_vpc_no = None
        self._source_vpc_name = None
        self._source_vpc_ipv4_cidr_block = None
        self._source_vpc_login_id = None
        self._target_vpc_no = None
        self._target_vpc_name = None
        self._target_vpc_ipv4_cidr_block = None
        self._target_vpc_login_id = None
        self._vpc_peering_description = None
        self._has_reverse_vpc_peering = None
        self._is_between_accounts = None
        self._reverse_vpc_peering_instance_no = None
        self.discriminator = None

        if vpc_peering_instance_no is not None:
            self.vpc_peering_instance_no = vpc_peering_instance_no
        if vpc_peering_name is not None:
            self.vpc_peering_name = vpc_peering_name
        if region_code is not None:
            self.region_code = region_code
        if create_date is not None:
            self.create_date = create_date
        if last_modifiy_date is not None:
            self.last_modifiy_date = last_modifiy_date
        if vpc_peering_instance_status is not None:
            self.vpc_peering_instance_status = vpc_peering_instance_status
        if vpc_peering_instance_status_name is not None:
            self.vpc_peering_instance_status_name = vpc_peering_instance_status_name
        if vpc_peering_instance_operation is not None:
            self.vpc_peering_instance_operation = vpc_peering_instance_operation
        if source_vpc_no is not None:
            self.source_vpc_no = source_vpc_no
        if source_vpc_name is not None:
            self.source_vpc_name = source_vpc_name
        if source_vpc_ipv4_cidr_block is not None:
            self.source_vpc_ipv4_cidr_block = source_vpc_ipv4_cidr_block
        if source_vpc_login_id is not None:
            self.source_vpc_login_id = source_vpc_login_id
        if target_vpc_no is not None:
            self.target_vpc_no = target_vpc_no
        if target_vpc_name is not None:
            self.target_vpc_name = target_vpc_name
        if target_vpc_ipv4_cidr_block is not None:
            self.target_vpc_ipv4_cidr_block = target_vpc_ipv4_cidr_block
        if target_vpc_login_id is not None:
            self.target_vpc_login_id = target_vpc_login_id
        if vpc_peering_description is not None:
            self.vpc_peering_description = vpc_peering_description
        if has_reverse_vpc_peering is not None:
            self.has_reverse_vpc_peering = has_reverse_vpc_peering
        if is_between_accounts is not None:
            self.is_between_accounts = is_between_accounts
        if reverse_vpc_peering_instance_no is not None:
            self.reverse_vpc_peering_instance_no = reverse_vpc_peering_instance_no

    @property
    def vpc_peering_instance_no(self):
        """Gets the vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501

        VPCPeering인스턴스번호  # noqa: E501

        :return: The vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_instance_no

    @vpc_peering_instance_no.setter
    def vpc_peering_instance_no(self, vpc_peering_instance_no):
        """Sets the vpc_peering_instance_no of this VpcPeeringInstance.

        VPCPeering인스턴스번호  # noqa: E501

        :param vpc_peering_instance_no: The vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._vpc_peering_instance_no = vpc_peering_instance_no

    @property
    def vpc_peering_name(self):
        """Gets the vpc_peering_name of this VpcPeeringInstance.  # noqa: E501

        VPCPeering이름  # noqa: E501

        :return: The vpc_peering_name of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_name

    @vpc_peering_name.setter
    def vpc_peering_name(self, vpc_peering_name):
        """Sets the vpc_peering_name of this VpcPeeringInstance.

        VPCPeering이름  # noqa: E501

        :param vpc_peering_name: The vpc_peering_name of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._vpc_peering_name = vpc_peering_name

    @property
    def region_code(self):
        """Gets the region_code of this VpcPeeringInstance.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this VpcPeeringInstance.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def create_date(self):
        """Gets the create_date of this VpcPeeringInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this VpcPeeringInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def last_modifiy_date(self):
        """Gets the last_modifiy_date of this VpcPeeringInstance.  # noqa: E501

        마지막수정일시  # noqa: E501

        :return: The last_modifiy_date of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_modifiy_date

    @last_modifiy_date.setter
    def last_modifiy_date(self, last_modifiy_date):
        """Sets the last_modifiy_date of this VpcPeeringInstance.

        마지막수정일시  # noqa: E501

        :param last_modifiy_date: The last_modifiy_date of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._last_modifiy_date = last_modifiy_date

    @property
    def vpc_peering_instance_status(self):
        """Gets the vpc_peering_instance_status of this VpcPeeringInstance.  # noqa: E501

        VPCPeering인스턴스상태  # noqa: E501

        :return: The vpc_peering_instance_status of this VpcPeeringInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._vpc_peering_instance_status

    @vpc_peering_instance_status.setter
    def vpc_peering_instance_status(self, vpc_peering_instance_status):
        """Sets the vpc_peering_instance_status of this VpcPeeringInstance.

        VPCPeering인스턴스상태  # noqa: E501

        :param vpc_peering_instance_status: The vpc_peering_instance_status of this VpcPeeringInstance.  # noqa: E501
        :type: CommonCode
        """

        self._vpc_peering_instance_status = vpc_peering_instance_status

    @property
    def vpc_peering_instance_status_name(self):
        """Gets the vpc_peering_instance_status_name of this VpcPeeringInstance.  # noqa: E501

        VPCPeering인스턴스상태이름  # noqa: E501

        :return: The vpc_peering_instance_status_name of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_instance_status_name

    @vpc_peering_instance_status_name.setter
    def vpc_peering_instance_status_name(self, vpc_peering_instance_status_name):
        """Sets the vpc_peering_instance_status_name of this VpcPeeringInstance.

        VPCPeering인스턴스상태이름  # noqa: E501

        :param vpc_peering_instance_status_name: The vpc_peering_instance_status_name of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._vpc_peering_instance_status_name = vpc_peering_instance_status_name

    @property
    def vpc_peering_instance_operation(self):
        """Gets the vpc_peering_instance_operation of this VpcPeeringInstance.  # noqa: E501

        VPCPeering인스턴스OP  # noqa: E501

        :return: The vpc_peering_instance_operation of this VpcPeeringInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._vpc_peering_instance_operation

    @vpc_peering_instance_operation.setter
    def vpc_peering_instance_operation(self, vpc_peering_instance_operation):
        """Sets the vpc_peering_instance_operation of this VpcPeeringInstance.

        VPCPeering인스턴스OP  # noqa: E501

        :param vpc_peering_instance_operation: The vpc_peering_instance_operation of this VpcPeeringInstance.  # noqa: E501
        :type: CommonCode
        """

        self._vpc_peering_instance_operation = vpc_peering_instance_operation

    @property
    def source_vpc_no(self):
        """Gets the source_vpc_no of this VpcPeeringInstance.  # noqa: E501

        요청VPC번호  # noqa: E501

        :return: The source_vpc_no of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_vpc_no

    @source_vpc_no.setter
    def source_vpc_no(self, source_vpc_no):
        """Sets the source_vpc_no of this VpcPeeringInstance.

        요청VPC번호  # noqa: E501

        :param source_vpc_no: The source_vpc_no of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._source_vpc_no = source_vpc_no

    @property
    def source_vpc_name(self):
        """Gets the source_vpc_name of this VpcPeeringInstance.  # noqa: E501

        요청VPC이름  # noqa: E501

        :return: The source_vpc_name of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_vpc_name

    @source_vpc_name.setter
    def source_vpc_name(self, source_vpc_name):
        """Sets the source_vpc_name of this VpcPeeringInstance.

        요청VPC이름  # noqa: E501

        :param source_vpc_name: The source_vpc_name of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._source_vpc_name = source_vpc_name

    @property
    def source_vpc_ipv4_cidr_block(self):
        """Gets the source_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501

        요청VPC IPv4 CIDR블록  # noqa: E501

        :return: The source_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_vpc_ipv4_cidr_block

    @source_vpc_ipv4_cidr_block.setter
    def source_vpc_ipv4_cidr_block(self, source_vpc_ipv4_cidr_block):
        """Sets the source_vpc_ipv4_cidr_block of this VpcPeeringInstance.

        요청VPC IPv4 CIDR블록  # noqa: E501

        :param source_vpc_ipv4_cidr_block: The source_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._source_vpc_ipv4_cidr_block = source_vpc_ipv4_cidr_block

    @property
    def source_vpc_login_id(self):
        """Gets the source_vpc_login_id of this VpcPeeringInstance.  # noqa: E501

        요청VPC소유자ID  # noqa: E501

        :return: The source_vpc_login_id of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_vpc_login_id

    @source_vpc_login_id.setter
    def source_vpc_login_id(self, source_vpc_login_id):
        """Sets the source_vpc_login_id of this VpcPeeringInstance.

        요청VPC소유자ID  # noqa: E501

        :param source_vpc_login_id: The source_vpc_login_id of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._source_vpc_login_id = source_vpc_login_id

    @property
    def target_vpc_no(self):
        """Gets the target_vpc_no of this VpcPeeringInstance.  # noqa: E501

        수락VPC번호  # noqa: E501

        :return: The target_vpc_no of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._target_vpc_no

    @target_vpc_no.setter
    def target_vpc_no(self, target_vpc_no):
        """Sets the target_vpc_no of this VpcPeeringInstance.

        수락VPC번호  # noqa: E501

        :param target_vpc_no: The target_vpc_no of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._target_vpc_no = target_vpc_no

    @property
    def target_vpc_name(self):
        """Gets the target_vpc_name of this VpcPeeringInstance.  # noqa: E501

        수락VPC이름  # noqa: E501

        :return: The target_vpc_name of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._target_vpc_name

    @target_vpc_name.setter
    def target_vpc_name(self, target_vpc_name):
        """Sets the target_vpc_name of this VpcPeeringInstance.

        수락VPC이름  # noqa: E501

        :param target_vpc_name: The target_vpc_name of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._target_vpc_name = target_vpc_name

    @property
    def target_vpc_ipv4_cidr_block(self):
        """Gets the target_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501

        수락VPC IPv4 CIDR블록  # noqa: E501

        :return: The target_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._target_vpc_ipv4_cidr_block

    @target_vpc_ipv4_cidr_block.setter
    def target_vpc_ipv4_cidr_block(self, target_vpc_ipv4_cidr_block):
        """Sets the target_vpc_ipv4_cidr_block of this VpcPeeringInstance.

        수락VPC IPv4 CIDR블록  # noqa: E501

        :param target_vpc_ipv4_cidr_block: The target_vpc_ipv4_cidr_block of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._target_vpc_ipv4_cidr_block = target_vpc_ipv4_cidr_block

    @property
    def target_vpc_login_id(self):
        """Gets the target_vpc_login_id of this VpcPeeringInstance.  # noqa: E501

        수락VPC소유자ID  # noqa: E501

        :return: The target_vpc_login_id of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._target_vpc_login_id

    @target_vpc_login_id.setter
    def target_vpc_login_id(self, target_vpc_login_id):
        """Sets the target_vpc_login_id of this VpcPeeringInstance.

        수락VPC소유자ID  # noqa: E501

        :param target_vpc_login_id: The target_vpc_login_id of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._target_vpc_login_id = target_vpc_login_id

    @property
    def vpc_peering_description(self):
        """Gets the vpc_peering_description of this VpcPeeringInstance.  # noqa: E501

        VPCPeering설명  # noqa: E501

        :return: The vpc_peering_description of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_description

    @vpc_peering_description.setter
    def vpc_peering_description(self, vpc_peering_description):
        """Sets the vpc_peering_description of this VpcPeeringInstance.

        VPCPeering설명  # noqa: E501

        :param vpc_peering_description: The vpc_peering_description of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._vpc_peering_description = vpc_peering_description

    @property
    def has_reverse_vpc_peering(self):
        """Gets the has_reverse_vpc_peering of this VpcPeeringInstance.  # noqa: E501

        역방향VPCPeering존재여부  # noqa: E501

        :return: The has_reverse_vpc_peering of this VpcPeeringInstance.  # noqa: E501
        :rtype: bool
        """
        return self._has_reverse_vpc_peering

    @has_reverse_vpc_peering.setter
    def has_reverse_vpc_peering(self, has_reverse_vpc_peering):
        """Sets the has_reverse_vpc_peering of this VpcPeeringInstance.

        역방향VPCPeering존재여부  # noqa: E501

        :param has_reverse_vpc_peering: The has_reverse_vpc_peering of this VpcPeeringInstance.  # noqa: E501
        :type: bool
        """

        self._has_reverse_vpc_peering = has_reverse_vpc_peering

    @property
    def is_between_accounts(self):
        """Gets the is_between_accounts of this VpcPeeringInstance.  # noqa: E501

        계정간의VPCPeering여부  # noqa: E501

        :return: The is_between_accounts of this VpcPeeringInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_between_accounts

    @is_between_accounts.setter
    def is_between_accounts(self, is_between_accounts):
        """Sets the is_between_accounts of this VpcPeeringInstance.

        계정간의VPCPeering여부  # noqa: E501

        :param is_between_accounts: The is_between_accounts of this VpcPeeringInstance.  # noqa: E501
        :type: bool
        """

        self._is_between_accounts = is_between_accounts

    @property
    def reverse_vpc_peering_instance_no(self):
        """Gets the reverse_vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501

        역방향VPCPeering인스턴스번호  # noqa: E501

        :return: The reverse_vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501
        :rtype: str
        """
        return self._reverse_vpc_peering_instance_no

    @reverse_vpc_peering_instance_no.setter
    def reverse_vpc_peering_instance_no(self, reverse_vpc_peering_instance_no):
        """Sets the reverse_vpc_peering_instance_no of this VpcPeeringInstance.

        역방향VPCPeering인스턴스번호  # noqa: E501

        :param reverse_vpc_peering_instance_no: The reverse_vpc_peering_instance_no of this VpcPeeringInstance.  # noqa: E501
        :type: str
        """

        self._reverse_vpc_peering_instance_no = reverse_vpc_peering_instance_no

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
        if not isinstance(other, VpcPeeringInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
