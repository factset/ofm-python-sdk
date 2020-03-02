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

class GetProductDto(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'id': 'str',
        'marking': 'Marking',
        'name': 'str',
        'detail': 'str',
        'date_added': 'int',
        'highlight': 'GetProductDtoHighlight',
        'coverage_table': 'list[GetProductDtoCoverageTable]',
        'video_url': 'str',
        'preview_link': 'GetProductDtoPreviewLink',
        'third_party_urls': 'list[GetProductDtoThirdPartyUrls]',
        'seo_meta': 'GetProductDtoSeoMeta',
        'slug': 'str',
        'product_status_attr': 'str',
        'partner': 'GetProductDtoPartner',
        'related_products': 'list[GetProductDtoRelatedProducts]',
        'documents': 'list[Document]',
        'type': 'list[str]',
        'attributes_groups': 'list[GetProductDtoAttributesGroups]',
        'preview_tags': 'list[GetProductDtoAttributes]',
        'update_frequency': 'str',
        'delivery_frequency': 'str',
        'product_label_override': 'str',
        'created': 'int',
        'updated': 'int',
        'meta': 'list[GetResourcesSectionDtoMeta]',
        'version_schema': 'GetProductDtoVersionSchema'
    }

    attribute_map = {
        'id': 'id',
        'marking': 'marking',
        'name': 'name',
        'detail': 'detail',
        'date_added': 'dateAdded',
        'highlight': 'highlight',
        'coverage_table': 'coverageTable',
        'video_url': 'videoUrl',
        'preview_link': 'previewLink',
        'third_party_urls': 'thirdPartyUrls',
        'seo_meta': 'seoMeta',
        'slug': 'slug',
        'product_status_attr': 'productStatusAttr',
        'partner': 'partner',
        'related_products': 'relatedProducts',
        'documents': 'documents',
        'type': 'type',
        'attributes_groups': 'attributesGroups',
        'preview_tags': 'previewTags',
        'update_frequency': 'updateFrequency',
        'delivery_frequency': 'deliveryFrequency',
        'product_label_override': 'productLabelOverride',
        'created': 'created',
        'updated': 'updated',
        'meta': 'meta',
        'version_schema': 'versionSchema'
    }

    def __init__(self, id=None, marking=None, name=None, detail=None, date_added=None, highlight=None, coverage_table=None, video_url=None, preview_link=None, third_party_urls=None, seo_meta=None, slug=None, product_status_attr=None, partner=None, related_products=None, documents=None, type=None, attributes_groups=None, preview_tags=None, update_frequency=None, delivery_frequency=None, product_label_override=None, created=None, updated=None, meta=None, version_schema=None):  # noqa: E501
        """GetProductDto - a model defined in ofm"""  # noqa: E501
        self._id = None
        self._marking = None
        self._name = None
        self._detail = None
        self._date_added = None
        self._highlight = None
        self._coverage_table = None
        self._video_url = None
        self._preview_link = None
        self._third_party_urls = None
        self._seo_meta = None
        self._slug = None
        self._product_status_attr = None
        self._partner = None
        self._related_products = None
        self._documents = None
        self._type = None
        self._attributes_groups = None
        self._preview_tags = None
        self._update_frequency = None
        self._delivery_frequency = None
        self._product_label_override = None
        self._created = None
        self._updated = None
        self._meta = None
        self._version_schema = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if marking is not None:
            self.marking = marking
        if name is not None:
            self.name = name
        if detail is not None:
            self.detail = detail
        if date_added is not None:
            self.date_added = date_added
        if highlight is not None:
            self.highlight = highlight
        if coverage_table is not None:
            self.coverage_table = coverage_table
        if video_url is not None:
            self.video_url = video_url
        if preview_link is not None:
            self.preview_link = preview_link
        if third_party_urls is not None:
            self.third_party_urls = third_party_urls
        if seo_meta is not None:
            self.seo_meta = seo_meta
        if slug is not None:
            self.slug = slug
        if product_status_attr is not None:
            self.product_status_attr = product_status_attr
        if partner is not None:
            self.partner = partner
        if related_products is not None:
            self.related_products = related_products
        if documents is not None:
            self.documents = documents
        if type is not None:
            self.type = type
        if attributes_groups is not None:
            self.attributes_groups = attributes_groups
        if preview_tags is not None:
            self.preview_tags = preview_tags
        if update_frequency is not None:
            self.update_frequency = update_frequency
        if delivery_frequency is not None:
            self.delivery_frequency = delivery_frequency
        if product_label_override is not None:
            self.product_label_override = product_label_override
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if meta is not None:
            self.meta = meta
        if version_schema is not None:
            self.version_schema = version_schema

    @property
    def id(self):
        """Gets the id of this GetProductDto.  # noqa: E501


        :return: The id of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductDto.


        :param id: The id of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def marking(self):
        """Gets the marking of this GetProductDto.  # noqa: E501


        :return: The marking of this GetProductDto.  # noqa: E501
        :rtype: Marking
        """
        return self._marking

    @marking.setter
    def marking(self, marking):
        """Sets the marking of this GetProductDto.


        :param marking: The marking of this GetProductDto.  # noqa: E501
        :type: Marking
        """

        self._marking = marking

    @property
    def name(self):
        """Gets the name of this GetProductDto.  # noqa: E501


        :return: The name of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductDto.


        :param name: The name of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def detail(self):
        """Gets the detail of this GetProductDto.  # noqa: E501


        :return: The detail of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this GetProductDto.


        :param detail: The detail of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def date_added(self):
        """Gets the date_added of this GetProductDto.  # noqa: E501


        :return: The date_added of this GetProductDto.  # noqa: E501
        :rtype: int
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this GetProductDto.


        :param date_added: The date_added of this GetProductDto.  # noqa: E501
        :type: int
        """

        self._date_added = date_added

    @property
    def highlight(self):
        """Gets the highlight of this GetProductDto.  # noqa: E501


        :return: The highlight of this GetProductDto.  # noqa: E501
        :rtype: GetProductDtoHighlight
        """
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        """Sets the highlight of this GetProductDto.


        :param highlight: The highlight of this GetProductDto.  # noqa: E501
        :type: GetProductDtoHighlight
        """

        self._highlight = highlight

    @property
    def coverage_table(self):
        """Gets the coverage_table of this GetProductDto.  # noqa: E501


        :return: The coverage_table of this GetProductDto.  # noqa: E501
        :rtype: list[GetProductDtoCoverageTable]
        """
        return self._coverage_table

    @coverage_table.setter
    def coverage_table(self, coverage_table):
        """Sets the coverage_table of this GetProductDto.


        :param coverage_table: The coverage_table of this GetProductDto.  # noqa: E501
        :type: list[GetProductDtoCoverageTable]
        """

        self._coverage_table = coverage_table

    @property
    def video_url(self):
        """Gets the video_url of this GetProductDto.  # noqa: E501


        :return: The video_url of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this GetProductDto.


        :param video_url: The video_url of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._video_url = video_url

    @property
    def preview_link(self):
        """Gets the preview_link of this GetProductDto.  # noqa: E501


        :return: The preview_link of this GetProductDto.  # noqa: E501
        :rtype: GetProductDtoPreviewLink
        """
        return self._preview_link

    @preview_link.setter
    def preview_link(self, preview_link):
        """Sets the preview_link of this GetProductDto.


        :param preview_link: The preview_link of this GetProductDto.  # noqa: E501
        :type: GetProductDtoPreviewLink
        """

        self._preview_link = preview_link

    @property
    def third_party_urls(self):
        """Gets the third_party_urls of this GetProductDto.  # noqa: E501


        :return: The third_party_urls of this GetProductDto.  # noqa: E501
        :rtype: list[GetProductDtoThirdPartyUrls]
        """
        return self._third_party_urls

    @third_party_urls.setter
    def third_party_urls(self, third_party_urls):
        """Sets the third_party_urls of this GetProductDto.


        :param third_party_urls: The third_party_urls of this GetProductDto.  # noqa: E501
        :type: list[GetProductDtoThirdPartyUrls]
        """

        self._third_party_urls = third_party_urls

    @property
    def seo_meta(self):
        """Gets the seo_meta of this GetProductDto.  # noqa: E501


        :return: The seo_meta of this GetProductDto.  # noqa: E501
        :rtype: GetProductDtoSeoMeta
        """
        return self._seo_meta

    @seo_meta.setter
    def seo_meta(self, seo_meta):
        """Sets the seo_meta of this GetProductDto.


        :param seo_meta: The seo_meta of this GetProductDto.  # noqa: E501
        :type: GetProductDtoSeoMeta
        """

        self._seo_meta = seo_meta

    @property
    def slug(self):
        """Gets the slug of this GetProductDto.  # noqa: E501


        :return: The slug of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this GetProductDto.


        :param slug: The slug of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def product_status_attr(self):
        """Gets the product_status_attr of this GetProductDto.  # noqa: E501


        :return: The product_status_attr of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._product_status_attr

    @product_status_attr.setter
    def product_status_attr(self, product_status_attr):
        """Sets the product_status_attr of this GetProductDto.


        :param product_status_attr: The product_status_attr of this GetProductDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Coming Soon", "Recently Added", "Candidate", "In queue", "Recently Updated", "Available", "Available for Testing"]  # noqa: E501
        if product_status_attr not in allowed_values:
            raise ValueError(
                "Invalid value for `product_status_attr` ({0}), must be one of {1}"  # noqa: E501
                .format(product_status_attr, allowed_values)
            )

        self._product_status_attr = product_status_attr

    @property
    def partner(self):
        """Gets the partner of this GetProductDto.  # noqa: E501


        :return: The partner of this GetProductDto.  # noqa: E501
        :rtype: GetProductDtoPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this GetProductDto.


        :param partner: The partner of this GetProductDto.  # noqa: E501
        :type: GetProductDtoPartner
        """

        self._partner = partner

    @property
    def related_products(self):
        """Gets the related_products of this GetProductDto.  # noqa: E501


        :return: The related_products of this GetProductDto.  # noqa: E501
        :rtype: list[GetProductDtoRelatedProducts]
        """
        return self._related_products

    @related_products.setter
    def related_products(self, related_products):
        """Sets the related_products of this GetProductDto.


        :param related_products: The related_products of this GetProductDto.  # noqa: E501
        :type: list[GetProductDtoRelatedProducts]
        """

        self._related_products = related_products

    @property
    def documents(self):
        """Gets the documents of this GetProductDto.  # noqa: E501


        :return: The documents of this GetProductDto.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this GetProductDto.


        :param documents: The documents of this GetProductDto.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def type(self):
        """Gets the type of this GetProductDto.  # noqa: E501


        :return: The type of this GetProductDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetProductDto.


        :param type: The type of this GetProductDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Data Feed", "API", "Solution"]  # noqa: E501
        if not set(type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._type = type

    @property
    def attributes_groups(self):
        """Gets the attributes_groups of this GetProductDto.  # noqa: E501


        :return: The attributes_groups of this GetProductDto.  # noqa: E501
        :rtype: list[GetProductDtoAttributesGroups]
        """
        return self._attributes_groups

    @attributes_groups.setter
    def attributes_groups(self, attributes_groups):
        """Sets the attributes_groups of this GetProductDto.


        :param attributes_groups: The attributes_groups of this GetProductDto.  # noqa: E501
        :type: list[GetProductDtoAttributesGroups]
        """

        self._attributes_groups = attributes_groups

    @property
    def preview_tags(self):
        """Gets the preview_tags of this GetProductDto.  # noqa: E501


        :return: The preview_tags of this GetProductDto.  # noqa: E501
        :rtype: list[GetProductDtoAttributes]
        """
        return self._preview_tags

    @preview_tags.setter
    def preview_tags(self, preview_tags):
        """Sets the preview_tags of this GetProductDto.


        :param preview_tags: The preview_tags of this GetProductDto.  # noqa: E501
        :type: list[GetProductDtoAttributes]
        """

        self._preview_tags = preview_tags

    @property
    def update_frequency(self):
        """Gets the update_frequency of this GetProductDto.  # noqa: E501


        :return: The update_frequency of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._update_frequency

    @update_frequency.setter
    def update_frequency(self, update_frequency):
        """Sets the update_frequency of this GetProductDto.


        :param update_frequency: The update_frequency of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._update_frequency = update_frequency

    @property
    def delivery_frequency(self):
        """Gets the delivery_frequency of this GetProductDto.  # noqa: E501


        :return: The delivery_frequency of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._delivery_frequency

    @delivery_frequency.setter
    def delivery_frequency(self, delivery_frequency):
        """Sets the delivery_frequency of this GetProductDto.


        :param delivery_frequency: The delivery_frequency of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._delivery_frequency = delivery_frequency

    @property
    def product_label_override(self):
        """Gets the product_label_override of this GetProductDto.  # noqa: E501


        :return: The product_label_override of this GetProductDto.  # noqa: E501
        :rtype: str
        """
        return self._product_label_override

    @product_label_override.setter
    def product_label_override(self, product_label_override):
        """Sets the product_label_override of this GetProductDto.


        :param product_label_override: The product_label_override of this GetProductDto.  # noqa: E501
        :type: str
        """

        self._product_label_override = product_label_override

    @property
    def created(self):
        """Gets the created of this GetProductDto.  # noqa: E501


        :return: The created of this GetProductDto.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetProductDto.


        :param created: The created of this GetProductDto.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetProductDto.  # noqa: E501


        :return: The updated of this GetProductDto.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetProductDto.


        :param updated: The updated of this GetProductDto.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def meta(self):
        """Gets the meta of this GetProductDto.  # noqa: E501


        :return: The meta of this GetProductDto.  # noqa: E501
        :rtype: list[GetResourcesSectionDtoMeta]
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this GetProductDto.


        :param meta: The meta of this GetProductDto.  # noqa: E501
        :type: list[GetResourcesSectionDtoMeta]
        """

        self._meta = meta

    @property
    def version_schema(self):
        """Gets the version_schema of this GetProductDto.  # noqa: E501


        :return: The version_schema of this GetProductDto.  # noqa: E501
        :rtype: GetProductDtoVersionSchema
        """
        return self._version_schema

    @version_schema.setter
    def version_schema(self, version_schema):
        """Sets the version_schema of this GetProductDto.


        :param version_schema: The version_schema of this GetProductDto.  # noqa: E501
        :type: GetProductDtoVersionSchema
        """

        self._version_schema = version_schema

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
        if issubclass(GetProductDto, dict):
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
        if not isinstance(other, GetProductDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
