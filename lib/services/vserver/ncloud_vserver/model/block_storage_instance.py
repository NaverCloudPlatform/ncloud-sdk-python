# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.common_code import CommonCode  # noqa: F401,E501


class BlockStorageInstance(object):
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
        'block_storage_instance_no': 'str',
        'server_instance_no': 'str',
        'block_storage_name': 'str',
        'block_storage_type': 'CommonCode',
        'block_storage_size': 'int',
        'device_name': 'str',
        'block_storage_product_code': 'str',
        'block_storage_instance_status': 'CommonCode',
        'block_storage_instance_operation': 'CommonCode',
        'block_storage_instance_status_name': 'str',
        'create_date': 'str',
        'block_storage_description': 'str',
        'block_storage_disk_type': 'CommonCode',
        'block_storage_disk_detail_type': 'CommonCode',
        'max_iops_throughput': 'int',
        'is_encrypted_volume': 'bool',
        'zone_code': 'str',
        'region_code': 'str'
    }

    attribute_map = {
        'block_storage_instance_no': 'blockStorageInstanceNo',
        'server_instance_no': 'serverInstanceNo',
        'block_storage_name': 'blockStorageName',
        'block_storage_type': 'blockStorageType',
        'block_storage_size': 'blockStorageSize',
        'device_name': 'deviceName',
        'block_storage_product_code': 'blockStorageProductCode',
        'block_storage_instance_status': 'blockStorageInstanceStatus',
        'block_storage_instance_operation': 'blockStorageInstanceOperation',
        'block_storage_instance_status_name': 'blockStorageInstanceStatusName',
        'create_date': 'createDate',
        'block_storage_description': 'blockStorageDescription',
        'block_storage_disk_type': 'blockStorageDiskType',
        'block_storage_disk_detail_type': 'blockStorageDiskDetailType',
        'max_iops_throughput': 'maxIopsThroughput',
        'is_encrypted_volume': 'isEncryptedVolume',
        'zone_code': 'zoneCode',
        'region_code': 'regionCode'
    }

    def __init__(self, block_storage_instance_no=None, server_instance_no=None, block_storage_name=None, block_storage_type=None, block_storage_size=None, device_name=None, block_storage_product_code=None, block_storage_instance_status=None, block_storage_instance_operation=None, block_storage_instance_status_name=None, create_date=None, block_storage_description=None, block_storage_disk_type=None, block_storage_disk_detail_type=None, max_iops_throughput=None, is_encrypted_volume=None, zone_code=None, region_code=None):  # noqa: E501
        """BlockStorageInstance - a model defined in Swagger"""  # noqa: E501

        self._block_storage_instance_no = None
        self._server_instance_no = None
        self._block_storage_name = None
        self._block_storage_type = None
        self._block_storage_size = None
        self._device_name = None
        self._block_storage_product_code = None
        self._block_storage_instance_status = None
        self._block_storage_instance_operation = None
        self._block_storage_instance_status_name = None
        self._create_date = None
        self._block_storage_description = None
        self._block_storage_disk_type = None
        self._block_storage_disk_detail_type = None
        self._max_iops_throughput = None
        self._is_encrypted_volume = None
        self._zone_code = None
        self._region_code = None
        self.discriminator = None

        if block_storage_instance_no is not None:
            self.block_storage_instance_no = block_storage_instance_no
        if server_instance_no is not None:
            self.server_instance_no = server_instance_no
        if block_storage_name is not None:
            self.block_storage_name = block_storage_name
        if block_storage_type is not None:
            self.block_storage_type = block_storage_type
        if block_storage_size is not None:
            self.block_storage_size = block_storage_size
        if device_name is not None:
            self.device_name = device_name
        if block_storage_product_code is not None:
            self.block_storage_product_code = block_storage_product_code
        if block_storage_instance_status is not None:
            self.block_storage_instance_status = block_storage_instance_status
        if block_storage_instance_operation is not None:
            self.block_storage_instance_operation = block_storage_instance_operation
        if block_storage_instance_status_name is not None:
            self.block_storage_instance_status_name = block_storage_instance_status_name
        if create_date is not None:
            self.create_date = create_date
        if block_storage_description is not None:
            self.block_storage_description = block_storage_description
        if block_storage_disk_type is not None:
            self.block_storage_disk_type = block_storage_disk_type
        if block_storage_disk_detail_type is not None:
            self.block_storage_disk_detail_type = block_storage_disk_detail_type
        if max_iops_throughput is not None:
            self.max_iops_throughput = max_iops_throughput
        if is_encrypted_volume is not None:
            self.is_encrypted_volume = is_encrypted_volume
        if zone_code is not None:
            self.zone_code = zone_code
        if region_code is not None:
            self.region_code = region_code

    @property
    def block_storage_instance_no(self):
        """Gets the block_storage_instance_no of this BlockStorageInstance.  # noqa: E501

        블록스토리지인스턴스번호  # noqa: E501

        :return: The block_storage_instance_no of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_instance_no

    @block_storage_instance_no.setter
    def block_storage_instance_no(self, block_storage_instance_no):
        """Sets the block_storage_instance_no of this BlockStorageInstance.

        블록스토리지인스턴스번호  # noqa: E501

        :param block_storage_instance_no: The block_storage_instance_no of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_instance_no = block_storage_instance_no

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this BlockStorageInstance.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this BlockStorageInstance.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._server_instance_no = server_instance_no

    @property
    def block_storage_name(self):
        """Gets the block_storage_name of this BlockStorageInstance.  # noqa: E501

        블록스토리지이름  # noqa: E501

        :return: The block_storage_name of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_name

    @block_storage_name.setter
    def block_storage_name(self, block_storage_name):
        """Sets the block_storage_name of this BlockStorageInstance.

        블록스토리지이름  # noqa: E501

        :param block_storage_name: The block_storage_name of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_name = block_storage_name

    @property
    def block_storage_type(self):
        """Gets the block_storage_type of this BlockStorageInstance.  # noqa: E501

        블록스토리지유형  # noqa: E501

        :return: The block_storage_type of this BlockStorageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_type

    @block_storage_type.setter
    def block_storage_type(self, block_storage_type):
        """Sets the block_storage_type of this BlockStorageInstance.

        블록스토리지유형  # noqa: E501

        :param block_storage_type: The block_storage_type of this BlockStorageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_type = block_storage_type

    @property
    def block_storage_size(self):
        """Gets the block_storage_size of this BlockStorageInstance.  # noqa: E501

        블록스토리지사이즈  # noqa: E501

        :return: The block_storage_size of this BlockStorageInstance.  # noqa: E501
        :rtype: int
        """
        return self._block_storage_size

    @block_storage_size.setter
    def block_storage_size(self, block_storage_size):
        """Sets the block_storage_size of this BlockStorageInstance.

        블록스토리지사이즈  # noqa: E501

        :param block_storage_size: The block_storage_size of this BlockStorageInstance.  # noqa: E501
        :type: int
        """

        self._block_storage_size = block_storage_size

    @property
    def device_name(self):
        """Gets the device_name of this BlockStorageInstance.  # noqa: E501

        디바이스이름  # noqa: E501

        :return: The device_name of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this BlockStorageInstance.

        디바이스이름  # noqa: E501

        :param device_name: The device_name of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def block_storage_product_code(self):
        """Gets the block_storage_product_code of this BlockStorageInstance.  # noqa: E501

        블록스토리지상품코드  # noqa: E501

        :return: The block_storage_product_code of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_product_code

    @block_storage_product_code.setter
    def block_storage_product_code(self, block_storage_product_code):
        """Sets the block_storage_product_code of this BlockStorageInstance.

        블록스토리지상품코드  # noqa: E501

        :param block_storage_product_code: The block_storage_product_code of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_product_code = block_storage_product_code

    @property
    def block_storage_instance_status(self):
        """Gets the block_storage_instance_status of this BlockStorageInstance.  # noqa: E501

        블록스토리지인스턴스상태  # noqa: E501

        :return: The block_storage_instance_status of this BlockStorageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_instance_status

    @block_storage_instance_status.setter
    def block_storage_instance_status(self, block_storage_instance_status):
        """Sets the block_storage_instance_status of this BlockStorageInstance.

        블록스토리지인스턴스상태  # noqa: E501

        :param block_storage_instance_status: The block_storage_instance_status of this BlockStorageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_instance_status = block_storage_instance_status

    @property
    def block_storage_instance_operation(self):
        """Gets the block_storage_instance_operation of this BlockStorageInstance.  # noqa: E501

        블록스토리지인스턴스OP  # noqa: E501

        :return: The block_storage_instance_operation of this BlockStorageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_instance_operation

    @block_storage_instance_operation.setter
    def block_storage_instance_operation(self, block_storage_instance_operation):
        """Sets the block_storage_instance_operation of this BlockStorageInstance.

        블록스토리지인스턴스OP  # noqa: E501

        :param block_storage_instance_operation: The block_storage_instance_operation of this BlockStorageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_instance_operation = block_storage_instance_operation

    @property
    def block_storage_instance_status_name(self):
        """Gets the block_storage_instance_status_name of this BlockStorageInstance.  # noqa: E501

        블록스토리지인스턴스상태이름  # noqa: E501

        :return: The block_storage_instance_status_name of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_instance_status_name

    @block_storage_instance_status_name.setter
    def block_storage_instance_status_name(self, block_storage_instance_status_name):
        """Sets the block_storage_instance_status_name of this BlockStorageInstance.

        블록스토리지인스턴스상태이름  # noqa: E501

        :param block_storage_instance_status_name: The block_storage_instance_status_name of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_instance_status_name = block_storage_instance_status_name

    @property
    def create_date(self):
        """Gets the create_date of this BlockStorageInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this BlockStorageInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def block_storage_description(self):
        """Gets the block_storage_description of this BlockStorageInstance.  # noqa: E501

        블록스토리지설명  # noqa: E501

        :return: The block_storage_description of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_description

    @block_storage_description.setter
    def block_storage_description(self, block_storage_description):
        """Sets the block_storage_description of this BlockStorageInstance.

        블록스토리지설명  # noqa: E501

        :param block_storage_description: The block_storage_description of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_description = block_storage_description

    @property
    def block_storage_disk_type(self):
        """Gets the block_storage_disk_type of this BlockStorageInstance.  # noqa: E501

        블록스토리지디스크유형  # noqa: E501

        :return: The block_storage_disk_type of this BlockStorageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_disk_type

    @block_storage_disk_type.setter
    def block_storage_disk_type(self, block_storage_disk_type):
        """Sets the block_storage_disk_type of this BlockStorageInstance.

        블록스토리지디스크유형  # noqa: E501

        :param block_storage_disk_type: The block_storage_disk_type of this BlockStorageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_disk_type = block_storage_disk_type

    @property
    def block_storage_disk_detail_type(self):
        """Gets the block_storage_disk_detail_type of this BlockStorageInstance.  # noqa: E501

        블록스토리지디스크상세유형  # noqa: E501

        :return: The block_storage_disk_detail_type of this BlockStorageInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_disk_detail_type

    @block_storage_disk_detail_type.setter
    def block_storage_disk_detail_type(self, block_storage_disk_detail_type):
        """Sets the block_storage_disk_detail_type of this BlockStorageInstance.

        블록스토리지디스크상세유형  # noqa: E501

        :param block_storage_disk_detail_type: The block_storage_disk_detail_type of this BlockStorageInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_disk_detail_type = block_storage_disk_detail_type

    @property
    def max_iops_throughput(self):
        """Gets the max_iops_throughput of this BlockStorageInstance.  # noqa: E501

        최대IOPS  # noqa: E501

        :return: The max_iops_throughput of this BlockStorageInstance.  # noqa: E501
        :rtype: int
        """
        return self._max_iops_throughput

    @max_iops_throughput.setter
    def max_iops_throughput(self, max_iops_throughput):
        """Sets the max_iops_throughput of this BlockStorageInstance.

        최대IOPS  # noqa: E501

        :param max_iops_throughput: The max_iops_throughput of this BlockStorageInstance.  # noqa: E501
        :type: int
        """

        self._max_iops_throughput = max_iops_throughput

    @property
    def is_encrypted_volume(self):
        """Gets the is_encrypted_volume of this BlockStorageInstance.  # noqa: E501

        볼륨암호화여부  # noqa: E501

        :return: The is_encrypted_volume of this BlockStorageInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted_volume

    @is_encrypted_volume.setter
    def is_encrypted_volume(self, is_encrypted_volume):
        """Sets the is_encrypted_volume of this BlockStorageInstance.

        볼륨암호화여부  # noqa: E501

        :param is_encrypted_volume: The is_encrypted_volume of this BlockStorageInstance.  # noqa: E501
        :type: bool
        """

        self._is_encrypted_volume = is_encrypted_volume

    @property
    def zone_code(self):
        """Gets the zone_code of this BlockStorageInstance.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this BlockStorageInstance.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

    @property
    def region_code(self):
        """Gets the region_code of this BlockStorageInstance.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this BlockStorageInstance.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this BlockStorageInstance.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this BlockStorageInstance.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

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
        if not isinstance(other, BlockStorageInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
