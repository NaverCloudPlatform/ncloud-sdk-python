# coding: utf-8

"""
    loadbalancer

    OpenAPI spec version: 2018-06-21T02:19:18Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_loadbalancer.model.load_balancer_rule_parameter import LoadBalancerRuleParameter  # noqa: F401,E501


class CreateLoadBalancerInstanceRequest(object):
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
        'load_balancer_name': 'str',
        'load_balancer_algorithm_type_code': 'str',
        'load_balancer_description': 'str',
        'load_balancer_rule_list': 'list[LoadBalancerRuleParameter]',
        'server_instance_no_list': 'list[str]',
        'internet_line_type_code': 'str',
        'network_usage_type_code': 'str',
        'region_no': 'str'
    }

    attribute_map = {
        'load_balancer_name': 'loadBalancerName',
        'load_balancer_algorithm_type_code': 'loadBalancerAlgorithmTypeCode',
        'load_balancer_description': 'loadBalancerDescription',
        'load_balancer_rule_list': 'loadBalancerRuleList',
        'server_instance_no_list': 'serverInstanceNoList',
        'internet_line_type_code': 'internetLineTypeCode',
        'network_usage_type_code': 'networkUsageTypeCode',
        'region_no': 'regionNo'
    }

    def __init__(self, load_balancer_name=None, load_balancer_algorithm_type_code=None, load_balancer_description=None, load_balancer_rule_list=None, server_instance_no_list=None, internet_line_type_code=None, network_usage_type_code=None, region_no=None):  # noqa: E501
        """CreateLoadBalancerInstanceRequest - a model defined in Swagger"""  # noqa: E501

        self._load_balancer_name = None
        self._load_balancer_algorithm_type_code = None
        self._load_balancer_description = None
        self._load_balancer_rule_list = None
        self._server_instance_no_list = None
        self._internet_line_type_code = None
        self._network_usage_type_code = None
        self._region_no = None
        self.discriminator = None

        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if load_balancer_algorithm_type_code is not None:
            self.load_balancer_algorithm_type_code = load_balancer_algorithm_type_code
        if load_balancer_description is not None:
            self.load_balancer_description = load_balancer_description
        self.load_balancer_rule_list = load_balancer_rule_list
        if server_instance_no_list is not None:
            self.server_instance_no_list = server_instance_no_list
        if internet_line_type_code is not None:
            self.internet_line_type_code = internet_line_type_code
        if network_usage_type_code is not None:
            self.network_usage_type_code = network_usage_type_code
        if region_no is not None:
            self.region_no = region_no

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        로드밸런서명  # noqa: E501

        :return: The load_balancer_name of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this CreateLoadBalancerInstanceRequest.

        로드밸런서명  # noqa: E501

        :param load_balancer_name: The load_balancer_name of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def load_balancer_algorithm_type_code(self):
        """Gets the load_balancer_algorithm_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        로드밸런서알고리즘구분코드  # noqa: E501

        :return: The load_balancer_algorithm_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_algorithm_type_code

    @load_balancer_algorithm_type_code.setter
    def load_balancer_algorithm_type_code(self, load_balancer_algorithm_type_code):
        """Sets the load_balancer_algorithm_type_code of this CreateLoadBalancerInstanceRequest.

        로드밸런서알고리즘구분코드  # noqa: E501

        :param load_balancer_algorithm_type_code: The load_balancer_algorithm_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_algorithm_type_code = load_balancer_algorithm_type_code

    @property
    def load_balancer_description(self):
        """Gets the load_balancer_description of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        로드밸런서설명  # noqa: E501

        :return: The load_balancer_description of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_description

    @load_balancer_description.setter
    def load_balancer_description(self, load_balancer_description):
        """Sets the load_balancer_description of this CreateLoadBalancerInstanceRequest.

        로드밸런서설명  # noqa: E501

        :param load_balancer_description: The load_balancer_description of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_description = load_balancer_description

    @property
    def load_balancer_rule_list(self):
        """Gets the load_balancer_rule_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        로드밸런서RULE리스트  # noqa: E501

        :return: The load_balancer_rule_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: list[LoadBalancerRuleParameter]
        """
        return self._load_balancer_rule_list

    @load_balancer_rule_list.setter
    def load_balancer_rule_list(self, load_balancer_rule_list):
        """Sets the load_balancer_rule_list of this CreateLoadBalancerInstanceRequest.

        로드밸런서RULE리스트  # noqa: E501

        :param load_balancer_rule_list: The load_balancer_rule_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: list[LoadBalancerRuleParameter]
        """
        if load_balancer_rule_list is None:
            raise ValueError("Invalid value for `load_balancer_rule_list`, must not be `None`")  # noqa: E501

        self._load_balancer_rule_list = load_balancer_rule_list

    @property
    def server_instance_no_list(self):
        """Gets the server_instance_no_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        서버인스턴스번호리스트  # noqa: E501

        :return: The server_instance_no_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_instance_no_list

    @server_instance_no_list.setter
    def server_instance_no_list(self, server_instance_no_list):
        """Sets the server_instance_no_list of this CreateLoadBalancerInstanceRequest.

        서버인스턴스번호리스트  # noqa: E501

        :param server_instance_no_list: The server_instance_no_list of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: list[str]
        """

        self._server_instance_no_list = server_instance_no_list

    @property
    def internet_line_type_code(self):
        """Gets the internet_line_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        인터넷라인구분코드  # noqa: E501

        :return: The internet_line_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._internet_line_type_code

    @internet_line_type_code.setter
    def internet_line_type_code(self, internet_line_type_code):
        """Sets the internet_line_type_code of this CreateLoadBalancerInstanceRequest.

        인터넷라인구분코드  # noqa: E501

        :param internet_line_type_code: The internet_line_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._internet_line_type_code = internet_line_type_code

    @property
    def network_usage_type_code(self):
        """Gets the network_usage_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        네트워크용도구분코드  # noqa: E501

        :return: The network_usage_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_usage_type_code

    @network_usage_type_code.setter
    def network_usage_type_code(self, network_usage_type_code):
        """Sets the network_usage_type_code of this CreateLoadBalancerInstanceRequest.

        네트워크용도구분코드  # noqa: E501

        :param network_usage_type_code: The network_usage_type_code of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._network_usage_type_code = network_usage_type_code

    @property
    def region_no(self):
        """Gets the region_no of this CreateLoadBalancerInstanceRequest.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this CreateLoadBalancerInstanceRequest.

        리전번호  # noqa: E501

        :param region_no: The region_no of this CreateLoadBalancerInstanceRequest.  # noqa: E501
        :type: str
        """

        self._region_no = region_no

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
        if not isinstance(other, CreateLoadBalancerInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other