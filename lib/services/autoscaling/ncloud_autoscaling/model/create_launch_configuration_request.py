# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-11-13T06:27:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateLaunchConfigurationRequest(object):
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
        'launch_configuration_name': 'str',
        'server_image_product_code': 'str',
        'server_product_code': 'str',
        'member_server_image_no': 'str',
        'access_control_group_configuration_no_list': 'list[str]',
        'login_key_name': 'str',
        'user_data': 'str',
        'region_no': 'str'
    }

    attribute_map = {
        'launch_configuration_name': 'launchConfigurationName',
        'server_image_product_code': 'serverImageProductCode',
        'server_product_code': 'serverProductCode',
        'member_server_image_no': 'memberServerImageNo',
        'access_control_group_configuration_no_list': 'accessControlGroupConfigurationNoList',
        'login_key_name': 'loginKeyName',
        'user_data': 'userData',
        'region_no': 'regionNo'
    }

    def __init__(self, launch_configuration_name=None, server_image_product_code=None, server_product_code=None, member_server_image_no=None, access_control_group_configuration_no_list=None, login_key_name=None, user_data=None, region_no=None):  # noqa: E501
        """CreateLaunchConfigurationRequest - a model defined in Swagger"""  # noqa: E501

        self._launch_configuration_name = None
        self._server_image_product_code = None
        self._server_product_code = None
        self._member_server_image_no = None
        self._access_control_group_configuration_no_list = None
        self._login_key_name = None
        self._user_data = None
        self._region_no = None
        self.discriminator = None

        if launch_configuration_name is not None:
            self.launch_configuration_name = launch_configuration_name
        if server_image_product_code is not None:
            self.server_image_product_code = server_image_product_code
        if server_product_code is not None:
            self.server_product_code = server_product_code
        if member_server_image_no is not None:
            self.member_server_image_no = member_server_image_no
        if access_control_group_configuration_no_list is not None:
            self.access_control_group_configuration_no_list = access_control_group_configuration_no_list
        if login_key_name is not None:
            self.login_key_name = login_key_name
        if user_data is not None:
            self.user_data = user_data
        if region_no is not None:
            self.region_no = region_no

    @property
    def launch_configuration_name(self):
        """Gets the launch_configuration_name of this CreateLaunchConfigurationRequest.  # noqa: E501

        론치설정명  # noqa: E501

        :return: The launch_configuration_name of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._launch_configuration_name

    @launch_configuration_name.setter
    def launch_configuration_name(self, launch_configuration_name):
        """Sets the launch_configuration_name of this CreateLaunchConfigurationRequest.

        론치설정명  # noqa: E501

        :param launch_configuration_name: The launch_configuration_name of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._launch_configuration_name = launch_configuration_name

    @property
    def server_image_product_code(self):
        """Gets the server_image_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501

        소프트웨어상품코드  # noqa: E501

        :return: The server_image_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_image_product_code

    @server_image_product_code.setter
    def server_image_product_code(self, server_image_product_code):
        """Sets the server_image_product_code of this CreateLaunchConfigurationRequest.

        소프트웨어상품코드  # noqa: E501

        :param server_image_product_code: The server_image_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._server_image_product_code = server_image_product_code

    @property
    def server_product_code(self):
        """Gets the server_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501

        서버상품코드  # noqa: E501

        :return: The server_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_product_code

    @server_product_code.setter
    def server_product_code(self, server_product_code):
        """Sets the server_product_code of this CreateLaunchConfigurationRequest.

        서버상품코드  # noqa: E501

        :param server_product_code: The server_product_code of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._server_product_code = server_product_code

    @property
    def member_server_image_no(self):
        """Gets the member_server_image_no of this CreateLaunchConfigurationRequest.  # noqa: E501

        회원서버이미지번호  # noqa: E501

        :return: The member_server_image_no of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_no

    @member_server_image_no.setter
    def member_server_image_no(self, member_server_image_no):
        """Sets the member_server_image_no of this CreateLaunchConfigurationRequest.

        회원서버이미지번호  # noqa: E501

        :param member_server_image_no: The member_server_image_no of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._member_server_image_no = member_server_image_no

    @property
    def access_control_group_configuration_no_list(self):
        """Gets the access_control_group_configuration_no_list of this CreateLaunchConfigurationRequest.  # noqa: E501

        ACG설정번호리스트  # noqa: E501

        :return: The access_control_group_configuration_no_list of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_control_group_configuration_no_list

    @access_control_group_configuration_no_list.setter
    def access_control_group_configuration_no_list(self, access_control_group_configuration_no_list):
        """Sets the access_control_group_configuration_no_list of this CreateLaunchConfigurationRequest.

        ACG설정번호리스트  # noqa: E501

        :param access_control_group_configuration_no_list: The access_control_group_configuration_no_list of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: list[str]
        """

        self._access_control_group_configuration_no_list = access_control_group_configuration_no_list

    @property
    def login_key_name(self):
        """Gets the login_key_name of this CreateLaunchConfigurationRequest.  # noqa: E501

        로그인키명  # noqa: E501

        :return: The login_key_name of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._login_key_name

    @login_key_name.setter
    def login_key_name(self, login_key_name):
        """Sets the login_key_name of this CreateLaunchConfigurationRequest.

        로그인키명  # noqa: E501

        :param login_key_name: The login_key_name of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._login_key_name = login_key_name

    @property
    def user_data(self):
        """Gets the user_data of this CreateLaunchConfigurationRequest.  # noqa: E501

        사용자데이터  # noqa: E501

        :return: The user_data of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateLaunchConfigurationRequest.

        사용자데이터  # noqa: E501

        :param user_data: The user_data of this CreateLaunchConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def region_no(self):
        """Gets the region_no of this CreateLaunchConfigurationRequest.  # noqa: E501

        리전번호  # noqa: E501

        :return: The region_no of this CreateLaunchConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_no

    @region_no.setter
    def region_no(self, region_no):
        """Sets the region_no of this CreateLaunchConfigurationRequest.

        리전번호  # noqa: E501

        :param region_no: The region_no of this CreateLaunchConfigurationRequest.  # noqa: E501
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
        if not isinstance(other, CreateLaunchConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
