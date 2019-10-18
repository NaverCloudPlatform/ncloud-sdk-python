# coding: utf-8

"""
    server

    OpenAPI spec version: 2019-01-25T05:09:58Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NasVolumeInstanceRating(object):
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
        'rating_time': 'str',
        'volume_size': 'int',
        'volume_use_size': 'int',
        'volume_use_ratio': 'float',
        'average_volume_size': 'int',
        'average_volume_use_size': 'int',
        'average_volume_use_ratio': 'float',
        'max_volume_use_size': 'int',
        'max_volume_use_ratio': 'float',
        'min_volume_use_size': 'int',
        'min_volume_use_ratio': 'float',
        'snapshot_volume_size': 'int',
        'snapshot_volume_use_size': 'int',
        'snapshot_volume_use_ratio': 'float',
        'snapshot_average_volume_size': 'int',
        'snapshot_average_volume_use_size': 'int',
        'snapshot_average_volume_use_ratio': 'float',
        'snapshot_max_volume_use_size': 'int',
        'snapshot_max_volume_use_ratio': 'float',
        'snapshot_min_volume_use_size': 'int',
        'snapshot_min_volume_use_ratio': 'float'
    }

    attribute_map = {
        'rating_time': 'ratingTime',
        'volume_size': 'volumeSize',
        'volume_use_size': 'volumeUseSize',
        'volume_use_ratio': 'volumeUseRatio',
        'average_volume_size': 'averageVolumeSize',
        'average_volume_use_size': 'averageVolumeUseSize',
        'average_volume_use_ratio': 'averageVolumeUseRatio',
        'max_volume_use_size': 'maxVolumeUseSize',
        'max_volume_use_ratio': 'maxVolumeUseRatio',
        'min_volume_use_size': 'minVolumeUseSize',
        'min_volume_use_ratio': 'minVolumeUseRatio',
        'snapshot_volume_size': 'snapshotVolumeSize',
        'snapshot_volume_use_size': 'snapshotVolumeUseSize',
        'snapshot_volume_use_ratio': 'snapshotVolumeUseRatio',
        'snapshot_average_volume_size': 'snapshotAverageVolumeSize',
        'snapshot_average_volume_use_size': 'snapshotAverageVolumeUseSize',
        'snapshot_average_volume_use_ratio': 'snapshotAverageVolumeUseRatio',
        'snapshot_max_volume_use_size': 'snapshotMaxVolumeUseSize',
        'snapshot_max_volume_use_ratio': 'snapshotMaxVolumeUseRatio',
        'snapshot_min_volume_use_size': 'snapshotMinVolumeUseSize',
        'snapshot_min_volume_use_ratio': 'snapshotMinVolumeUseRatio'
    }

    def __init__(self, rating_time=None, volume_size=None, volume_use_size=None, volume_use_ratio=None, average_volume_size=None, average_volume_use_size=None, average_volume_use_ratio=None, max_volume_use_size=None, max_volume_use_ratio=None, min_volume_use_size=None, min_volume_use_ratio=None, snapshot_volume_size=None, snapshot_volume_use_size=None, snapshot_volume_use_ratio=None, snapshot_average_volume_size=None, snapshot_average_volume_use_size=None, snapshot_average_volume_use_ratio=None, snapshot_max_volume_use_size=None, snapshot_max_volume_use_ratio=None, snapshot_min_volume_use_size=None, snapshot_min_volume_use_ratio=None):  # noqa: E501
        """NasVolumeInstanceRating - a model defined in Swagger"""  # noqa: E501

        self._rating_time = None
        self._volume_size = None
        self._volume_use_size = None
        self._volume_use_ratio = None
        self._average_volume_size = None
        self._average_volume_use_size = None
        self._average_volume_use_ratio = None
        self._max_volume_use_size = None
        self._max_volume_use_ratio = None
        self._min_volume_use_size = None
        self._min_volume_use_ratio = None
        self._snapshot_volume_size = None
        self._snapshot_volume_use_size = None
        self._snapshot_volume_use_ratio = None
        self._snapshot_average_volume_size = None
        self._snapshot_average_volume_use_size = None
        self._snapshot_average_volume_use_ratio = None
        self._snapshot_max_volume_use_size = None
        self._snapshot_max_volume_use_ratio = None
        self._snapshot_min_volume_use_size = None
        self._snapshot_min_volume_use_ratio = None
        self.discriminator = None

        if rating_time is not None:
            self.rating_time = rating_time
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_use_size is not None:
            self.volume_use_size = volume_use_size
        if volume_use_ratio is not None:
            self.volume_use_ratio = volume_use_ratio
        if average_volume_size is not None:
            self.average_volume_size = average_volume_size
        if average_volume_use_size is not None:
            self.average_volume_use_size = average_volume_use_size
        if average_volume_use_ratio is not None:
            self.average_volume_use_ratio = average_volume_use_ratio
        if max_volume_use_size is not None:
            self.max_volume_use_size = max_volume_use_size
        if max_volume_use_ratio is not None:
            self.max_volume_use_ratio = max_volume_use_ratio
        if min_volume_use_size is not None:
            self.min_volume_use_size = min_volume_use_size
        if min_volume_use_ratio is not None:
            self.min_volume_use_ratio = min_volume_use_ratio
        if snapshot_volume_size is not None:
            self.snapshot_volume_size = snapshot_volume_size
        if snapshot_volume_use_size is not None:
            self.snapshot_volume_use_size = snapshot_volume_use_size
        if snapshot_volume_use_ratio is not None:
            self.snapshot_volume_use_ratio = snapshot_volume_use_ratio
        if snapshot_average_volume_size is not None:
            self.snapshot_average_volume_size = snapshot_average_volume_size
        if snapshot_average_volume_use_size is not None:
            self.snapshot_average_volume_use_size = snapshot_average_volume_use_size
        if snapshot_average_volume_use_ratio is not None:
            self.snapshot_average_volume_use_ratio = snapshot_average_volume_use_ratio
        if snapshot_max_volume_use_size is not None:
            self.snapshot_max_volume_use_size = snapshot_max_volume_use_size
        if snapshot_max_volume_use_ratio is not None:
            self.snapshot_max_volume_use_ratio = snapshot_max_volume_use_ratio
        if snapshot_min_volume_use_size is not None:
            self.snapshot_min_volume_use_size = snapshot_min_volume_use_size
        if snapshot_min_volume_use_ratio is not None:
            self.snapshot_min_volume_use_ratio = snapshot_min_volume_use_ratio

    @property
    def rating_time(self):
        """Gets the rating_time of this NasVolumeInstanceRating.  # noqa: E501

        측정시간  # noqa: E501

        :return: The rating_time of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: str
        """
        return self._rating_time

    @rating_time.setter
    def rating_time(self, rating_time):
        """Sets the rating_time of this NasVolumeInstanceRating.

        측정시간  # noqa: E501

        :param rating_time: The rating_time of this NasVolumeInstanceRating.  # noqa: E501
        :type: str
        """

        self._rating_time = rating_time

    @property
    def volume_size(self):
        """Gets the volume_size of this NasVolumeInstanceRating.  # noqa: E501

        볼륨사이즈  # noqa: E501

        :return: The volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this NasVolumeInstanceRating.

        볼륨사이즈  # noqa: E501

        :param volume_size: The volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._volume_size = volume_size

    @property
    def volume_use_size(self):
        """Gets the volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        볼륨사용사이즈  # noqa: E501

        :return: The volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._volume_use_size

    @volume_use_size.setter
    def volume_use_size(self, volume_use_size):
        """Sets the volume_use_size of this NasVolumeInstanceRating.

        볼륨사용사이즈  # noqa: E501

        :param volume_use_size: The volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._volume_use_size = volume_use_size

    @property
    def volume_use_ratio(self):
        """Gets the volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        볼륨사용비율  # noqa: E501

        :return: The volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._volume_use_ratio

    @volume_use_ratio.setter
    def volume_use_ratio(self, volume_use_ratio):
        """Sets the volume_use_ratio of this NasVolumeInstanceRating.

        볼륨사용비율  # noqa: E501

        :param volume_use_ratio: The volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._volume_use_ratio = volume_use_ratio

    @property
    def average_volume_size(self):
        """Gets the average_volume_size of this NasVolumeInstanceRating.  # noqa: E501

        평균볼륨사이즈  # noqa: E501

        :return: The average_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._average_volume_size

    @average_volume_size.setter
    def average_volume_size(self, average_volume_size):
        """Sets the average_volume_size of this NasVolumeInstanceRating.

        평균볼륨사이즈  # noqa: E501

        :param average_volume_size: The average_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._average_volume_size = average_volume_size

    @property
    def average_volume_use_size(self):
        """Gets the average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        평균볼륨사용사이즈  # noqa: E501

        :return: The average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._average_volume_use_size

    @average_volume_use_size.setter
    def average_volume_use_size(self, average_volume_use_size):
        """Sets the average_volume_use_size of this NasVolumeInstanceRating.

        평균볼륨사용사이즈  # noqa: E501

        :param average_volume_use_size: The average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._average_volume_use_size = average_volume_use_size

    @property
    def average_volume_use_ratio(self):
        """Gets the average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        평균볼륨사용비율  # noqa: E501

        :return: The average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._average_volume_use_ratio

    @average_volume_use_ratio.setter
    def average_volume_use_ratio(self, average_volume_use_ratio):
        """Sets the average_volume_use_ratio of this NasVolumeInstanceRating.

        평균볼륨사용비율  # noqa: E501

        :param average_volume_use_ratio: The average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._average_volume_use_ratio = average_volume_use_ratio

    @property
    def max_volume_use_size(self):
        """Gets the max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        최대볼륨사용사이즈  # noqa: E501

        :return: The max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._max_volume_use_size

    @max_volume_use_size.setter
    def max_volume_use_size(self, max_volume_use_size):
        """Sets the max_volume_use_size of this NasVolumeInstanceRating.

        최대볼륨사용사이즈  # noqa: E501

        :param max_volume_use_size: The max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._max_volume_use_size = max_volume_use_size

    @property
    def max_volume_use_ratio(self):
        """Gets the max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        최대볼륨사용비율  # noqa: E501

        :return: The max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._max_volume_use_ratio

    @max_volume_use_ratio.setter
    def max_volume_use_ratio(self, max_volume_use_ratio):
        """Sets the max_volume_use_ratio of this NasVolumeInstanceRating.

        최대볼륨사용비율  # noqa: E501

        :param max_volume_use_ratio: The max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._max_volume_use_ratio = max_volume_use_ratio

    @property
    def min_volume_use_size(self):
        """Gets the min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        최소볼륨사용사이즈  # noqa: E501

        :return: The min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._min_volume_use_size

    @min_volume_use_size.setter
    def min_volume_use_size(self, min_volume_use_size):
        """Sets the min_volume_use_size of this NasVolumeInstanceRating.

        최소볼륨사용사이즈  # noqa: E501

        :param min_volume_use_size: The min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._min_volume_use_size = min_volume_use_size

    @property
    def min_volume_use_ratio(self):
        """Gets the min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        최소볼륨사용비율  # noqa: E501

        :return: The min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._min_volume_use_ratio

    @min_volume_use_ratio.setter
    def min_volume_use_ratio(self, min_volume_use_ratio):
        """Sets the min_volume_use_ratio of this NasVolumeInstanceRating.

        최소볼륨사용비율  # noqa: E501

        :param min_volume_use_ratio: The min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._min_volume_use_ratio = min_volume_use_ratio

    @property
    def snapshot_volume_size(self):
        """Gets the snapshot_volume_size of this NasVolumeInstanceRating.  # noqa: E501

        스냅샷볼륨사이즈  # noqa: E501

        :return: The snapshot_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_volume_size

    @snapshot_volume_size.setter
    def snapshot_volume_size(self, snapshot_volume_size):
        """Sets the snapshot_volume_size of this NasVolumeInstanceRating.

        스냅샷볼륨사이즈  # noqa: E501

        :param snapshot_volume_size: The snapshot_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_volume_size = snapshot_volume_size

    @property
    def snapshot_volume_use_size(self):
        """Gets the snapshot_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        스냅샷볼륨사용사이즈  # noqa: E501

        :return: The snapshot_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_volume_use_size

    @snapshot_volume_use_size.setter
    def snapshot_volume_use_size(self, snapshot_volume_use_size):
        """Sets the snapshot_volume_use_size of this NasVolumeInstanceRating.

        스냅샷볼륨사용사이즈  # noqa: E501

        :param snapshot_volume_use_size: The snapshot_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_volume_use_size = snapshot_volume_use_size

    @property
    def snapshot_volume_use_ratio(self):
        """Gets the snapshot_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        스냅샷볼륨사용비율  # noqa: E501

        :return: The snapshot_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_volume_use_ratio

    @snapshot_volume_use_ratio.setter
    def snapshot_volume_use_ratio(self, snapshot_volume_use_ratio):
        """Sets the snapshot_volume_use_ratio of this NasVolumeInstanceRating.

        스냅샷볼륨사용비율  # noqa: E501

        :param snapshot_volume_use_ratio: The snapshot_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._snapshot_volume_use_ratio = snapshot_volume_use_ratio

    @property
    def snapshot_average_volume_size(self):
        """Gets the snapshot_average_volume_size of this NasVolumeInstanceRating.  # noqa: E501

        평균스냅샷볼륨사이즈  # noqa: E501

        :return: The snapshot_average_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_average_volume_size

    @snapshot_average_volume_size.setter
    def snapshot_average_volume_size(self, snapshot_average_volume_size):
        """Sets the snapshot_average_volume_size of this NasVolumeInstanceRating.

        평균스냅샷볼륨사이즈  # noqa: E501

        :param snapshot_average_volume_size: The snapshot_average_volume_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_average_volume_size = snapshot_average_volume_size

    @property
    def snapshot_average_volume_use_size(self):
        """Gets the snapshot_average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        평균스냅샷볼륨사용사이즈  # noqa: E501

        :return: The snapshot_average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_average_volume_use_size

    @snapshot_average_volume_use_size.setter
    def snapshot_average_volume_use_size(self, snapshot_average_volume_use_size):
        """Sets the snapshot_average_volume_use_size of this NasVolumeInstanceRating.

        평균스냅샷볼륨사용사이즈  # noqa: E501

        :param snapshot_average_volume_use_size: The snapshot_average_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_average_volume_use_size = snapshot_average_volume_use_size

    @property
    def snapshot_average_volume_use_ratio(self):
        """Gets the snapshot_average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        평균스냅샷볼륨사용비율  # noqa: E501

        :return: The snapshot_average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_average_volume_use_ratio

    @snapshot_average_volume_use_ratio.setter
    def snapshot_average_volume_use_ratio(self, snapshot_average_volume_use_ratio):
        """Sets the snapshot_average_volume_use_ratio of this NasVolumeInstanceRating.

        평균스냅샷볼륨사용비율  # noqa: E501

        :param snapshot_average_volume_use_ratio: The snapshot_average_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._snapshot_average_volume_use_ratio = snapshot_average_volume_use_ratio

    @property
    def snapshot_max_volume_use_size(self):
        """Gets the snapshot_max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        최대스냅샷볼륨사용사이즈  # noqa: E501

        :return: The snapshot_max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_max_volume_use_size

    @snapshot_max_volume_use_size.setter
    def snapshot_max_volume_use_size(self, snapshot_max_volume_use_size):
        """Sets the snapshot_max_volume_use_size of this NasVolumeInstanceRating.

        최대스냅샷볼륨사용사이즈  # noqa: E501

        :param snapshot_max_volume_use_size: The snapshot_max_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_max_volume_use_size = snapshot_max_volume_use_size

    @property
    def snapshot_max_volume_use_ratio(self):
        """Gets the snapshot_max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        최대스냅샷볼륨사용비율  # noqa: E501

        :return: The snapshot_max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_max_volume_use_ratio

    @snapshot_max_volume_use_ratio.setter
    def snapshot_max_volume_use_ratio(self, snapshot_max_volume_use_ratio):
        """Sets the snapshot_max_volume_use_ratio of this NasVolumeInstanceRating.

        최대스냅샷볼륨사용비율  # noqa: E501

        :param snapshot_max_volume_use_ratio: The snapshot_max_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._snapshot_max_volume_use_ratio = snapshot_max_volume_use_ratio

    @property
    def snapshot_min_volume_use_size(self):
        """Gets the snapshot_min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501

        최소스냅샷볼륨사용사이즈  # noqa: E501

        :return: The snapshot_min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_min_volume_use_size

    @snapshot_min_volume_use_size.setter
    def snapshot_min_volume_use_size(self, snapshot_min_volume_use_size):
        """Sets the snapshot_min_volume_use_size of this NasVolumeInstanceRating.

        최소스냅샷볼륨사용사이즈  # noqa: E501

        :param snapshot_min_volume_use_size: The snapshot_min_volume_use_size of this NasVolumeInstanceRating.  # noqa: E501
        :type: int
        """

        self._snapshot_min_volume_use_size = snapshot_min_volume_use_size

    @property
    def snapshot_min_volume_use_ratio(self):
        """Gets the snapshot_min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501

        최소스냅샷볼륨사용비율  # noqa: E501

        :return: The snapshot_min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_min_volume_use_ratio

    @snapshot_min_volume_use_ratio.setter
    def snapshot_min_volume_use_ratio(self, snapshot_min_volume_use_ratio):
        """Sets the snapshot_min_volume_use_ratio of this NasVolumeInstanceRating.

        최소스냅샷볼륨사용비율  # noqa: E501

        :param snapshot_min_volume_use_ratio: The snapshot_min_volume_use_ratio of this NasVolumeInstanceRating.  # noqa: E501
        :type: float
        """

        self._snapshot_min_volume_use_ratio = snapshot_min_volume_use_ratio

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
        if not isinstance(other, NasVolumeInstanceRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
