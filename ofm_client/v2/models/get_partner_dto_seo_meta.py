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


class GetPartnerDtoSeoMeta(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'product_title': 'str',
        'product_summary': 'str'
    }

    attribute_map = {
        'product_title': 'productTitle',
        'product_summary': 'productSummary'
    }

    def __init__(self, product_title=None, product_summary=None):  # noqa: E501
        """GetPartnerDtoSeoMeta - a model defined in ofm"""  # noqa: E501

        self._product_title = None
        self._product_summary = None
        self.discriminator = None

        if product_title is not None:
            self.product_title = product_title
        if product_summary is not None:
            self.product_summary = product_summary

    @property
    def product_title(self):
        """Gets the product_title of this GetPartnerDtoSeoMeta.  # noqa: E501


        :return: The product_title of this GetPartnerDtoSeoMeta.  # noqa: E501
        :rtype: str
        """
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        """Sets the product_title of this GetPartnerDtoSeoMeta.


        :param product_title: The product_title of this GetPartnerDtoSeoMeta.  # noqa: E501
        :type: str
        """

        self._product_title = product_title

    @property
    def product_summary(self):
        """Gets the product_summary of this GetPartnerDtoSeoMeta.  # noqa: E501


        :return: The product_summary of this GetPartnerDtoSeoMeta.  # noqa: E501
        :rtype: str
        """
        return self._product_summary

    @product_summary.setter
    def product_summary(self, product_summary):
        """Sets the product_summary of this GetPartnerDtoSeoMeta.


        :param product_summary: The product_summary of this GetPartnerDtoSeoMeta.  # noqa: E501
        :type: str
        """

        self._product_summary = product_summary

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
        if issubclass(GetPartnerDtoSeoMeta, dict):
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
        if not isinstance(other, GetPartnerDtoSeoMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
