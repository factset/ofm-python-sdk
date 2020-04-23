# ofm_client.v2.AttributesApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributes_get**](AttributesApi.md#attributes_get) | **GET** /attributes | Retrieve a collection of Attribute records.
[**attributes_id_get**](AttributesApi.md#attributes_id_get) | **GET** /attributes/{id} | Retrieve a collection of Attribute records.
[**attributes_search_post**](AttributesApi.md#attributes_search_post) | **POST** /attributes/search | Retrieve a collection of Attribute records.


# **attributes_get**
> list[object] attributes_get(limit=limit, page=page)

Retrieve a collection of Attribute records.

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

# **attributes_id_get**
> attributes_id_get(id)

Retrieve a collection of Attribute records.

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
api_instance = ofm_client.v2.AttributesApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of an attribute record

try:
    # Retrieve a collection of Attribute records.
    api_instance.attributes_id_get(id)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of an attribute record | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_search_post**
> list[object] attributes_search_post(body=body)

Retrieve a collection of Attribute records.

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
api_instance = ofm_client.v2.AttributesApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostAttributeSearchDto() # PostAttributeSearchDto |  (optional)

try:
    # Retrieve a collection of Attribute records.
    api_response = api_instance.attributes_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->attributes_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAttributeSearchDto**](PostAttributeSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

