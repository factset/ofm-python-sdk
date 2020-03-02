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


class GetResourcesSectionDtoMeta(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'documents_total': 'int',
        'documents_private': 'int'
    }

    attribute_map = {
        'documents_total': 'documentsTotal',
        'documents_private': 'documentsPrivate'
    }

    def __init__(self, documents_total=None, documents_private=None):  # noqa: E501
        """GetResourcesSectionDtoMeta - a model defined in ofm"""  # noqa: E501

        self._documents_total = None
        self._documents_private = None
        self.discriminator = None

        if documents_total is not None:
            self.documents_total = documents_total
        if documents_private is not None:
            self.documents_private = documents_private

    @property
    def documents_total(self):
        """Gets the documents_total of this GetResourcesSectionDtoMeta.  # noqa: E501


        :return: The documents_total of this GetResourcesSectionDtoMeta.  # noqa: E501
        :rtype: int
        """
        return self._documents_total

    @documents_total.setter
    def documents_total(self, documents_total):
        """Sets the documents_total of this GetResourcesSectionDtoMeta.


        :param documents_total: The documents_total of this GetResourcesSectionDtoMeta.  # noqa: E501
        :type: int
        """

        self._documents_total = documents_total

    @property
    def documents_private(self):
        """Gets the documents_private of this GetResourcesSectionDtoMeta.  # noqa: E501


        :return: The documents_private of this GetResourcesSectionDtoMeta.  # noqa: E501
        :rtype: int
        """
        return self._documents_private

    @documents_private.setter
    def documents_private(self, documents_private):
        """Sets the documents_private of this GetResourcesSectionDtoMeta.


        :param documents_private: The documents_private of this GetResourcesSectionDtoMeta.  # noqa: E501
        :type: int
        """

        self._documents_private = documents_private

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
        if issubclass(GetResourcesSectionDtoMeta, dict):
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
        if not isinstance(other, GetResourcesSectionDtoMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
