# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateBlockStorageSnapshotInstanceRequest(object):
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
        'block_storage_snapshot_name': 'str',
        'block_storage_snapshot_description': 'str',
        'original_block_storage_instance_no': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'block_storage_snapshot_name': 'blockStorageSnapshotName',
        'block_storage_snapshot_description': 'blockStorageSnapshotDescription',
        'original_block_storage_instance_no': 'originalBlockStorageInstanceNo'
    }

    def __init__(self, region_code=None, block_storage_snapshot_name=None, block_storage_snapshot_description=None, original_block_storage_instance_no=None):  # noqa: E501
        """CreateBlockStorageSnapshotInstanceRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._block_storage_snapshot_name = None
        self._block_storage_snapshot_description = None
        self._original_block_storage_instance_no = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if block_storage_snapshot_name is not None:
            self.block_storage_snapshot_name = block_storage_snapshot_name
        if block_storage_snapshot_description is not None:
            self.block_storage_snapshot_description = block_storage_snapshot_description
        self.original_block_storage_instance_no = original_block_storage_instance_no

    @property
    def region_code(self):
        """Gets the region_code of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this CreateBlockStorageSnapshotInstanceRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def block_storage_snapshot_name(self):
        """Gets the block_storage_snapshot_name of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501

        블록스토리지스냅샷이름  # noqa: E501

        :return: The block_storage_snapshot_name of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_name

    @block_storage_snapshot_name.setter
    def block_storage_snapshot_name(self, block_storage_snapshot_name):
        """Sets the block_storage_snapshot_name of this CreateBlockStorageSnapshotInstanceRequest.

        블록스토리지스냅샷이름  # noqa: E501

        :param block_storage_snapshot_name: The block_storage_snapshot_name of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_name = block_storage_snapshot_name

    @property
    def block_storage_snapshot_description(self):
        """Gets the block_storage_snapshot_description of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501

        블록스토리지스냅샷설명  # noqa: E501

        :return: The block_storage_snapshot_description of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_description

    @block_storage_snapshot_description.setter
    def block_storage_snapshot_description(self, block_storage_snapshot_description):
        """Sets the block_storage_snapshot_description of this CreateBlockStorageSnapshotInstanceRequest.

        블록스토리지스냅샷설명  # noqa: E501

        :param block_storage_snapshot_description: The block_storage_snapshot_description of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_description = block_storage_snapshot_description

    @property
    def original_block_storage_instance_no(self):
        """Gets the original_block_storage_instance_no of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501

        원본블록스토리지인스턴스번호  # noqa: E501

        :return: The original_block_storage_instance_no of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._original_block_storage_instance_no

    @original_block_storage_instance_no.setter
    def original_block_storage_instance_no(self, original_block_storage_instance_no):
        """Sets the original_block_storage_instance_no of this CreateBlockStorageSnapshotInstanceRequest.

        원본블록스토리지인스턴스번호  # noqa: E501

        :param original_block_storage_instance_no: The original_block_storage_instance_no of this CreateBlockStorageSnapshotInstanceRequest.  # noqa: E501
        :type: str
        """
        if original_block_storage_instance_no is None:
            raise ValueError("Invalid value for `original_block_storage_instance_no`, must not be `None`")  # noqa: E501

        self._original_block_storage_instance_no = original_block_storage_instance_no

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
        if not isinstance(other, CreateBlockStorageSnapshotInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
