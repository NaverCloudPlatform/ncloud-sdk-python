# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateBlockStorageInstanceRequest(object):
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
        'block_storage_name': 'str',
        'block_storage_size': 'int',
        'block_storage_disk_detail_type_code': 'str',
        'block_storage_description': 'str',
        'server_instance_no': 'str',
        'block_storage_snapshot_instance_no': 'str',
        'zone_code': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'block_storage_name': 'blockStorageName',
        'block_storage_size': 'blockStorageSize',
        'block_storage_disk_detail_type_code': 'blockStorageDiskDetailTypeCode',
        'block_storage_description': 'blockStorageDescription',
        'server_instance_no': 'serverInstanceNo',
        'block_storage_snapshot_instance_no': 'blockStorageSnapshotInstanceNo',
        'zone_code': 'zoneCode'
    }

    def __init__(self, region_code=None, block_storage_name=None, block_storage_size=None, block_storage_disk_detail_type_code=None, block_storage_description=None, server_instance_no=None, block_storage_snapshot_instance_no=None, zone_code=None):  # noqa: E501
        """CreateBlockStorageInstanceRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._block_storage_name = None
        self._block_storage_size = None
        self._block_storage_disk_detail_type_code = None
        self._block_storage_description = None
        self._server_instance_no = None
        self._block_storage_snapshot_instance_no = None
        self._zone_code = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if block_storage_name is not None:
            self.block_storage_name = block_storage_name
        self.block_storage_size = block_storage_size
        if block_storage_disk_detail_type_code is not None:
            self.block_storage_disk_detail_type_code = block_storage_disk_detail_type_code
        if block_storage_description is not None:
            self.block_storage_description = block_storage_description
        self.server_instance_no = server_instance_no
        if block_storage_snapshot_instance_no is not None:
            self.block_storage_snapshot_instance_no = block_storage_snapshot_instance_no
        if zone_code is not None:
            self.zone_code = zone_code

    @property
    def region_code(self):
        """Gets the region_code of this CreateBlockStorageInstanceRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateBlockStorageInstanceRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def block_storage_name(self):
        """Gets the block_storage_name of this CreateBlockStorageInstanceRequest.  # noqa: E501

        블록스토리지이름  # noqa: E501

        :return: The block_storage_name of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_name

    @block_storage_name.setter
    def block_storage_name(self, block_storage_name):
        """Sets the block_storage_name of this CreateBlockStorageInstanceRequest.

        블록스토리지이름  # noqa: E501

        :param block_storage_name: The block_storage_name of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_name = block_storage_name

    @property
    def block_storage_size(self):
        """Gets the block_storage_size of this CreateBlockStorageInstanceRequest.  # noqa: E501

        블록스토리지사이즈  # noqa: E501

        :return: The block_storage_size of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._block_storage_size

    @block_storage_size.setter
    def block_storage_size(self, block_storage_size):
        """Sets the block_storage_size of this CreateBlockStorageInstanceRequest.

        블록스토리지사이즈  # noqa: E501

        :param block_storage_size: The block_storage_size of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: int
        """
        if block_storage_size is None:
            raise ValueError("Invalid value for `block_storage_size`, must not be `None`")  # noqa: E501

        self._block_storage_size = block_storage_size

    @property
    def block_storage_disk_detail_type_code(self):
        """Gets the block_storage_disk_detail_type_code of this CreateBlockStorageInstanceRequest.  # noqa: E501

        블록스토리지디스크상세유형코드  # noqa: E501

        :return: The block_storage_disk_detail_type_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_disk_detail_type_code

    @block_storage_disk_detail_type_code.setter
    def block_storage_disk_detail_type_code(self, block_storage_disk_detail_type_code):
        """Sets the block_storage_disk_detail_type_code of this CreateBlockStorageInstanceRequest.

        블록스토리지디스크상세유형코드  # noqa: E501

        :param block_storage_disk_detail_type_code: The block_storage_disk_detail_type_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_disk_detail_type_code = block_storage_disk_detail_type_code

    @property
    def block_storage_description(self):
        """Gets the block_storage_description of this CreateBlockStorageInstanceRequest.  # noqa: E501

        블록스토리지설명  # noqa: E501

        :return: The block_storage_description of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_description

    @block_storage_description.setter
    def block_storage_description(self, block_storage_description):
        """Sets the block_storage_description of this CreateBlockStorageInstanceRequest.

        블록스토리지설명  # noqa: E501

        :param block_storage_description: The block_storage_description of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_description = block_storage_description

    @property
    def server_instance_no(self):
        """Gets the server_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501

        서버인스턴스번호  # noqa: E501

        :return: The server_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_instance_no

    @server_instance_no.setter
    def server_instance_no(self, server_instance_no):
        """Sets the server_instance_no of this CreateBlockStorageInstanceRequest.

        서버인스턴스번호  # noqa: E501

        :param server_instance_no: The server_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """
        if server_instance_no is None:
            raise ValueError("Invalid value for `server_instance_no`, must not be `None`")  # noqa: E501

        self._server_instance_no = server_instance_no

    @property
    def block_storage_snapshot_instance_no(self):
        """Gets the block_storage_snapshot_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501

        블록스토리지스냅샷인스턴스번호  # noqa: E501

        :return: The block_storage_snapshot_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_instance_no

    @block_storage_snapshot_instance_no.setter
    def block_storage_snapshot_instance_no(self, block_storage_snapshot_instance_no):
        """Sets the block_storage_snapshot_instance_no of this CreateBlockStorageInstanceRequest.

        블록스토리지스냅샷인스턴스번호  # noqa: E501

        :param block_storage_snapshot_instance_no: The block_storage_snapshot_instance_no of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_instance_no = block_storage_snapshot_instance_no

    @property
    def zone_code(self):
        """Gets the zone_code of this CreateBlockStorageInstanceRequest.  # noqa: E501

        ZONE코드  # noqa: E501

        :return: The zone_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        """Sets the zone_code of this CreateBlockStorageInstanceRequest.

        ZONE코드  # noqa: E501

        :param zone_code: The zone_code of this CreateBlockStorageInstanceRequest.  # noqa: E501
        :type: str
        """

        self._zone_code = zone_code

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
        if not isinstance(other, CreateBlockStorageInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
