# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AcceptOrRejectVpcPeeringRequest(object):
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
        'vpc_peering_instance_no': 'str',
        'is_accept': 'bool'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'vpc_peering_instance_no': 'vpcPeeringInstanceNo',
        'is_accept': 'isAccept'
    }

    def __init__(self, region_code=None, vpc_peering_instance_no=None, is_accept=None):  # noqa: E501
        """AcceptOrRejectVpcPeeringRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._vpc_peering_instance_no = None
        self._is_accept = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        self.vpc_peering_instance_no = vpc_peering_instance_no
        self.is_accept = is_accept

    @property
    def region_code(self):
        """Gets the region_code of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this AcceptOrRejectVpcPeeringRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def vpc_peering_instance_no(self):
        """Gets the vpc_peering_instance_no of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501

        VPCPeering인스턴스번호  # noqa: E501

        :return: The vpc_peering_instance_no of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_instance_no

    @vpc_peering_instance_no.setter
    def vpc_peering_instance_no(self, vpc_peering_instance_no):
        """Sets the vpc_peering_instance_no of this AcceptOrRejectVpcPeeringRequest.

        VPCPeering인스턴스번호  # noqa: E501

        :param vpc_peering_instance_no: The vpc_peering_instance_no of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :type: str
        """
        if vpc_peering_instance_no is None:
            raise ValueError("Invalid value for `vpc_peering_instance_no`, must not be `None`")  # noqa: E501

        self._vpc_peering_instance_no = vpc_peering_instance_no

    @property
    def is_accept(self):
        """Gets the is_accept of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501

        수락여부  # noqa: E501

        :return: The is_accept of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_accept

    @is_accept.setter
    def is_accept(self, is_accept):
        """Sets the is_accept of this AcceptOrRejectVpcPeeringRequest.

        수락여부  # noqa: E501

        :param is_accept: The is_accept of this AcceptOrRejectVpcPeeringRequest.  # noqa: E501
        :type: bool
        """
        if is_accept is None:
            raise ValueError("Invalid value for `is_accept`, must not be `None`")  # noqa: E501

        self._is_accept = is_accept

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
        if not isinstance(other, AcceptOrRejectVpcPeeringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other