# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vloadbalancer.model.common_code import CommonCode  # noqa: F401,E501


class LoadBalancerInstance(object):
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
        'load_balancer_instance_no': 'str',
        'load_balancer_instance_status': 'CommonCode',
        'load_balancer_instance_operation': 'CommonCode',
        'load_balancer_instance_status_name': 'str',
        'load_balancer_description': 'str',
        'create_date': 'str',
        'load_balancer_name': 'str',
        'load_balancer_domain': 'str',
        'load_balancer_ip_list': 'list[str]',
        'load_balancer_type': 'CommonCode',
        'load_balancer_network_type': 'CommonCode',
        'throughput_type': 'CommonCode',
        'idle_timeout': 'int',
        'vpc_no': 'str',
        'region_code': 'str',
        'subnet_no_list': 'list[str]',
        'load_balancer_listener_no_list': 'list[str]'
    }

    attribute_map = {
        'load_balancer_instance_no': 'loadBalancerInstanceNo',
        'load_balancer_instance_status': 'loadBalancerInstanceStatus',
        'load_balancer_instance_operation': 'loadBalancerInstanceOperation',
        'load_balancer_instance_status_name': 'loadBalancerInstanceStatusName',
        'load_balancer_description': 'loadBalancerDescription',
        'create_date': 'createDate',
        'load_balancer_name': 'loadBalancerName',
        'load_balancer_domain': 'loadBalancerDomain',
        'load_balancer_ip_list': 'loadBalancerIpList',
        'load_balancer_type': 'loadBalancerType',
        'load_balancer_network_type': 'loadBalancerNetworkType',
        'throughput_type': 'throughputType',
        'idle_timeout': 'idleTimeout',
        'vpc_no': 'vpcNo',
        'region_code': 'regionCode',
        'subnet_no_list': 'subnetNoList',
        'load_balancer_listener_no_list': 'loadBalancerListenerNoList'
    }

    def __init__(self, load_balancer_instance_no=None, load_balancer_instance_status=None, load_balancer_instance_operation=None, load_balancer_instance_status_name=None, load_balancer_description=None, create_date=None, load_balancer_name=None, load_balancer_domain=None, load_balancer_ip_list=None, load_balancer_type=None, load_balancer_network_type=None, throughput_type=None, idle_timeout=None, vpc_no=None, region_code=None, subnet_no_list=None, load_balancer_listener_no_list=None):  # noqa: E501
        """LoadBalancerInstance - a model defined in Swagger"""  # noqa: E501

        self._load_balancer_instance_no = None
        self._load_balancer_instance_status = None
        self._load_balancer_instance_operation = None
        self._load_balancer_instance_status_name = None
        self._load_balancer_description = None
        self._create_date = None
        self._load_balancer_name = None
        self._load_balancer_domain = None
        self._load_balancer_ip_list = None
        self._load_balancer_type = None
        self._load_balancer_network_type = None
        self._throughput_type = None
        self._idle_timeout = None
        self._vpc_no = None
        self._region_code = None
        self._subnet_no_list = None
        self._load_balancer_listener_no_list = None
        self.discriminator = None

        if load_balancer_instance_no is not None:
            self.load_balancer_instance_no = load_balancer_instance_no
        if load_balancer_instance_status is not None:
            self.load_balancer_instance_status = load_balancer_instance_status
        if load_balancer_instance_operation is not None:
            self.load_balancer_instance_operation = load_balancer_instance_operation
        if load_balancer_instance_status_name is not None:
            self.load_balancer_instance_status_name = load_balancer_instance_status_name
        if load_balancer_description is not None:
            self.load_balancer_description = load_balancer_description
        if create_date is not None:
            self.create_date = create_date
        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if load_balancer_domain is not None:
            self.load_balancer_domain = load_balancer_domain
        if load_balancer_ip_list is not None:
            self.load_balancer_ip_list = load_balancer_ip_list
        if load_balancer_type is not None:
            self.load_balancer_type = load_balancer_type
        if load_balancer_network_type is not None:
            self.load_balancer_network_type = load_balancer_network_type
        if throughput_type is not None:
            self.throughput_type = throughput_type
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if vpc_no is not None:
            self.vpc_no = vpc_no
        if region_code is not None:
            self.region_code = region_code
        if subnet_no_list is not None:
            self.subnet_no_list = subnet_no_list
        if load_balancer_listener_no_list is not None:
            self.load_balancer_listener_no_list = load_balancer_listener_no_list

    @property
    def load_balancer_instance_no(self):
        """Gets the load_balancer_instance_no of this LoadBalancerInstance.  # noqa: E501

        로드밸런서인스턴스번호  # noqa: E501

        :return: The load_balancer_instance_no of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_instance_no

    @load_balancer_instance_no.setter
    def load_balancer_instance_no(self, load_balancer_instance_no):
        """Sets the load_balancer_instance_no of this LoadBalancerInstance.

        로드밸런서인스턴스번호  # noqa: E501

        :param load_balancer_instance_no: The load_balancer_instance_no of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._load_balancer_instance_no = load_balancer_instance_no

    @property
    def load_balancer_instance_status(self):
        """Gets the load_balancer_instance_status of this LoadBalancerInstance.  # noqa: E501

        로드밸런서인스턴스상태  # noqa: E501

        :return: The load_balancer_instance_status of this LoadBalancerInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._load_balancer_instance_status

    @load_balancer_instance_status.setter
    def load_balancer_instance_status(self, load_balancer_instance_status):
        """Sets the load_balancer_instance_status of this LoadBalancerInstance.

        로드밸런서인스턴스상태  # noqa: E501

        :param load_balancer_instance_status: The load_balancer_instance_status of this LoadBalancerInstance.  # noqa: E501
        :type: CommonCode
        """

        self._load_balancer_instance_status = load_balancer_instance_status

    @property
    def load_balancer_instance_operation(self):
        """Gets the load_balancer_instance_operation of this LoadBalancerInstance.  # noqa: E501

        로드밸런서인스턴스OP  # noqa: E501

        :return: The load_balancer_instance_operation of this LoadBalancerInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._load_balancer_instance_operation

    @load_balancer_instance_operation.setter
    def load_balancer_instance_operation(self, load_balancer_instance_operation):
        """Sets the load_balancer_instance_operation of this LoadBalancerInstance.

        로드밸런서인스턴스OP  # noqa: E501

        :param load_balancer_instance_operation: The load_balancer_instance_operation of this LoadBalancerInstance.  # noqa: E501
        :type: CommonCode
        """

        self._load_balancer_instance_operation = load_balancer_instance_operation

    @property
    def load_balancer_instance_status_name(self):
        """Gets the load_balancer_instance_status_name of this LoadBalancerInstance.  # noqa: E501

        로드밸런서인스턴스상태이름  # noqa: E501

        :return: The load_balancer_instance_status_name of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_instance_status_name

    @load_balancer_instance_status_name.setter
    def load_balancer_instance_status_name(self, load_balancer_instance_status_name):
        """Sets the load_balancer_instance_status_name of this LoadBalancerInstance.

        로드밸런서인스턴스상태이름  # noqa: E501

        :param load_balancer_instance_status_name: The load_balancer_instance_status_name of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._load_balancer_instance_status_name = load_balancer_instance_status_name

    @property
    def load_balancer_description(self):
        """Gets the load_balancer_description of this LoadBalancerInstance.  # noqa: E501

        로드밸런서설명  # noqa: E501

        :return: The load_balancer_description of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_description

    @load_balancer_description.setter
    def load_balancer_description(self, load_balancer_description):
        """Sets the load_balancer_description of this LoadBalancerInstance.

        로드밸런서설명  # noqa: E501

        :param load_balancer_description: The load_balancer_description of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._load_balancer_description = load_balancer_description

    @property
    def create_date(self):
        """Gets the create_date of this LoadBalancerInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this LoadBalancerInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this LoadBalancerInstance.  # noqa: E501

        로드밸런서이름  # noqa: E501

        :return: The load_balancer_name of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this LoadBalancerInstance.

        로드밸런서이름  # noqa: E501

        :param load_balancer_name: The load_balancer_name of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def load_balancer_domain(self):
        """Gets the load_balancer_domain of this LoadBalancerInstance.  # noqa: E501

        로드밸런서도메인  # noqa: E501

        :return: The load_balancer_domain of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_domain

    @load_balancer_domain.setter
    def load_balancer_domain(self, load_balancer_domain):
        """Sets the load_balancer_domain of this LoadBalancerInstance.

        로드밸런서도메인  # noqa: E501

        :param load_balancer_domain: The load_balancer_domain of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._load_balancer_domain = load_balancer_domain

    @property
    def load_balancer_ip_list(self):
        """Gets the load_balancer_ip_list of this LoadBalancerInstance.  # noqa: E501

        로드밸런서IP리스트  # noqa: E501

        :return: The load_balancer_ip_list of this LoadBalancerInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_ip_list

    @load_balancer_ip_list.setter
    def load_balancer_ip_list(self, load_balancer_ip_list):
        """Sets the load_balancer_ip_list of this LoadBalancerInstance.

        로드밸런서IP리스트  # noqa: E501

        :param load_balancer_ip_list: The load_balancer_ip_list of this LoadBalancerInstance.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_ip_list = load_balancer_ip_list

    @property
    def load_balancer_type(self):
        """Gets the load_balancer_type of this LoadBalancerInstance.  # noqa: E501

        로드밸런서유형  # noqa: E501

        :return: The load_balancer_type of this LoadBalancerInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._load_balancer_type

    @load_balancer_type.setter
    def load_balancer_type(self, load_balancer_type):
        """Sets the load_balancer_type of this LoadBalancerInstance.

        로드밸런서유형  # noqa: E501

        :param load_balancer_type: The load_balancer_type of this LoadBalancerInstance.  # noqa: E501
        :type: CommonCode
        """

        self._load_balancer_type = load_balancer_type

    @property
    def load_balancer_network_type(self):
        """Gets the load_balancer_network_type of this LoadBalancerInstance.  # noqa: E501

        로드밸런서네트워크유형  # noqa: E501

        :return: The load_balancer_network_type of this LoadBalancerInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._load_balancer_network_type

    @load_balancer_network_type.setter
    def load_balancer_network_type(self, load_balancer_network_type):
        """Sets the load_balancer_network_type of this LoadBalancerInstance.

        로드밸런서네트워크유형  # noqa: E501

        :param load_balancer_network_type: The load_balancer_network_type of this LoadBalancerInstance.  # noqa: E501
        :type: CommonCode
        """

        self._load_balancer_network_type = load_balancer_network_type

    @property
    def throughput_type(self):
        """Gets the throughput_type of this LoadBalancerInstance.  # noqa: E501

        부하처리성능유형  # noqa: E501

        :return: The throughput_type of this LoadBalancerInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._throughput_type

    @throughput_type.setter
    def throughput_type(self, throughput_type):
        """Sets the throughput_type of this LoadBalancerInstance.

        부하처리성능유형  # noqa: E501

        :param throughput_type: The throughput_type of this LoadBalancerInstance.  # noqa: E501
        :type: CommonCode
        """

        self._throughput_type = throughput_type

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this LoadBalancerInstance.  # noqa: E501

        연결타임아웃  # noqa: E501

        :return: The idle_timeout of this LoadBalancerInstance.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this LoadBalancerInstance.

        연결타임아웃  # noqa: E501

        :param idle_timeout: The idle_timeout of this LoadBalancerInstance.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

    @property
    def vpc_no(self):
        """Gets the vpc_no of this LoadBalancerInstance.  # noqa: E501

        VPC번호  # noqa: E501

        :return: The vpc_no of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._vpc_no

    @vpc_no.setter
    def vpc_no(self, vpc_no):
        """Sets the vpc_no of this LoadBalancerInstance.

        VPC번호  # noqa: E501

        :param vpc_no: The vpc_no of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._vpc_no = vpc_no

    @property
    def region_code(self):
        """Gets the region_code of this LoadBalancerInstance.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this LoadBalancerInstance.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this LoadBalancerInstance.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this LoadBalancerInstance.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def subnet_no_list(self):
        """Gets the subnet_no_list of this LoadBalancerInstance.  # noqa: E501

        서브넷번호리스트  # noqa: E501

        :return: The subnet_no_list of this LoadBalancerInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_no_list

    @subnet_no_list.setter
    def subnet_no_list(self, subnet_no_list):
        """Sets the subnet_no_list of this LoadBalancerInstance.

        서브넷번호리스트  # noqa: E501

        :param subnet_no_list: The subnet_no_list of this LoadBalancerInstance.  # noqa: E501
        :type: list[str]
        """

        self._subnet_no_list = subnet_no_list

    @property
    def load_balancer_listener_no_list(self):
        """Gets the load_balancer_listener_no_list of this LoadBalancerInstance.  # noqa: E501

        로드밸런서리스너번호리스트  # noqa: E501

        :return: The load_balancer_listener_no_list of this LoadBalancerInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_listener_no_list

    @load_balancer_listener_no_list.setter
    def load_balancer_listener_no_list(self, load_balancer_listener_no_list):
        """Sets the load_balancer_listener_no_list of this LoadBalancerInstance.

        로드밸런서리스너번호리스트  # noqa: E501

        :param load_balancer_listener_no_list: The load_balancer_listener_no_list of this LoadBalancerInstance.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_listener_no_list = load_balancer_listener_no_list

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
        if not isinstance(other, LoadBalancerInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other