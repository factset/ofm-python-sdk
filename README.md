# Open:FactSet Marketplace API Client
Headless CMS API used by the Open:FactSet Marketplace.

- API version: v2.1.5
- Package version: 1.0.0
- Build package: io.ofm.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ofm_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ofm_client
from ofm_client.v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = ofm_client.v2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ofm_client.v2.AttributesApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Attribute records.
    api_response = api_instance.attributes_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.factset.com/ofs/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttributesApi* | [**attributes_get**](docs/AttributesApi.md#attributes_get) | **GET** /attributes | Retrieve a collection of Attribute records.
*AttributesApi* | [**attributes_id_get**](docs/AttributesApi.md#attributes_id_get) | **GET** /attributes/{id} | Retrieve a collection of Attribute records.
*AttributesApi* | [**attributes_search_post**](docs/AttributesApi.md#attributes_search_post) | **POST** /attributes/search | Retrieve a collection of Attribute records.
*AttributesGroupsApi* | [**attributes_groups_get**](docs/AttributesGroupsApi.md#attributes_groups_get) | **GET** /attributes/groups | Retrieve a collection of Attributes Group records.
*AttributesGroupsApi* | [**attributes_groups_id_get**](docs/AttributesGroupsApi.md#attributes_groups_id_get) | **GET** /attributes/groups/{id} | Retrieve a specific Attributes Group record.
*AttributesGroupsApi* | [**attributes_groups_search_post**](docs/AttributesGroupsApi.md#attributes_groups_search_post) | **POST** /attributes/groups/search | Retrieve a collection of Attributes Group records.
*AttributesGroupsApi* | [**attributes_groups_used_get**](docs/AttributesGroupsApi.md#attributes_groups_used_get) | **GET** /attributes/groups/used | Retrieve a collection of Attributes Group records in use.
*MediaApi* | [**media_download_namespace_scope_guid_file_name_get**](docs/MediaApi.md#media_download_namespace_scope_guid_file_name_get) | **GET** /media/download/{namespace}/{scope}/{guid}/{fileName} | Retrieve a specific media file
*MediaApi* | [**media_download_namespace_scope_guid_file_name_head**](docs/MediaApi.md#media_download_namespace_scope_guid_file_name_head) | **HEAD** /media/download/{namespace}/{scope}/{guid}/{fileName} | Check the existence and retrieve the headers of a spefic media file
*PartnersApi* | [**partners_get**](docs/PartnersApi.md#partners_get) | **GET** /partners | Retrieve a collection of Partner records.
*PartnersApi* | [**partners_id_get**](docs/PartnersApi.md#partners_id_get) | **GET** /partners/{id} | Retrieve a specific Partner record.
*PartnersApi* | [**partners_search_post**](docs/PartnersApi.md#partners_search_post) | **POST** /partners/search | Retrieve a collection of Partner records.
*ProductsApi* | [**products_get**](docs/ProductsApi.md#products_get) | **GET** /products | Retrieve a collection of Product records.
*ProductsApi* | [**products_id_get**](docs/ProductsApi.md#products_id_get) | **GET** /products/{id} | Retrieve a specific Product record.
*ProductsApi* | [**products_search_post**](docs/ProductsApi.md#products_search_post) | **POST** /products/search | Retrieve a collection of Product records.
*ProductsApi* | [**products_types_get**](docs/ProductsApi.md#products_types_get) | **GET** /products/types | Retrieve a collection of the available Product Types along with the number of published products per type.
*ResourcesApi* | [**resources_get**](docs/ResourcesApi.md#resources_get) | **GET** /resources | Retrieve a collection of Resource records.
*ResourcesApi* | [**resources_id_get**](docs/ResourcesApi.md#resources_id_get) | **GET** /resources/{id} | Retrieve a specific Resource record.
*ResourcesApi* | [**resources_search_post**](docs/ResourcesApi.md#resources_search_post) | **POST** /resources/search | Retrieve a collection of Resource records.
*ResourcesSectionsApi* | [**resources_sections_get**](docs/ResourcesSectionsApi.md#resources_sections_get) | **GET** /resources/sections | Retrieve a collection of Resources Section records.
*ResourcesSectionsApi* | [**resources_sections_id_get**](docs/ResourcesSectionsApi.md#resources_sections_id_get) | **GET** /resources/sections/{id} | Retrieve a specific Resources Section record.
*ResourcesSectionsApi* | [**resources_sections_search_post**](docs/ResourcesSectionsApi.md#resources_sections_search_post) | **POST** /resources/sections/search | Retrieve a collection of Resources Section records.


## Documentation For Models

 - [Document](docs/Document.md)
 - [DocumentSection](docs/DocumentSection.md)
 - [GetAttributeDto](docs/GetAttributeDto.md)
 - [GetAttributesGroupDto](docs/GetAttributesGroupDto.md)
 - [GetAttributesGroupDtoAttributes](docs/GetAttributesGroupDtoAttributes.md)
 - [GetPartnerDto](docs/GetPartnerDto.md)
 - [GetPartnerDtoForumTags](docs/GetPartnerDtoForumTags.md)
 - [GetPartnerDtoSeoMeta](docs/GetPartnerDtoSeoMeta.md)
 - [GetPartnerDtoSocialMedia](docs/GetPartnerDtoSocialMedia.md)
 - [GetPartnerDtoVersionSchema](docs/GetPartnerDtoVersionSchema.md)
 - [GetProductDto](docs/GetProductDto.md)
 - [GetProductDtoAttributes](docs/GetProductDtoAttributes.md)
 - [GetProductDtoAttributesGroups](docs/GetProductDtoAttributesGroups.md)
 - [GetProductDtoColumns](docs/GetProductDtoColumns.md)
 - [GetProductDtoCoverageTable](docs/GetProductDtoCoverageTable.md)
 - [GetProductDtoHighlight](docs/GetProductDtoHighlight.md)
 - [GetProductDtoPartner](docs/GetProductDtoPartner.md)
 - [GetProductDtoPartnerSocialMedia](docs/GetProductDtoPartnerSocialMedia.md)
 - [GetProductDtoPreviewLink](docs/GetProductDtoPreviewLink.md)
 - [GetProductDtoRelatedProducts](docs/GetProductDtoRelatedProducts.md)
 - [GetProductDtoSeoMeta](docs/GetProductDtoSeoMeta.md)
 - [GetProductDtoThirdPartyUrls](docs/GetProductDtoThirdPartyUrls.md)
 - [GetProductDtoVersionSchema](docs/GetProductDtoVersionSchema.md)
 - [GetResourceDto](docs/GetResourceDto.md)
 - [GetResourcesSectionDto](docs/GetResourcesSectionDto.md)
 - [GetResourcesSectionDtoMeta](docs/GetResourcesSectionDtoMeta.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Marking](docs/Marking.md)
 - [PostAttributeSearchDto](docs/PostAttributeSearchDto.md)
 - [PostAttributesGroupSearchDto](docs/PostAttributesGroupSearchDto.md)
 - [PostPartnerSearchDto](docs/PostPartnerSearchDto.md)
 - [PostProductSearchDto](docs/PostProductSearchDto.md)
 - [PostResourceSearchDto](docs/PostResourceSearchDto.md)
 - [PostResourcesSectionSearchDto](docs/PostResourcesSectionSearchDto.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication
