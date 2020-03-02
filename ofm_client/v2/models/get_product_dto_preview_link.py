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


class GetProductDtoPreviewLink(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'link_url': 'str',
        'link_name': 'str'
    }

    attribute_map = {
        'link_url': 'linkUrl',
        'link_name': 'linkName'
    }

    def __init__(self, link_url=None, link_name=None):  # noqa: E501
        """GetProductDtoPreviewLink - a model defined in ofm"""  # noqa: E501

        self._link_url = None
        self._link_name = None
        self.discriminator = None

        if link_url is not None:
            self.link_url = link_url
        if link_name is not None:
            self.link_name = link_name

    @property
    def link_url(self):
        """Gets the link_url of this GetProductDtoPreviewLink.  # noqa: E501


        :return: The link_url of this GetProductDtoPreviewLink.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this GetProductDtoPreviewLink.


        :param link_url: The link_url of this GetProductDtoPreviewLink.  # noqa: E501
        :type: str
        """

        self._link_url = link_url

    @property
    def link_name(self):
        """Gets the link_name of this GetProductDtoPreviewLink.  # noqa: E501


        :return: The link_name of this GetProductDtoPreviewLink.  # noqa: E501
        :rtype: str
        """
        return self._link_name

    @link_name.setter
    def link_name(self, link_name):
        """Sets the link_name of this GetProductDtoPreviewLink.


        :param link_name: The link_name of this GetProductDtoPreviewLink.  # noqa: E501
        :type: str
        """

        self._link_name = link_name

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
        if issubclass(GetProductDtoPreviewLink, dict):
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
        if not isinstance(other, GetProductDtoPreviewLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
