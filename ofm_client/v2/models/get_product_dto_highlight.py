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


class GetProductDtoHighlight(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'point1': 'str',
        'point2': 'str',
        'point3': 'str'
    }

    attribute_map = {
        'point1': 'point1',
        'point2': 'point2',
        'point3': 'point3'
    }

    def __init__(self, point1=None, point2=None, point3=None):  # noqa: E501
        """GetProductDtoHighlight - a model defined in ofm"""  # noqa: E501

        self._point1 = None
        self._point2 = None
        self._point3 = None
        self.discriminator = None

        if point1 is not None:
            self.point1 = point1
        if point2 is not None:
            self.point2 = point2
        if point3 is not None:
            self.point3 = point3

    @property
    def point1(self):
        """Gets the point1 of this GetProductDtoHighlight.  # noqa: E501


        :return: The point1 of this GetProductDtoHighlight.  # noqa: E501
        :rtype: str
        """
        return self._point1

    @point1.setter
    def point1(self, point1):
        """Sets the point1 of this GetProductDtoHighlight.


        :param point1: The point1 of this GetProductDtoHighlight.  # noqa: E501
        :type: str
        """

        self._point1 = point1

    @property
    def point2(self):
        """Gets the point2 of this GetProductDtoHighlight.  # noqa: E501


        :return: The point2 of this GetProductDtoHighlight.  # noqa: E501
        :rtype: str
        """
        return self._point2

    @point2.setter
    def point2(self, point2):
        """Sets the point2 of this GetProductDtoHighlight.


        :param point2: The point2 of this GetProductDtoHighlight.  # noqa: E501
        :type: str
        """

        self._point2 = point2

    @property
    def point3(self):
        """Gets the point3 of this GetProductDtoHighlight.  # noqa: E501


        :return: The point3 of this GetProductDtoHighlight.  # noqa: E501
        :rtype: str
        """
        return self._point3

    @point3.setter
    def point3(self, point3):
        """Sets the point3 of this GetProductDtoHighlight.


        :param point3: The point3 of this GetProductDtoHighlight.  # noqa: E501
        :type: str
        """

        self._point3 = point3

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
        if issubclass(GetProductDtoHighlight, dict):
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
        if not isinstance(other, GetProductDtoHighlight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
