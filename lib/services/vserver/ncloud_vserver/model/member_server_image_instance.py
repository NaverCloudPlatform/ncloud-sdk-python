# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.common_code import CommonCode  # noqa: F401,E501


class MemberServerImageInstance(object):
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
        'member_server_image_instance_no': 'str',
        'member_server_image_name': 'str',
        'member_server_image_description': 'str',
        'original_server_instance_no': 'str',
        'original_server_image_product_code': 'str',
        'member_server_image_instance_status': 'CommonCode',
        'member_server_image_instance_operation': 'CommonCode',
        'member_server_image_instance_status_name': 'str',
        'create_date': 'str',
        'member_server_image_block_storage_total_rows': 'int',
        'member_server_image_block_storage_total_size': 'int'
    }

    attribute_map = {
        'member_server_image_instance_no': 'memberServerImageInstanceNo',
        'member_server_image_name': 'memberServerImageName',
        'member_server_image_description': 'memberServerImageDescription',
        'original_server_instance_no': 'originalServerInstanceNo',
        'original_server_image_product_code': 'originalServerImageProductCode',
        'member_server_image_instance_status': 'memberServerImageInstanceStatus',
        'member_server_image_instance_operation': 'memberServerImageInstanceOperation',
        'member_server_image_instance_status_name': 'memberServerImageInstanceStatusName',
        'create_date': 'createDate',
        'member_server_image_block_storage_total_rows': 'memberServerImageBlockStorageTotalRows',
        'member_server_image_block_storage_total_size': 'memberServerImageBlockStorageTotalSize'
    }

    def __init__(self, member_server_image_instance_no=None, member_server_image_name=None, member_server_image_description=None, original_server_instance_no=None, original_server_image_product_code=None, member_server_image_instance_status=None, member_server_image_instance_operation=None, member_server_image_instance_status_name=None, create_date=None, member_server_image_block_storage_total_rows=None, member_server_image_block_storage_total_size=None):  # noqa: E501
        """MemberServerImageInstance - a model defined in Swagger"""  # noqa: E501

        self._member_server_image_instance_no = None
        self._member_server_image_name = None
        self._member_server_image_description = None
        self._original_server_instance_no = None
        self._original_server_image_product_code = None
        self._member_server_image_instance_status = None
        self._member_server_image_instance_operation = None
        self._member_server_image_instance_status_name = None
        self._create_date = None
        self._member_server_image_block_storage_total_rows = None
        self._member_server_image_block_storage_total_size = None
        self.discriminator = None

        if member_server_image_instance_no is not None:
            self.member_server_image_instance_no = member_server_image_instance_no
        if member_server_image_name is not None:
            self.member_server_image_name = member_server_image_name
        if member_server_image_description is not None:
            self.member_server_image_description = member_server_image_description
        if original_server_instance_no is not None:
            self.original_server_instance_no = original_server_instance_no
        if original_server_image_product_code is not None:
            self.original_server_image_product_code = original_server_image_product_code
        if member_server_image_instance_status is not None:
            self.member_server_image_instance_status = member_server_image_instance_status
        if member_server_image_instance_operation is not None:
            self.member_server_image_instance_operation = member_server_image_instance_operation
        if member_server_image_instance_status_name is not None:
            self.member_server_image_instance_status_name = member_server_image_instance_status_name
        if create_date is not None:
            self.create_date = create_date
        if member_server_image_block_storage_total_rows is not None:
            self.member_server_image_block_storage_total_rows = member_server_image_block_storage_total_rows
        if member_server_image_block_storage_total_size is not None:
            self.member_server_image_block_storage_total_size = member_server_image_block_storage_total_size

    @property
    def member_server_image_instance_no(self):
        """Gets the member_server_image_instance_no of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지인스턴스번호  # noqa: E501

        :return: The member_server_image_instance_no of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_instance_no

    @member_server_image_instance_no.setter
    def member_server_image_instance_no(self, member_server_image_instance_no):
        """Sets the member_server_image_instance_no of this MemberServerImageInstance.

        회원서버이미지인스턴스번호  # noqa: E501

        :param member_server_image_instance_no: The member_server_image_instance_no of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._member_server_image_instance_no = member_server_image_instance_no

    @property
    def member_server_image_name(self):
        """Gets the member_server_image_name of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지이름  # noqa: E501

        :return: The member_server_image_name of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_name

    @member_server_image_name.setter
    def member_server_image_name(self, member_server_image_name):
        """Sets the member_server_image_name of this MemberServerImageInstance.

        회원서버이미지이름  # noqa: E501

        :param member_server_image_name: The member_server_image_name of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._member_server_image_name = member_server_image_name

    @property
    def member_server_image_description(self):
        """Gets the member_server_image_description of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지설명  # noqa: E501

        :return: The member_server_image_description of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_description

    @member_server_image_description.setter
    def member_server_image_description(self, member_server_image_description):
        """Sets the member_server_image_description of this MemberServerImageInstance.

        회원서버이미지설명  # noqa: E501

        :param member_server_image_description: The member_server_image_description of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._member_server_image_description = member_server_image_description

    @property
    def original_server_instance_no(self):
        """Gets the original_server_instance_no of this MemberServerImageInstance.  # noqa: E501

        원본서버인스턴스번호  # noqa: E501

        :return: The original_server_instance_no of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._original_server_instance_no

    @original_server_instance_no.setter
    def original_server_instance_no(self, original_server_instance_no):
        """Sets the original_server_instance_no of this MemberServerImageInstance.

        원본서버인스턴스번호  # noqa: E501

        :param original_server_instance_no: The original_server_instance_no of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._original_server_instance_no = original_server_instance_no

    @property
    def original_server_image_product_code(self):
        """Gets the original_server_image_product_code of this MemberServerImageInstance.  # noqa: E501

        원본서버이미지상품코드  # noqa: E501

        :return: The original_server_image_product_code of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._original_server_image_product_code

    @original_server_image_product_code.setter
    def original_server_image_product_code(self, original_server_image_product_code):
        """Sets the original_server_image_product_code of this MemberServerImageInstance.

        원본서버이미지상품코드  # noqa: E501

        :param original_server_image_product_code: The original_server_image_product_code of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._original_server_image_product_code = original_server_image_product_code

    @property
    def member_server_image_instance_status(self):
        """Gets the member_server_image_instance_status of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지인스턴스상태  # noqa: E501

        :return: The member_server_image_instance_status of this MemberServerImageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._member_server_image_instance_status

    @member_server_image_instance_status.setter
    def member_server_image_instance_status(self, member_server_image_instance_status):
        """Sets the member_server_image_instance_status of this MemberServerImageInstance.

        회원서버이미지인스턴스상태  # noqa: E501

        :param member_server_image_instance_status: The member_server_image_instance_status of this MemberServerImageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._member_server_image_instance_status = member_server_image_instance_status

    @property
    def member_server_image_instance_operation(self):
        """Gets the member_server_image_instance_operation of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지인스턴스OP  # noqa: E501

        :return: The member_server_image_instance_operation of this MemberServerImageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._member_server_image_instance_operation

    @member_server_image_instance_operation.setter
    def member_server_image_instance_operation(self, member_server_image_instance_operation):
        """Sets the member_server_image_instance_operation of this MemberServerImageInstance.

        회원서버이미지인스턴스OP  # noqa: E501

        :param member_server_image_instance_operation: The member_server_image_instance_operation of this MemberServerImageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._member_server_image_instance_operation = member_server_image_instance_operation

    @property
    def member_server_image_instance_status_name(self):
        """Gets the member_server_image_instance_status_name of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지인스턴스상태이름  # noqa: E501

        :return: The member_server_image_instance_status_name of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._member_server_image_instance_status_name

    @member_server_image_instance_status_name.setter
    def member_server_image_instance_status_name(self, member_server_image_instance_status_name):
        """Sets the member_server_image_instance_status_name of this MemberServerImageInstance.

        회원서버이미지인스턴스상태이름  # noqa: E501

        :param member_server_image_instance_status_name: The member_server_image_instance_status_name of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._member_server_image_instance_status_name = member_server_image_instance_status_name

    @property
    def create_date(self):
        """Gets the create_date of this MemberServerImageInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this MemberServerImageInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this MemberServerImageInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this MemberServerImageInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def member_server_image_block_storage_total_rows(self):
        """Gets the member_server_image_block_storage_total_rows of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지블록스토리지총개수  # noqa: E501

        :return: The member_server_image_block_storage_total_rows of this MemberServerImageInstance.  # noqa: E501
        :rtype: int
        """
        return self._member_server_image_block_storage_total_rows

    @member_server_image_block_storage_total_rows.setter
    def member_server_image_block_storage_total_rows(self, member_server_image_block_storage_total_rows):
        """Sets the member_server_image_block_storage_total_rows of this MemberServerImageInstance.

        회원서버이미지블록스토리지총개수  # noqa: E501

        :param member_server_image_block_storage_total_rows: The member_server_image_block_storage_total_rows of this MemberServerImageInstance.  # noqa: E501
        :type: int
        """

        self._member_server_image_block_storage_total_rows = member_server_image_block_storage_total_rows

    @property
    def member_server_image_block_storage_total_size(self):
        """Gets the member_server_image_block_storage_total_size of this MemberServerImageInstance.  # noqa: E501

        회원서버이미지블록스토리지총사이즈  # noqa: E501

        :return: The member_server_image_block_storage_total_size of this MemberServerImageInstance.  # noqa: E501
        :rtype: int
        """
        return self._member_server_image_block_storage_total_size

    @member_server_image_block_storage_total_size.setter
    def member_server_image_block_storage_total_size(self, member_server_image_block_storage_total_size):
        """Sets the member_server_image_block_storage_total_size of this MemberServerImageInstance.

        회원서버이미지블록스토리지총사이즈  # noqa: E501

        :param member_server_image_block_storage_total_size: The member_server_image_block_storage_total_size of this MemberServerImageInstance.  # noqa: E501
        :type: int
        """

        self._member_server_image_block_storage_total_size = member_server_image_block_storage_total_size

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
        if not isinstance(other, MemberServerImageInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
