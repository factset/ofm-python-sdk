# ofm_client.v2.ResourcesSectionsApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_sections_get**](ResourcesSectionsApi.md#resources_sections_get) | **GET** /resources/sections | Retrieve a collection of Resources Section records.
[**resources_sections_id_get**](ResourcesSectionsApi.md#resources_sections_id_get) | **GET** /resources/sections/{id} | Retrieve a specific Resources Section record.
[**resources_sections_search_post**](ResourcesSectionsApi.md#resources_sections_search_post) | **POST** /resources/sections/search | Retrieve a collection of Resources Section records.


# **resources_sections_get**
> list[object] resources_sections_get(limit=limit, page=page)

Retrieve a collection of Resources Section records.

### Example
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
api_instance = ofm_client.v2.ResourcesSectionsApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Resources Section records.
    api_response = api_instance.resources_sections_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesSectionsApi->resources_sections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the amount of records per page | [optional] [default to 10]
 **page** | **int**| Select which page to show | [optional] [default to 1]

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_sections_id_get**
> GetResourcesSectionDto resources_sections_id_get(id)

Retrieve a specific Resources Section record.

### Example
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
api_instance = ofm_client.v2.ResourcesSectionsApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of a Resources Section record

try:
    # Retrieve a specific Resources Section record.
    api_response = api_instance.resources_sections_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesSectionsApi->resources_sections_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of a Resources Section record | 

### Return type

[**GetResourcesSectionDto**](GetResourcesSectionDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_sections_search_post**
> list[object] resources_sections_search_post(body=body)

Retrieve a collection of Resources Section records.

### Example
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
api_instance = ofm_client.v2.ResourcesSectionsApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostResourcesSectionSearchDto() # PostResourcesSectionSearchDto |  (optional)

try:
    # Retrieve a collection of Resources Section records.
    api_response = api_instance.resources_sections_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesSectionsApi->resources_sections_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostResourcesSectionSearchDto**](PostResourcesSectionSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

