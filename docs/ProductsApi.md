# ofm_client.v2.ProductsApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductsApi.md#products_get) | **GET** /products | Retrieve a collection of Product records.
[**products_id_get**](ProductsApi.md#products_id_get) | **GET** /products/{id} | Retrieve a specific Product record.
[**products_search_post**](ProductsApi.md#products_search_post) | **POST** /products/search | Retrieve a collection of Product records.
[**products_types_get**](ProductsApi.md#products_types_get) | **GET** /products/types | Retrieve a collection of the available Product Types along with the number of published products per type.


# **products_get**
> list[object] products_get(limit=limit, page=page)

Retrieve a collection of Product records.

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
api_instance = ofm_client.v2.ProductsApi(ofm_client.v2.ApiClient(configuration))
limit = 10 # int | Limit the amount of records per page (optional) (default to 10)
page = 1 # int | Select which page to show (optional) (default to 1)

try:
    # Retrieve a collection of Product records.
    api_response = api_instance.products_get(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get: %s\n" % e)
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

# **products_id_get**
> GetProductDto products_id_get(id)

Retrieve a specific Product record.

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
api_instance = ofm_client.v2.ProductsApi(ofm_client.v2.ApiClient(configuration))
id = 'id_example' # str | Globally unique identifier (GUID) of a Product record

try:
    # Retrieve a specific Product record.
    api_response = api_instance.products_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Globally unique identifier (GUID) of a Product record | 

### Return type

[**GetProductDto**](GetProductDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_search_post**
> list[object] products_search_post(body=body)

Retrieve a collection of Product records.

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
api_instance = ofm_client.v2.ProductsApi(ofm_client.v2.ApiClient(configuration))
body = ofm_client.v2.PostProductSearchDto() # PostProductSearchDto |  (optional)

try:
    # Retrieve a collection of Product records.
    api_response = api_instance.products_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostProductSearchDto**](PostProductSearchDto.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_types_get**
> list[InlineResponse200] products_types_get()

Retrieve a collection of the available Product Types along with the number of published products per type.

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
api_instance = ofm_client.v2.ProductsApi(ofm_client.v2.ApiClient(configuration))

try:
    # Retrieve a collection of the available Product Types along with the number of published products per type.
    api_response = api_instance.products_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

