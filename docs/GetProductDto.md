# GetProductDto
Product details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | API product id | [optional] 
**marking** | [**Marking**](Marking.md) | Contains product state | [optional] 
**name** | **str** | Product name | [optional] 
**detail** | **str** | Product description | [optional] 
**date_added** | **int** | Product added date | [optional] 
**highlight** | [**GetProductDtoHighlight**](GetProductDtoHighlight.md) | Product highlight  | [optional] 
**coverage_table** | [**list[GetProductDtoCoverageTable]**](GetProductDtoCoverageTable.md) | Product coverage table | [optional] 
**video_url** | **str** | Product video url | [optional] 
**preview_link** | [**GetProductDtoPreviewLink**](GetProductDtoPreviewLink.md) | Product sample link  | [optional] 
**third_party_urls** | [**list[GetProductDtoThirdPartyUrls]**](GetProductDtoThirdPartyUrls.md) | Product additional research url | [optional] 
**seo_meta** | [**GetProductDtoSeoMeta**](GetProductDtoSeoMeta.md) | Search engine metadata | [optional] 
**slug** | **str** | Product url path identifier  | [optional] 
**product_status_attr** | **str** | Product status | [optional] 
**partner** | [**GetProductDtoPartner**](GetProductDtoPartner.md) | Product partner | [optional] 
**related_products** | [**list[GetProductDtoRelatedProducts]**](GetProductDtoRelatedProducts.md) | Product related products | [optional] 
**documents** | [**list[Document]**](Document.md) | Product documents | [optional] 
**type** | **list[str]** | Product types | [optional] 
**attributes_groups** | [**list[GetProductDtoAttributesGroups]**](GetProductDtoAttributesGroups.md) | Product attributes | [optional] 
**preview_tags** | [**list[GetProductDtoAttributes]**](GetProductDtoAttributes.md) | Product tags visible on catalog | [optional] 
**update_frequency** | **str** | Product update frequency | [optional] 
**delivery_frequency** | **str** | Product delivery frequency | [optional] 
**product_label_override** | **str** | Product provider page text | [optional] 
**created** | **int** | Product create date | [optional] 
**updated** | **int** | Product last update date | [optional] 
**meta** | [**list[GetResourcesSectionDtoMeta]**](GetResourcesSectionDtoMeta.md) | Product  | [optional] 
**version_schema** | [**GetProductDtoVersionSchema**](GetProductDtoVersionSchema.md) | Product version object| [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


