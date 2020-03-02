from __future__ import print_function, absolute_import

import base64
import json
import time
import urllib3

from urllib3._collections import HTTPHeaderDict
from pprint import pprint
from typing import List, Callable

import ofm_client.v2

from ofm_client.v2.rest import ApiException
from ofm_client.v2.query_builder import QueryBuilder
from ofm_client.v2.models import GetProductDto, GetPartnerDto

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure HTTP basic authorization: Basic
configuration = ofm_client.v2.Configuration()
configuration.username = 'username'
configuration.password = 'password'
configuration.verify_ssl = False

# create an instance of the API class
apiClient = ofm_client.v2.ApiClient(configuration)
partnersEndpoint = ofm_client.v2.PartnersApi(apiClient)
productsEndpoint = ofm_client.v2.ProductsApi(apiClient)

try:    # Search within the collection of Product records.

    # Instaciate a QueryBuilder
    query = QueryBuilder()

    # Limit the response results to 5
    query.limit(5)

    # Ask for the first page of the result set
    query.page(1)

    # Limit the reponse fields to name, and firmInfo.
    query.fields(['name','firmInfo'])

    # SEARCHING
    # Add search expressions. 
    # All search expressions are combined with OR. 
    # At least one expression should match per record.

    # SEARCHING for partners with keywords included in any of the fields
    # The following search term searches for non-casesensitive keywords {Factset} in any of the Product fields {name,firmInfo}.
    # The last keyword always acts as a prefix. E.g. stream will match streaming
    query.search().fields(['name', 'firmInfo']).contain_keywords_prefix('Factset')

    # FILTERING
    # Add filter expressions. 
    # All filter expressions are combined with AND. 
    # All of the filter expressions are casesensitive and must match per record.

    # FILTERING for partners where a field is equal wiith value
    query.filters().field('name').equals('FactSet')

    # SORTING
    # Add sort expressions. 
    # All sort expressions are applied in order. 
    
    # Sorting partners by name desc
    query.sort().field('name').asc()

    # Export the request body
    body = query.build()
    
    partners: List[GetPartnerDto]
    statusCode: int
    headers: HTTPHeaderDict
    (partners, statusCode, headers)  =  partnersEndpoint.partners_search_post_with_http_info(body=body)

    pagination: dict = json.loads(headers.get('X-Pagination'))

    print('\n####################### PARTNERS #######################\n')
    print("Total partners:  " + str(pagination['totalCount']))
    print("Total pages:     " + str(pagination['totalPages']))
    print("Current page:    " + str(pagination['currentPage']))
    print("Page size:       " + str(pagination['pageSize']))
    print('\n')
    
    for partner in partners:
        print("Parnter Identifier:  " + partner.id)
        print("Partner name:        " + partner.name)
        print("Description:         " + partner.firm_info)
        print('\n')

    # Get the first two products of all listed partners
    partnerIds = list(map(lambda  x: x.id, partners))

    productsQuery = QueryBuilder()
    productsQuery.limit(2)
    productsQuery.page(1)
    productsQuery.filters().field('partner.id').any_of(partnerIds)
    productsQuery.sort().field('name').asc()

    products: List[GetProductDto] = productsEndpoint.products_search_post(body=productsQuery.build())

    print('\n####################### PRODUCTS of partners (' + ", ".join(partnerIds) + ') #######################\n')
    for product in products:
        print("Product name (types):    " + product.name + ' (' + ", ".join(product.type) + ')')
        print('\n')

except ApiException as e:
    print("Exception when calling PartnersApi->partners_search_post: %s\n" % e)