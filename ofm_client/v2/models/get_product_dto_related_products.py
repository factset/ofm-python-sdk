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


class GetProductDtoRelatedProducts(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'name': 'str',
        'id': 'str',
        'slug': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'slug': 'slug'
    }

    def __init__(self, name=None, id=None, slug=None):  # noqa: E501
        """GetProductDtoRelatedProducts - a model defined in ofm"""  # noqa: E501

        self._name = None
        self._id = None
        self._slug = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug

    @property
    def name(self):
        """Gets the name of this GetProductDtoRelatedProducts.  # noqa: E501


        :return: The name of this GetProductDtoRelatedProducts.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductDtoRelatedProducts.


        :param name: The name of this GetProductDtoRelatedProducts.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this GetProductDtoRelatedProducts.  # noqa: E501


        :return: The id of this GetProductDtoRelatedProducts.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductDtoRelatedProducts.


        :param id: The id of this GetProductDtoRelatedProducts.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this GetProductDtoRelatedProducts.  # noqa: E501


        :return: The slug of this GetProductDtoRelatedProducts.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GetProductDtoRelatedProducts.


        :param slug: The slug of this GetProductDtoRelatedProducts.  # noqa: E501
        :type: str
        """

        self._slug = slug

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
        if issubclass(GetProductDtoRelatedProducts, dict):
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
        if not isinstance(other, GetProductDtoRelatedProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
