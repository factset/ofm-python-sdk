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


class GetProductDtoColumns(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'title': 'str',
        'field': 'str',
        'align': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'field': 'field',
        'align': 'align',
        'required': 'required'
    }

    def __init__(self, title=None, field=None, align=None, required=None):  # noqa: E501
        """GetProductDtoColumns - a model defined in ofm"""  # noqa: E501

        self._title = None
        self._field = None
        self._align = None
        self._required = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if field is not None:
            self.field = field
        if align is not None:
            self.align = align
        if required is not None:
            self.required = required

    @property
    def title(self):
        """Gets the title of this GetProductDtoColumns.  # noqa: E501


        :return: The title of this GetProductDtoColumns.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetProductDtoColumns.


        :param title: The title of this GetProductDtoColumns.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def field(self):
        """Gets the field of this GetProductDtoColumns.  # noqa: E501


        :return: The field of this GetProductDtoColumns.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this GetProductDtoColumns.


        :param field: The field of this GetProductDtoColumns.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def align(self):
        """Gets the align of this GetProductDtoColumns.  # noqa: E501


        :return: The align of this GetProductDtoColumns.  # noqa: E501
        :rtype: str
        """
        return self._align

    @align.setter
    def align(self, align):
        """Sets the align of this GetProductDtoColumns.


        :param align: The align of this GetProductDtoColumns.  # noqa: E501
        :type: str
        """

        self._align = align

    @property
    def required(self):
        """Gets the required of this GetProductDtoColumns.  # noqa: E501


        :return: The required of this GetProductDtoColumns.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this GetProductDtoColumns.


        :param required: The required of this GetProductDtoColumns.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(GetProductDtoColumns, dict):
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
        if not isinstance(other, GetProductDtoColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
