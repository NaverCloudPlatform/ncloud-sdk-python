# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.common_code import CommonCode  # noqa: F401,E501


class PublicIpInstance(object):
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
        'public_ip_instance_no': 'str',
        'public_ip': 'str',
        'public_ip_description': 'str',
        'create_date': 'str',
        'public_ip_instance_status_name': 'str',
        'public_ip_instance_status': 'CommonCode',
        'server_instance_no': 'str',
        'server_name': 'str',
        'private_ip': 'str',
        'last_modify_date': 'str',
        'public_ip_instance_operation': 'CommonCode'
    }

    attribute_map = {
        'public_ip_instance_no': 'publicIpInstanceNo',
        'public_ip': 'publicIp',
        'public_ip_description': 'publicIpDescription',
        'create_date': 'createDate',
        'public_ip_instance_status_name': 'publicIpInstanceStatusName',
        'public_ip_instance_status': 'publicIpInstanceStatus',
        'server_instance_no': 'serverInstanceNo',
        'server_name': 'serverName',
        'private_ip': 'privateIp',
        'last_modify_date': 'lastModifyDate',
        'public_ip_instance_operation': 'publicIpInstanceOperation'
    }

    def __init__(self, public_ip_instance_no=None, public_ip=None, public_ip_description=None, create_date=None, public_ip_instance_status_name=None, public_ip_instance_status=None, server_instance_no=None, server_name=None, private_ip=None, last_modify_date=None, public_ip_instance_operation=None):  # noqa: E501
        """PublicIpInstance - a model defined in Swagger"""  # noqa: E501

        self._public_ip_instance_no = None
        self._public_ip = None
        self._public_ip_description = None
        self._create_date = None
        self._public_ip_instance_status_name = None
        self._public_ip_instance_status = None
        self._server_instance_no = None
        self._server_name = None
        self._private_ip = None
        self._last_modify_date = None
        self._public_ip_instance_operation = None
        self.discriminator = None

        if public_ip_instance_no is not None:
            self.public_ip_instance_no = public_ip_instance_no
        if public_ip is not None:
            self.public_ip = public_ip
        if public_ip_description is not None:
            self.public_ip_description = public_ip_description
        if create_date is not None:
            self.create_date = create_date
        if public_ip_instance_status_name is not None:
            self.public_ip_instance_status_name = public_ip_instance_status_name
        if public_ip_instance_status is not None:
            self.public_ip_instance_status = public_ip_instance_status
        if server_instance_no is not None:
            self.server_instance_no = server_instance_no
        if server_name is not None:
            self.server_name = server_name
        if private_ip is not None:
            self.private_ip = private_ip
        if last_modify_date is not None:
            self.last_modify_date = last_modify_date
        if public_ip_instance_operation is not None:
            self.public_ip_instance_operation = public_ip_instance_operation

    @property
    def public_ip_instance_no(self):
        """Gets the public_ip_instance_no of this PublicIpInstance.  # noqa: E501

        공인IP인스턴스번호  # noqa: E501

        :return: The public_ip_instance_no of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_instance_no

    @public_ip_instance_no.setter
    def public_ip_instance_no(self, public_ip_instance_no):
        """Sets the public_ip_instance_no of this PublicIpInstance.

        공인IP인스턴스번호  # noqa: E501

        :param public_ip_instance_no: The public_ip_instance_no of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._public_ip_instance_no = public_ip_instance_no

    @property
    def public_ip(self):
        """Gets the public_ip of this PublicIpInstance.  # noqa: E501

        공인IP주소  # noqa: E501

        :return: The public_ip of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this PublicIpInstance.

        공인IP주소  # noqa: E501

        :param public_ip: The public_ip of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def public_ip_description(self):
        """Gets the public_ip_description of this PublicIpInstance.  # noqa: E501

        공인IP설명  # noqa: E501

        :return: The public_ip_description of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_description

    @public_ip_description.setter
    def public_ip_description(self, public_ip_description):
        """Sets the public_ip_description of this PublicIpInstance.

        공인IP설명  # noqa: E501

        :param public_ip_description: The public_ip_description of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._public_ip_description = public_ip_description

    @property
    def create_date(self):
        """Gets the create_date of this PublicIpInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PublicIpInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def public_ip_instance_status_name(self):
        """Gets the public_ip_instance_status_name of this PublicIpInstance.  # noqa: E501

        공인IP인스턴스상태이름  # noqa: E501

        :return: The public_ip_instance_status_name of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_instance_status_name

    @public_ip_instance_status_name.setter
    def public_ip_instance_status_name(self, public_ip_instance_status_name):
        """Sets the public_ip_instance_status_name of this PublicIpInstance.

        공인IP인스턴스상태이름  # noqa: E501

        :param public_ip_instance_status_name: The public_ip_instance_status_name of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._public_ip_instance_status_name = public_ip_instance_status_name

    @property
    def public_ip_instance_status(self):
        """Gets the public_ip_instance_status of this PublicIpInstance.  # noqa: E501

        공인IP인스턴스상태  # noqa: E501

        :return: The public_ip_instance_status of this PublicIpInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._public_ip_instance_status

    @public_ip_instance_status.setter
    def public_ip_instance_status(self, public_ip_instance_status):
        """Sets the public_ip_instance_status of this PublicIpInstance.

        공인IP인스턴스상태  # noqa: E501

        :param public_ip_instance_status: The public_ip_instance_status of this PublicIpInstance.  # noqa: E501
        :type: CommonCode
        """

        self._public_ip_instance_status = public_ip_instance_status

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this PublicIpInstance.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this PublicIpInstance.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._server_instance_no = server_instance_no

    @property
    def server_name(self):
        """Gets the server_name of this PublicIpInstance.  # noqa: E501

        서버이름  # noqa: E501

        :return: The server_name of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this PublicIpInstance.

        서버이름  # noqa: E501

        :param server_name: The server_name of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

    @property
    def private_ip(self):
        """Gets the private_ip of this PublicIpInstance.  # noqa: E501

        사설IP주소  # noqa: E501

        :return: The private_ip of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this PublicIpInstance.

        사설IP주소  # noqa: E501

        :param private_ip: The private_ip of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def last_modify_date(self):
        """Gets the last_modify_date of this PublicIpInstance.  # noqa: E501

        마지막수정일시  # noqa: E501

        :return: The last_modify_date of this PublicIpInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_modify_date

    @last_modify_date.setter
    def last_modify_date(self, last_modify_date):
        """Sets the last_modify_date of this PublicIpInstance.

        마지막수정일시  # noqa: E501

        :param last_modify_date: The last_modify_date of this PublicIpInstance.  # noqa: E501
        :type: str
        """

        self._last_modify_date = last_modify_date

    @property
    def public_ip_instance_operation(self):
        """Gets the public_ip_instance_operation of this PublicIpInstance.  # noqa: E501

        공인IP인스턴스OP  # noqa: E501

        :return: The public_ip_instance_operation of this PublicIpInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._public_ip_instance_operation

    @public_ip_instance_operation.setter
    def public_ip_instance_operation(self, public_ip_instance_operation):
        """Sets the public_ip_instance_operation of this PublicIpInstance.

        공인IP인스턴스OP  # noqa: E501

        :param public_ip_instance_operation: The public_ip_instance_operation of this PublicIpInstance.  # noqa: E501
        :type: CommonCode
        """

        self._public_ip_instance_operation = public_ip_instance_operation

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
        if not isinstance(other, PublicIpInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
