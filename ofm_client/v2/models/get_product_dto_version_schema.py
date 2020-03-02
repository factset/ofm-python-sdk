# coding: utf-8

"""
    Open:FactSet Marketplace API

    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501

    OpenAPI spec version: v2.1.5
    Contact: openfactset-frontend-engineering@factset.com
    
"""


import pprint
import re  # noqa: F401

import six


class GetProductDtoVersionSchema(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'major': 'int',
        'minor': 'int',
        'patch': 'int',
        'versioned_id': 'str',
        'original_id': 'str'
    }

    attribute_map = {
        'major': 'major',
        'minor': 'minor',
        'patch': 'patch',
        'versioned_id': 'versionedId',
        'original_id': 'originalId'
    }

    def __init__(self, major=None, minor=None, patch=None, versioned_id=None, original_id=None):  # noqa: E501
        """GetProductDtoVersionSchema - a model defined in ofm"""  # noqa: E501

        self._major = None
        self._minor = None
        self._patch = None
        self._versioned_id = None
        self._original_id = None
        self.discriminator = None

        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if patch is not None:
            self.patch = patch
        if versioned_id is not None:
            self.versioned_id = versioned_id
        if original_id is not None:
            self.original_id = original_id

    @property
    def major(self):
        """Gets the major of this GetProductDtoVersionSchema.  # noqa: E501


        :return: The major of this GetProductDtoVersionSchema.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this GetProductDtoVersionSchema.


        :param major: The major of this GetProductDtoVersionSchema.  # noqa: E501
        :type: int
        """

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this GetProductDtoVersionSchema.  # noqa: E501


        :return: The minor of this GetProductDtoVersionSchema.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this GetProductDtoVersionSchema.


        :param minor: The minor of this GetProductDtoVersionSchema.  # noqa: E501
        :type: int
        """

        self._minor = minor

    @property
    def patch(self):
        """Gets the patch of this GetProductDtoVersionSchema.  # noqa: E501


        :return: The patch of this GetProductDtoVersionSchema.  # noqa: E501
        :rtype: int
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        """Sets the patch of this GetProductDtoVersionSchema.


        :param patch: The patch of this GetProductDtoVersionSchema.  # noqa: E501
        :type: int
        """

        self._patch = patch

    @property
    def versioned_id(self):
        """Gets the versioned_id of this GetProductDtoVersionSchema.  # noqa: E501


        :return: The versioned_id of this GetProductDtoVersionSchema.  # noqa: E501
        :rtype: str
        """
        return self._versioned_id

    @versioned_id.setter
    def versioned_id(self, versioned_id):
        """Sets the versioned_id of this GetProductDtoVersionSchema.


        :param versioned_id: The versioned_id of this GetProductDtoVersionSchema.  # noqa: E501
        :type: str
        """

        self._versioned_id = versioned_id

    @property
    def original_id(self):
        """Gets the original_id of this GetProductDtoVersionSchema.  # noqa: E501


        :return: The original_id of this GetProductDtoVersionSchema.  # noqa: E501
        :rtype: str
        """
        return self._original_id

    @original_id.setter
    def original_id(self, original_id):
        """Sets the original_id of this GetProductDtoVersionSchema.


        :param original_id: The original_id of this GetProductDtoVersionSchema.  # noqa: E501
        :type: str
        """

        self._original_id = original_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.ofm_types):
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
        if issubclass(GetProductDtoVersionSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetProductDtoVersionSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
