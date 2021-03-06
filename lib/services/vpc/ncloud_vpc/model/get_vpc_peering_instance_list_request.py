# coding: utf-8

"""
    vpc

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetVpcPeeringInstanceListRequest(object):
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
        'vpc_peering_instance_no_list': 'list[str]',
        'source_vpc_name': 'str',
        'vpc_peering_name': 'str',
        'target_vpc_name': 'str',
        'vpc_peering_instance_status_code': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'vpc_peering_instance_no_list': 'vpcPeeringInstanceNoList',
        'source_vpc_name': 'sourceVpcName',
        'vpc_peering_name': 'vpcPeeringName',
        'target_vpc_name': 'targetVpcName',
        'vpc_peering_instance_status_code': 'vpcPeeringInstanceStatusCode',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, region_code=None, vpc_peering_instance_no_list=None, source_vpc_name=None, vpc_peering_name=None, target_vpc_name=None, vpc_peering_instance_status_code=None, page_no=None, page_size=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetVpcPeeringInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._vpc_peering_instance_no_list = None
        self._source_vpc_name = None
        self._vpc_peering_name = None
        self._target_vpc_name = None
        self._vpc_peering_instance_status_code = None
        self._page_no = None
        self._page_size = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if vpc_peering_instance_no_list is not None:
            self.vpc_peering_instance_no_list = vpc_peering_instance_no_list
        if source_vpc_name is not None:
            self.source_vpc_name = source_vpc_name
        if vpc_peering_name is not None:
            self.vpc_peering_name = vpc_peering_name
        if target_vpc_name is not None:
            self.target_vpc_name = target_vpc_name
        if vpc_peering_instance_status_code is not None:
            self.vpc_peering_instance_status_code = vpc_peering_instance_status_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def region_code(self):
        """Gets the region_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetVpcPeeringInstanceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def vpc_peering_instance_no_list(self):
        """Gets the vpc_peering_instance_no_list of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        VPCPeering인스턴스번호리스트  # noqa: E501

        :return: The vpc_peering_instance_no_list of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vpc_peering_instance_no_list

    @vpc_peering_instance_no_list.setter
    def vpc_peering_instance_no_list(self, vpc_peering_instance_no_list):
        """Sets the vpc_peering_instance_no_list of this GetVpcPeeringInstanceListRequest.

        VPCPeering인스턴스번호리스트  # noqa: E501

        :param vpc_peering_instance_no_list: The vpc_peering_instance_no_list of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._vpc_peering_instance_no_list = vpc_peering_instance_no_list

    @property
    def source_vpc_name(self):
        """Gets the source_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        요청VPC이름  # noqa: E501

        :return: The source_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_vpc_name

    @source_vpc_name.setter
    def source_vpc_name(self, source_vpc_name):
        """Sets the source_vpc_name of this GetVpcPeeringInstanceListRequest.

        요청VPC이름  # noqa: E501

        :param source_vpc_name: The source_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._source_vpc_name = source_vpc_name

    @property
    def vpc_peering_name(self):
        """Gets the vpc_peering_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        VPCPeering이름  # noqa: E501

        :return: The vpc_peering_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_name

    @vpc_peering_name.setter
    def vpc_peering_name(self, vpc_peering_name):
        """Sets the vpc_peering_name of this GetVpcPeeringInstanceListRequest.

        VPCPeering이름  # noqa: E501

        :param vpc_peering_name: The vpc_peering_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_peering_name = vpc_peering_name

    @property
    def target_vpc_name(self):
        """Gets the target_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        수락VPC이름  # noqa: E501

        :return: The target_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_vpc_name

    @target_vpc_name.setter
    def target_vpc_name(self, target_vpc_name):
        """Sets the target_vpc_name of this GetVpcPeeringInstanceListRequest.

        수락VPC이름  # noqa: E501

        :param target_vpc_name: The target_vpc_name of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._target_vpc_name = target_vpc_name

    @property
    def vpc_peering_instance_status_code(self):
        """Gets the vpc_peering_instance_status_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        VPCPeering인스턴스상태코드  # noqa: E501

        :return: The vpc_peering_instance_status_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_peering_instance_status_code

    @vpc_peering_instance_status_code.setter
    def vpc_peering_instance_status_code(self, vpc_peering_instance_status_code):
        """Sets the vpc_peering_instance_status_code of this GetVpcPeeringInstanceListRequest.

        VPCPeering인스턴스상태코드  # noqa: E501

        :param vpc_peering_instance_status_code: The vpc_peering_instance_status_code of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_peering_instance_status_code = vpc_peering_instance_status_code

    @property
    def page_no(self):
        """Gets the page_no of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetVpcPeeringInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetVpcPeeringInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetVpcPeeringInstanceListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetVpcPeeringInstanceListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetVpcPeeringInstanceListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetVpcPeeringInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

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
        if not isinstance(other, GetVpcPeeringInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
