# coding: utf-8

"""
    vloadbalancer

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoadBalancerListenerParameter(object):
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
        'ssl_certificate_no': 'str',
        'use_http2': 'bool',
        'port': 'int',
        'protocol_type_code': 'str',
        'tls_min_version_type_code': 'str',
        'target_group_no': 'str'
    }

    attribute_map = {
        'ssl_certificate_no': 'sslCertificateNo',
        'use_http2': 'useHttp2',
        'port': 'port',
        'protocol_type_code': 'protocolTypeCode',
        'tls_min_version_type_code': 'tlsMinVersionTypeCode',
        'target_group_no': 'targetGroupNo'
    }

    def __init__(self, ssl_certificate_no=None, use_http2=None, port=None, protocol_type_code=None, tls_min_version_type_code=None, target_group_no=None):  # noqa: E501
        """LoadBalancerListenerParameter - a model defined in Swagger"""  # noqa: E501

        self._ssl_certificate_no = None
        self._use_http2 = None
        self._port = None
        self._protocol_type_code = None
        self._tls_min_version_type_code = None
        self._target_group_no = None
        self.discriminator = None

        if ssl_certificate_no is not None:
            self.ssl_certificate_no = ssl_certificate_no
        if use_http2 is not None:
            self.use_http2 = use_http2
        if port is not None:
            self.port = port
        if protocol_type_code is not None:
            self.protocol_type_code = protocol_type_code
        if tls_min_version_type_code is not None:
            self.tls_min_version_type_code = tls_min_version_type_code
        self.target_group_no = target_group_no

    @property
    def ssl_certificate_no(self):
        """Gets the ssl_certificate_no of this LoadBalancerListenerParameter.  # noqa: E501

        SSL인증서번호  # noqa: E501

        :return: The ssl_certificate_no of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: str
        """
        return self._ssl_certificate_no

    @ssl_certificate_no.setter
    def ssl_certificate_no(self, ssl_certificate_no):
        """Sets the ssl_certificate_no of this LoadBalancerListenerParameter.

        SSL인증서번호  # noqa: E501

        :param ssl_certificate_no: The ssl_certificate_no of this LoadBalancerListenerParameter.  # noqa: E501
        :type: str
        """

        self._ssl_certificate_no = ssl_certificate_no

    @property
    def use_http2(self):
        """Gets the use_http2 of this LoadBalancerListenerParameter.  # noqa: E501

        HTTP2사용여부  # noqa: E501

        :return: The use_http2 of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: bool
        """
        return self._use_http2

    @use_http2.setter
    def use_http2(self, use_http2):
        """Sets the use_http2 of this LoadBalancerListenerParameter.

        HTTP2사용여부  # noqa: E501

        :param use_http2: The use_http2 of this LoadBalancerListenerParameter.  # noqa: E501
        :type: bool
        """

        self._use_http2 = use_http2

    @property
    def port(self):
        """Gets the port of this LoadBalancerListenerParameter.  # noqa: E501

        포트  # noqa: E501

        :return: The port of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LoadBalancerListenerParameter.

        포트  # noqa: E501

        :param port: The port of this LoadBalancerListenerParameter.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol_type_code(self):
        """Gets the protocol_type_code of this LoadBalancerListenerParameter.  # noqa: E501

        프로토콜유형코드  # noqa: E501

        :return: The protocol_type_code of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type_code

    @protocol_type_code.setter
    def protocol_type_code(self, protocol_type_code):
        """Sets the protocol_type_code of this LoadBalancerListenerParameter.

        프로토콜유형코드  # noqa: E501

        :param protocol_type_code: The protocol_type_code of this LoadBalancerListenerParameter.  # noqa: E501
        :type: str
        """

        self._protocol_type_code = protocol_type_code

    @property
    def tls_min_version_type_code(self):
        """Gets the tls_min_version_type_code of this LoadBalancerListenerParameter.  # noqa: E501

        TLS최소지원버전유형코드  # noqa: E501

        :return: The tls_min_version_type_code of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: str
        """
        return self._tls_min_version_type_code

    @tls_min_version_type_code.setter
    def tls_min_version_type_code(self, tls_min_version_type_code):
        """Sets the tls_min_version_type_code of this LoadBalancerListenerParameter.

        TLS최소지원버전유형코드  # noqa: E501

        :param tls_min_version_type_code: The tls_min_version_type_code of this LoadBalancerListenerParameter.  # noqa: E501
        :type: str
        """

        self._tls_min_version_type_code = tls_min_version_type_code

    @property
    def target_group_no(self):
        """Gets the target_group_no of this LoadBalancerListenerParameter.  # noqa: E501

        타겟그룹번호  # noqa: E501

        :return: The target_group_no of this LoadBalancerListenerParameter.  # noqa: E501
        :rtype: str
        """
        return self._target_group_no

    @target_group_no.setter
    def target_group_no(self, target_group_no):
        """Sets the target_group_no of this LoadBalancerListenerParameter.

        타겟그룹번호  # noqa: E501

        :param target_group_no: The target_group_no of this LoadBalancerListenerParameter.  # noqa: E501
        :type: str
        """
        if target_group_no is None:
            raise ValueError("Invalid value for `target_group_no`, must not be `None`")  # noqa: E501

        self._target_group_no = target_group_no

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
        if not isinstance(other, LoadBalancerListenerParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
