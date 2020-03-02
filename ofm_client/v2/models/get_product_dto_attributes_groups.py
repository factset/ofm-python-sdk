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


class GetProductDtoAttributesGroups(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'id': 'str',
        'attributes': 'list[GetProductDtoAttributes]'
    }

    attribute_map = {
        'id': 'id',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, attributes=None):  # noqa: E501
        """GetProductDtoAttributesGroups - a model defined in ofm"""  # noqa: E501

        self._id = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this GetProductDtoAttributesGroups.  # noqa: E501


        :return: The id of this GetProductDtoAttributesGroups.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductDtoAttributesGroups.


        :param id: The id of this GetProductDtoAttributesGroups.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this GetProductDtoAttributesGroups.  # noqa: E501


        :return: The attributes of this GetProductDtoAttributesGroups.  # noqa: E501
        :rtype: list[GetProductDtoAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GetProductDtoAttributesGroups.


        :param attributes: The attributes of this GetProductDtoAttributesGroups.  # noqa: E501
        :type: list[GetProductDtoAttributes]
        """

        self._attributes = attributes

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
        if issubclass(GetProductDtoAttributesGroups, dict):
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
        if not isinstance(other, GetProductDtoAttributesGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
