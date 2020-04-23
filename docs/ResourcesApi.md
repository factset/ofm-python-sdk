# ofm_client.v2.ResourcesApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_get**](ResourcesApi.md#resources_get) | **GET** /resources | Retrieve a collection of Resource records.
[**resources_id_get**](ResourcesApi.md#resources_id_get) | **GET** /resources/{id} | Retrieve a specific Resource record.
[**resources_search_post**](ResourcesApi.md#resources_search_post) | **POST** /resources/search | Retrieve a collection of Resource records.


# **resources_get**
> list[object] resources_get(limit=limit, page=page)

Retrieve a collection of Resource records.

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
api_instance = ofm_client.v2.ResourcesApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Resource records.
    api_response = api_instance.resources_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_get: %s\n" % e)
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

# **resources_id_get**
> GetResourceDto resources_id_get(id)

Retrieve a specific Resource record.

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
api_instance = ofm_client.v2.ResourcesApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of a Resource record

try:
    # Retrieve a specific Resource record.
    api_response = api_instance.resources_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of a Resource record | 

### Return type

[**GetResourceDto**](GetResourceDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_search_post**
> list[object] resources_search_post(body=body)

Retrieve a collection of Resource records.

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
api_instance = ofm_client.v2.ResourcesApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostResourceSearchDto() # PostResourceSearchDto |  (optional)

try:
    # Retrieve a collection of Resource records.
    api_response = api_instance.resources_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->resources_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostResourceSearchDto**](PostResourceSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

