# ofm_client.v2.MediaApi

All URIs are relative to *https://api.factset.com/ofs/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_download_namespace_scope_guid_file_name_get**](MediaApi.md#media_download_namespace_scope_guid_file_name_get) | **GET** /media/download/{namespace}/{scope}/{guid}/{fileName} | Retrieve a specific media file
[**media_download_namespace_scope_guid_file_name_head**](MediaApi.md#media_download_namespace_scope_guid_file_name_head) | **HEAD** /media/download/{namespace}/{scope}/{guid}/{fileName} | Check the existence and retrieve the headers of a spefic media file


# **media_download_namespace_scope_guid_file_name_get**
> media_download_namespace_scope_guid_file_name_get(namespace, scope, guid, file_name)

Retrieve a specific media file

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
api_instance = ofm_client.v2.MediaApi(ofm_client.v2.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace of the media file
scope = 'scope_example' # str | The scope of the media file
guid = 'guid_example' # str | The GUID of the file being requested
file_name = 'file_name_example' # str | The name you want to show for this file in the uri.

try:
    # Retrieve a specific media file
    api_instance.media_download_namespace_scope_guid_file_name_get(namespace, scope, guid, file_name)
except ApiException as e:
    print("Exception when calling MediaApi->media_download_namespace_scope_guid_file_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace of the media file | 
 **scope** | **str**| The scope of the media file | 
 **guid** | **str**| The GUID of the file being requested | 
 **file_name** | **str**| The name you want to show for this file in the uri. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_download_namespace_scope_guid_file_name_head**
> media_download_namespace_scope_guid_file_name_head(namespace, scope, guid, file_name)

Check the existence and retrieve the headers of a spefic media file

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
api_instance = ofm_client.v2.MediaApi(ofm_client.v2.ApiClient(configuration))
namespace = 'namespace_example' # str | The namespace of the media file
scope = 'scope_example' # str | The scope of the media file
guid = 'guid_example' # str | The GUID of the file being requested
file_name = 'file_name_example' # str | The name you want to show for this file in the uri.

try:
    # Check the existence and retrieve the headers of a spefic media file
    api_instance.media_download_namespace_scope_guid_file_name_head(namespace, scope, guid, file_name)
except ApiException as e:
    print("Exception when calling MediaApi->media_download_namespace_scope_guid_file_name_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The namespace of the media file | 
 **scope** | **str**| The scope of the media file | 
 **guid** | **str**| The GUID of the file being requested | 
 **file_name** | **str**| The name you want to show for this file in the uri. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

