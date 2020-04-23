# ofm_client.v2.PartnersApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partners_get**](PartnersApi.md#partners_get) | **GET** /partners | Retrieve a collection of Partner records.
[**partners_id_get**](PartnersApi.md#partners_id_get) | **GET** /partners/{id} | Retrieve a specific Partner record.
[**partners_search_post**](PartnersApi.md#partners_search_post) | **POST** /partners/search | Retrieve a collection of Partner records.


# **partners_get**
> list[object] partners_get(limit=limit, page=page)

Retrieve a collection of Partner records.

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
api_instance = ofm_client.v2.PartnersApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Partner records.
    api_response = api_instance.partners_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnersApi->partners_get: %s\n" % e)
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

# **partners_id_get**
> partners_id_get(id)

Retrieve a specific Partner record.

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
api_instance = ofm_client.v2.PartnersApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of a partner record

try:
    # Retrieve a specific Partner record.
    api_instance.partners_id_get(id)
except ApiException as e:
    print("Exception when calling PartnersApi->partners_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of a partner record | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partners_search_post**
> list[object] partners_search_post(body=body)

Retrieve a collection of Partner records.

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
api_instance = ofm_client.v2.PartnersApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostPartnerSearchDto() # PostPartnerSearchDto |  (optional)

try:
    # Retrieve a collection of Partner records.
    api_response = api_instance.partners_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartnersApi->partners_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPartnerSearchDto**](PostPartnerSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

