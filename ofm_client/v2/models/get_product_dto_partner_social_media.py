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


class GetProductDtoPartnerSocialMedia(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'linkedin': 'str',
        'facebook': 'str',
        'twitter': 'str'
    }

    attribute_map = {
        'linkedin': 'linkedin',
        'facebook': 'facebook',
        'twitter': 'twitter'
    }

    def __init__(self, linkedin=None, facebook=None, twitter=None):  # noqa: E501
        """GetProductDtoPartnerSocialMedia - a model defined in ofm"""  # noqa: E501

        self._linkedin = None
        self._facebook = None
        self._twitter = None
        self.discriminator = None

        if linkedin is not None:
            self.linkedin = linkedin
        if facebook is not None:
            self.facebook = facebook
        if twitter is not None:
            self.twitter = twitter

    @property
    def linkedin(self):
        """Gets the linkedin of this GetProductDtoPartnerSocialMedia.  # noqa: E501


        :return: The linkedin of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """Sets the linkedin of this GetProductDtoPartnerSocialMedia.


        :param linkedin: The linkedin of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :type: str
        """

        self._linkedin = linkedin

    @property
    def facebook(self):
        """Gets the facebook of this GetProductDtoPartnerSocialMedia.  # noqa: E501


        :return: The facebook of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this GetProductDtoPartnerSocialMedia.


        :param facebook: The facebook of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """Gets the twitter of this GetProductDtoPartnerSocialMedia.  # noqa: E501


        :return: The twitter of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this GetProductDtoPartnerSocialMedia.


        :param twitter: The twitter of this GetProductDtoPartnerSocialMedia.  # noqa: E501
        :type: str
        """

        self._twitter = twitter

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
        if issubclass(GetProductDtoPartnerSocialMedia, dict):
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
        if not isinstance(other, GetProductDtoPartnerSocialMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
