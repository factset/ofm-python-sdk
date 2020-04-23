# ofm_client.v2.AttributesGroupsApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributes_groups_get**](AttributesGroupsApi.md#attributes_groups_get) | **GET** /attributes/groups | Retrieve a collection of Attributes Group records.
[**attributes_groups_id_get**](AttributesGroupsApi.md#attributes_groups_id_get) | **GET** /attributes/groups/{id} | Retrieve a specific Attributes Group record.
[**attributes_groups_search_post**](AttributesGroupsApi.md#attributes_groups_search_post) | **POST** /attributes/groups/search | Retrieve a collection of Attributes Group records.
[**attributes_groups_used_get**](AttributesGroupsApi.md#attributes_groups_used_get) | **GET** /attributes/groups/used | Retrieve a collection of Attributes Group records in use.


# **attributes_groups_get**
> list[object] attributes_groups_get(limit=limit, page=page)

Retrieve a collection of Attributes Group records.

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
api_instance = ofm_client.v2.AttributesGroupsApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Attributes Group records.
    api_response = api_instance.attributes_groups_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesGroupsApi->attributes_groups_get: %s\n" % e)
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

# **attributes_groups_id_get**
> GetAttributesGroupDto attributes_groups_id_get(id)

Retrieve a specific Attributes Group record.

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
api_instance = ofm_client.v2.AttributesGroupsApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of an Attributes Group record

try:
    # Retrieve a specific Attributes Group record.
    api_response = api_instance.attributes_groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesGroupsApi->attributes_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of an Attributes Group record | 

### Return type

[**GetAttributesGroupDto**](GetAttributesGroupDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_groups_search_post**
> list[object] attributes_groups_search_post(body=body)

Retrieve a collection of Attributes Group records.

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
api_instance = ofm_client.v2.AttributesGroupsApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostAttributesGroupSearchDto() # PostAttributesGroupSearchDto |  (optional)

try:
    # Retrieve a collection of Attributes Group records.
    api_response = api_instance.attributes_groups_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesGroupsApi->attributes_groups_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAttributesGroupSearchDto**](PostAttributesGroupSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributes_groups_used_get**
> list[object] attributes_groups_used_get(limit=limit, page=page)

Retrieve a collection of Attributes Group records in use.

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
api_instance = ofm_client.v2.AttributesGroupsApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Attributes Group records in use.
    api_response = api_instance.attributes_groups_used_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesGroupsApi->attributes_groups_used_get: %s\n" % e)
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

