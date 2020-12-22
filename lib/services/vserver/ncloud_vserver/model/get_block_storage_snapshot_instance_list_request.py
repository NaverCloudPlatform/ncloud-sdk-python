# coding: utf-8

"""
    vserver

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetBlockStorageSnapshotInstanceListRequest(object):
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
        'block_storage_snapshot_instance_no_list': 'list[str]',
        'original_block_storage_instance_no_list': 'list[str]',
        'block_storage_snapshot_instance_status_code': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'block_storage_snapshot_volume_size': 'int',
        'is_encrypted_original_block_storage_volume': 'bool',
        'block_storage_snapshot_name': 'str',
        'sorted_by': 'str',
        'sorting_order': 'str'
    }

    attribute_map = {
        'region_code': 'regionCode',
        'block_storage_snapshot_instance_no_list': 'blockStorageSnapshotInstanceNoList',
        'original_block_storage_instance_no_list': 'originalBlockStorageInstanceNoList',
        'block_storage_snapshot_instance_status_code': 'blockStorageSnapshotInstanceStatusCode',
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'block_storage_snapshot_volume_size': 'blockStorageSnapshotVolumeSize',
        'is_encrypted_original_block_storage_volume': 'isEncryptedOriginalBlockStorageVolume',
        'block_storage_snapshot_name': 'blockStorageSnapshotName',
        'sorted_by': 'sortedBy',
        'sorting_order': 'sortingOrder'
    }

    def __init__(self, region_code=None, block_storage_snapshot_instance_no_list=None, original_block_storage_instance_no_list=None, block_storage_snapshot_instance_status_code=None, page_no=None, page_size=None, block_storage_snapshot_volume_size=None, is_encrypted_original_block_storage_volume=None, block_storage_snapshot_name=None, sorted_by=None, sorting_order=None):  # noqa: E501
        """GetBlockStorageSnapshotInstanceListRequest - a model defined in Swagger"""  # noqa: E501

        self._region_code = None
        self._block_storage_snapshot_instance_no_list = None
        self._original_block_storage_instance_no_list = None
        self._block_storage_snapshot_instance_status_code = None
        self._page_no = None
        self._page_size = None
        self._block_storage_snapshot_volume_size = None
        self._is_encrypted_original_block_storage_volume = None
        self._block_storage_snapshot_name = None
        self._sorted_by = None
        self._sorting_order = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if block_storage_snapshot_instance_no_list is not None:
            self.block_storage_snapshot_instance_no_list = block_storage_snapshot_instance_no_list
        if original_block_storage_instance_no_list is not None:
            self.original_block_storage_instance_no_list = original_block_storage_instance_no_list
        if block_storage_snapshot_instance_status_code is not None:
            self.block_storage_snapshot_instance_status_code = block_storage_snapshot_instance_status_code
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if block_storage_snapshot_volume_size is not None:
            self.block_storage_snapshot_volume_size = block_storage_snapshot_volume_size
        if is_encrypted_original_block_storage_volume is not None:
            self.is_encrypted_original_block_storage_volume = is_encrypted_original_block_storage_volume
        if block_storage_snapshot_name is not None:
            self.block_storage_snapshot_name = block_storage_snapshot_name
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if sorting_order is not None:
            self.sorting_order = sorting_order

    @property
    def region_code(self):
        """Gets the region_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        REGION코드  # noqa: E501

        :return: The region_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this GetBlockStorageSnapshotInstanceListRequest.

        REGION코드  # noqa: E501

        :param region_code: The region_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def block_storage_snapshot_instance_no_list(self):
        """Gets the block_storage_snapshot_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        블록스토리지스냅샷인스턴스번호리스트  # noqa: E501

        :return: The block_storage_snapshot_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._block_storage_snapshot_instance_no_list

    @block_storage_snapshot_instance_no_list.setter
    def block_storage_snapshot_instance_no_list(self, block_storage_snapshot_instance_no_list):
        """Sets the block_storage_snapshot_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.

        블록스토리지스냅샷인스턴스번호리스트  # noqa: E501

        :param block_storage_snapshot_instance_no_list: The block_storage_snapshot_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._block_storage_snapshot_instance_no_list = block_storage_snapshot_instance_no_list

    @property
    def original_block_storage_instance_no_list(self):
        """Gets the original_block_storage_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        원본블록스토리지인스턴스번호리스트  # noqa: E501

        :return: The original_block_storage_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._original_block_storage_instance_no_list

    @original_block_storage_instance_no_list.setter
    def original_block_storage_instance_no_list(self, original_block_storage_instance_no_list):
        """Sets the original_block_storage_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.

        원본블록스토리지인스턴스번호리스트  # noqa: E501

        :param original_block_storage_instance_no_list: The original_block_storage_instance_no_list of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: list[str]
        """

        self._original_block_storage_instance_no_list = original_block_storage_instance_no_list

    @property
    def block_storage_snapshot_instance_status_code(self):
        """Gets the block_storage_snapshot_instance_status_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        블록스토리지스냅샷인스턴스상태코드  # noqa: E501

        :return: The block_storage_snapshot_instance_status_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_instance_status_code

    @block_storage_snapshot_instance_status_code.setter
    def block_storage_snapshot_instance_status_code(self, block_storage_snapshot_instance_status_code):
        """Sets the block_storage_snapshot_instance_status_code of this GetBlockStorageSnapshotInstanceListRequest.

        블록스토리지스냅샷인스턴스상태코드  # noqa: E501

        :param block_storage_snapshot_instance_status_code: The block_storage_snapshot_instance_status_code of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_instance_status_code = block_storage_snapshot_instance_status_code

    @property
    def page_no(self):
        """Gets the page_no of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        페이지번호  # noqa: E501

        :return: The page_no of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this GetBlockStorageSnapshotInstanceListRequest.

        페이지번호  # noqa: E501

        :param page_no: The page_no of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        페이지사이즈  # noqa: E501

        :return: The page_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetBlockStorageSnapshotInstanceListRequest.

        페이지사이즈  # noqa: E501

        :param page_size: The page_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def block_storage_snapshot_volume_size(self):
        """Gets the block_storage_snapshot_volume_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        블록스토리지스냅샷볼륨사이즈  # noqa: E501

        :return: The block_storage_snapshot_volume_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: int
        """
        return self._block_storage_snapshot_volume_size

    @block_storage_snapshot_volume_size.setter
    def block_storage_snapshot_volume_size(self, block_storage_snapshot_volume_size):
        """Sets the block_storage_snapshot_volume_size of this GetBlockStorageSnapshotInstanceListRequest.

        블록스토리지스냅샷볼륨사이즈  # noqa: E501

        :param block_storage_snapshot_volume_size: The block_storage_snapshot_volume_size of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: int
        """

        self._block_storage_snapshot_volume_size = block_storage_snapshot_volume_size

    @property
    def is_encrypted_original_block_storage_volume(self):
        """Gets the is_encrypted_original_block_storage_volume of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        원본블록스토리지볼륨암호화여부  # noqa: E501

        :return: The is_encrypted_original_block_storage_volume of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted_original_block_storage_volume

    @is_encrypted_original_block_storage_volume.setter
    def is_encrypted_original_block_storage_volume(self, is_encrypted_original_block_storage_volume):
        """Sets the is_encrypted_original_block_storage_volume of this GetBlockStorageSnapshotInstanceListRequest.

        원본블록스토리지볼륨암호화여부  # noqa: E501

        :param is_encrypted_original_block_storage_volume: The is_encrypted_original_block_storage_volume of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: bool
        """

        self._is_encrypted_original_block_storage_volume = is_encrypted_original_block_storage_volume

    @property
    def block_storage_snapshot_name(self):
        """Gets the block_storage_snapshot_name of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        블록스토리지스냅샷이름  # noqa: E501

        :return: The block_storage_snapshot_name of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._block_storage_snapshot_name

    @block_storage_snapshot_name.setter
    def block_storage_snapshot_name(self, block_storage_snapshot_name):
        """Sets the block_storage_snapshot_name of this GetBlockStorageSnapshotInstanceListRequest.

        블록스토리지스냅샷이름  # noqa: E501

        :param block_storage_snapshot_name: The block_storage_snapshot_name of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._block_storage_snapshot_name = block_storage_snapshot_name

    @property
    def sorted_by(self):
        """Gets the sorted_by of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        정렬대상  # noqa: E501

        :return: The sorted_by of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this GetBlockStorageSnapshotInstanceListRequest.

        정렬대상  # noqa: E501

        :param sorted_by: The sorted_by of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def sorting_order(self):
        """Gets the sorting_order of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501

        정렬순서  # noqa: E501

        :return: The sorting_order of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :rtype: str
        """
        return self._sorting_order

    @sorting_order.setter
    def sorting_order(self, sorting_order):
        """Sets the sorting_order of this GetBlockStorageSnapshotInstanceListRequest.

        정렬순서  # noqa: E501

        :param sorting_order: The sorting_order of this GetBlockStorageSnapshotInstanceListRequest.  # noqa: E501
        :type: str
        """

        self._sorting_order = sorting_order

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
        if not isinstance(other, GetBlockStorageSnapshotInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other