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


class GetProductDtoThirdPartyUrls(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'link': 'str',
        'name': 'str'
    }

    attribute_map = {
        'link': 'link',
        'name': 'name'
    }

    def __init__(self, link=None, name=None):  # noqa: E501
        """GetProductDtoThirdPartyUrls - a model defined in ofm"""  # noqa: E501

        self._link = None
        self._name = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if name is not None:
            self.name = name

    @property
    def link(self):
        """Gets the link of this GetProductDtoThirdPartyUrls.  # noqa: E501


        :return: The link of this GetProductDtoThirdPartyUrls.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GetProductDtoThirdPartyUrls.


        :param link: The link of this GetProductDtoThirdPartyUrls.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def name(self):
        """Gets the name of this GetProductDtoThirdPartyUrls.  # noqa: E501


        :return: The name of this GetProductDtoThirdPartyUrls.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductDtoThirdPartyUrls.


        :param name: The name of this GetProductDtoThirdPartyUrls.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GetProductDtoThirdPartyUrls, dict):
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
        if not isinstance(other, GetProductDtoThirdPartyUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
