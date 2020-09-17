# coding: utf-8

"""
    vserver

    OpenAPI spec version: 2020-09-17T02:28:03Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_vserver.model.common_code import CommonCode  # noqa: F401,E501


class BlockStorageSnapshotInstance(object):
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
        'block_storage_snapshot_instance_no': 'str',
        'block_storage_snapshot_name': 'str',
        'block_storage_snapshot_volume_size': 'int',
        'original_block_storage_instance_no': 'str',
        'block_storage_snapshot_instance_status': 'CommonCode',
        'block_storage_snapshot_instance_operation': 'CommonCode',
        'block_storage_snapshot_instance_status_name': 'str',
        'create_date': 'str',
        'is_encrypted_original_block_storage_volume': 'bool',
        'block_storage_snapshot_description': 'str'
    }

    attribute_map = {
        'block_storage_snapshot_instance_no': 'blockStorageSnapshotInstanceNo',
        'block_storage_snapshot_name': 'blockStorageSnapshotName',
        'block_storage_snapshot_volume_size': 'blockStorageSnapshotVolumeSize',
        'original_block_storage_instance_no': 'originalBlockStorageInstanceNo',
        'block_storage_snapshot_instance_status': 'blockStorageSnapshotInstanceStatus',
        'block_storage_snapshot_instance_operation': 'blockStorageSnapshotInstanceOperation',
        'block_storage_snapshot_instance_status_name': 'blockStorageSnapshotInstanceStatusName',
        'create_date': 'createDate',
        'is_encrypted_original_block_storage_volume': 'isEncryptedOriginalBlockStorageVolume',
        'block_storage_snapshot_description': 'blockStorageSnapshotDescription'
    }

    def __init__(self, block_storage_snapshot_instance_no=None, block_storage_snapshot_name=None, block_storage_snapshot_volume_size=None, original_block_storage_instance_no=None, block_storage_snapshot_instance_status=None, block_storage_snapshot_instance_operation=None, block_storage_snapshot_instance_status_name=None, create_date=None, is_encrypted_original_block_storage_volume=None, block_storage_snapshot_description=None):  # noqa: E501
        """BlockStorageSnapshotInstance - a model defined in Swagger"""  # noqa: E501

        self._block_storage_snapshot_instance_no = None
        self._block_storage_snapshot_name = None
        self._block_storage_snapshot_volume_size = None
        self._original_block_storage_instance_no = None
        self._block_storage_snapshot_instance_status = None
        self._block_storage_snapshot_instance_operation = None
        self._block_storage_snapshot_instance_status_name = None
        self._create_date = None
        self._is_encrypted_original_block_storage_volume = None
        self._block_storage_snapshot_description = None
        self.discriminator = None

        if block_storage_snapshot_instance_no is not None:
            self.block_storage_snapshot_instance_no = block_storage_snapshot_instance_no
        if block_storage_snapshot_name is not None:
            self.block_storage_snapshot_name = block_storage_snapshot_name
        if block_storage_snapshot_volume_size is not None:
            self.block_storage_snapshot_volume_size = block_storage_snapshot_volume_size
        if original_block_storage_instance_no is not None:
            self.original_block_storage_instance_no = original_block_storage_instance_no
        if block_storage_snapshot_instance_status is not None:
            self.block_storage_snapshot_instance_status = block_storage_snapshot_instance_status
        if block_storage_snapshot_instance_operation is not None:
            self.block_storage_snapshot_instance_operation = block_storage_snapshot_instance_operation
        if block_storage_snapshot_instance_status_name is not None:
            self.block_storage_snapshot_instance_status_name = block_storage_snapshot_instance_status_name
        if create_date is not None:
            self.create_date = create_date
        if is_encrypted_original_block_storage_volume is not None:
            self.is_encrypted_original_block_storage_volume = is_encrypted_original_block_storage_volume
        if block_storage_snapshot_description is not None:
            self.block_storage_snapshot_description = block_storage_snapshot_description

    @property
    def block_storage_snapshot_instance_no(self):
        """Gets the block_storage_snapshot_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷인스턴스번호  # noqa: E501

        :return: The block_storage_snapshot_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_instance_no

    @block_storage_snapshot_instance_no.setter
    def block_storage_snapshot_instance_no(self, block_storage_snapshot_instance_no):
        """Sets the block_storage_snapshot_instance_no of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷인스턴스번호  # noqa: E501

        :param block_storage_snapshot_instance_no: The block_storage_snapshot_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_instance_no = block_storage_snapshot_instance_no

    @property
    def block_storage_snapshot_name(self):
        """Gets the block_storage_snapshot_name of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷이름  # noqa: E501

        :return: The block_storage_snapshot_name of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_name

    @block_storage_snapshot_name.setter
    def block_storage_snapshot_name(self, block_storage_snapshot_name):
        """Sets the block_storage_snapshot_name of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷이름  # noqa: E501

        :param block_storage_snapshot_name: The block_storage_snapshot_name of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_name = block_storage_snapshot_name

    @property
    def block_storage_snapshot_volume_size(self):
        """Gets the block_storage_snapshot_volume_size of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷볼륨사이즈  # noqa: E501

        :return: The block_storage_snapshot_volume_size of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: int
        """
        return self._block_storage_snapshot_volume_size

    @block_storage_snapshot_volume_size.setter
    def block_storage_snapshot_volume_size(self, block_storage_snapshot_volume_size):
        """Sets the block_storage_snapshot_volume_size of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷볼륨사이즈  # noqa: E501

        :param block_storage_snapshot_volume_size: The block_storage_snapshot_volume_size of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: int
        """

        self._block_storage_snapshot_volume_size = block_storage_snapshot_volume_size

    @property
    def original_block_storage_instance_no(self):
        """Gets the original_block_storage_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501

        원본블록스토리지인스턴스번호  # noqa: E501

        :return: The original_block_storage_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._original_block_storage_instance_no

    @original_block_storage_instance_no.setter
    def original_block_storage_instance_no(self, original_block_storage_instance_no):
        """Sets the original_block_storage_instance_no of this BlockStorageSnapshotInstance.

        원본블록스토리지인스턴스번호  # noqa: E501

        :param original_block_storage_instance_no: The original_block_storage_instance_no of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._original_block_storage_instance_no = original_block_storage_instance_no

    @property
    def block_storage_snapshot_instance_status(self):
        """Gets the block_storage_snapshot_instance_status of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷인스턴스상태  # noqa: E501

        :return: The block_storage_snapshot_instance_status of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_snapshot_instance_status

    @block_storage_snapshot_instance_status.setter
    def block_storage_snapshot_instance_status(self, block_storage_snapshot_instance_status):
        """Sets the block_storage_snapshot_instance_status of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷인스턴스상태  # noqa: E501

        :param block_storage_snapshot_instance_status: The block_storage_snapshot_instance_status of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_snapshot_instance_status = block_storage_snapshot_instance_status

    @property
    def block_storage_snapshot_instance_operation(self):
        """Gets the block_storage_snapshot_instance_operation of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷인스턴스OP  # noqa: E501

        :return: The block_storage_snapshot_instance_operation of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._block_storage_snapshot_instance_operation

    @block_storage_snapshot_instance_operation.setter
    def block_storage_snapshot_instance_operation(self, block_storage_snapshot_instance_operation):
        """Sets the block_storage_snapshot_instance_operation of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷인스턴스OP  # noqa: E501

        :param block_storage_snapshot_instance_operation: The block_storage_snapshot_instance_operation of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: CommonCode
        """

        self._block_storage_snapshot_instance_operation = block_storage_snapshot_instance_operation

    @property
    def block_storage_snapshot_instance_status_name(self):
        """Gets the block_storage_snapshot_instance_status_name of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷인스턴스상태이름  # noqa: E501

        :return: The block_storage_snapshot_instance_status_name of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_instance_status_name

    @block_storage_snapshot_instance_status_name.setter
    def block_storage_snapshot_instance_status_name(self, block_storage_snapshot_instance_status_name):
        """Sets the block_storage_snapshot_instance_status_name of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷인스턴스상태이름  # noqa: E501

        :param block_storage_snapshot_instance_status_name: The block_storage_snapshot_instance_status_name of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_instance_status_name = block_storage_snapshot_instance_status_name

    @property
    def create_date(self):
        """Gets the create_date of this BlockStorageSnapshotInstance.  # noqa: E501

        생성일시  # noqa: E501

        :return: The create_date of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this BlockStorageSnapshotInstance.

        생성일시  # noqa: E501

        :param create_date: The create_date of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def is_encrypted_original_block_storage_volume(self):
        """Gets the is_encrypted_original_block_storage_volume of this BlockStorageSnapshotInstance.  # noqa: E501

        원본블록스토리지볼륨암호화여부  # noqa: E501

        :return: The is_encrypted_original_block_storage_volume of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted_original_block_storage_volume

    @is_encrypted_original_block_storage_volume.setter
    def is_encrypted_original_block_storage_volume(self, is_encrypted_original_block_storage_volume):
        """Sets the is_encrypted_original_block_storage_volume of this BlockStorageSnapshotInstance.

        원본블록스토리지볼륨암호화여부  # noqa: E501

        :param is_encrypted_original_block_storage_volume: The is_encrypted_original_block_storage_volume of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: bool
        """

        self._is_encrypted_original_block_storage_volume = is_encrypted_original_block_storage_volume

    @property
    def block_storage_snapshot_description(self):
        """Gets the block_storage_snapshot_description of this BlockStorageSnapshotInstance.  # noqa: E501

        블록스토리지스냅샷설명  # noqa: E501

        :return: The block_storage_snapshot_description of this BlockStorageSnapshotInstance.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_description

    @block_storage_snapshot_description.setter
    def block_storage_snapshot_description(self, block_storage_snapshot_description):
        """Sets the block_storage_snapshot_description of this BlockStorageSnapshotInstance.

        블록스토리지스냅샷설명  # noqa: E501

        :param block_storage_snapshot_description: The block_storage_snapshot_description of this BlockStorageSnapshotInstance.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_description = block_storage_snapshot_description

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
        if not isinstance(other, BlockStorageSnapshotInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
