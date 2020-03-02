from __future__ import print_function, absolute_import

import base64
import json
import time
import urllib3

from urllib3._collections import HTTPHeaderDict
from pprint import pprint
from typing import List

import ofm_client.v2

from ofm_client.v2.rest import ApiException
from ofm_client.v2.query_builder import QueryBuilder
from ofm_client.v2.models import GetProductDto

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure HTTP basic authorization: Basic
configuration = ofm_client.v2.Configuration()
configuration.username = 'username'
configuration.password = 'password'
configuration.verify_ssl = False

# create an instance of the API class
apiClient = ofm_client.v2.ApiClient(configuration)
productsEndpoint = ofm_client.v2.ProductsApi(apiClient)

try:    # Search within the collection of Product records.

    # Instaciate a QueryBuilder
    query = QueryBuilder()

    # Limit the response results to 5
    query.limit(5)

    # Ask for the first page of the result set
    query.page(1)

    # Limit the reponse fields to name, detail, documents, and partner.name. Field id is always present
    query.fields(['name','detail', 'documents', 'partner.name'])

    # SEARCHING
    # Add search expressions. 
    # All search expressions are combined with OR. 
    # At least one expression should match per record.

    # SEARCHING for products with keywords included in any of the fields
    # The following search term searches for non-casesensitive keywords {Factset,stream} in any of the Product fields {name,detail}.
    # The last keyword always acts as a prefix. E.g. stream will match streaming
    query.search().fields(['name', 'detail']).contain_keywords_prefix('Factset stream')

    # SEARCHING for products where phrase prefix is contained in a field
    # The following search terms search for a phrase within a specified field
    # The last search is not to be found as only one search condition needs to be meet to return a record
    query.search().field('name').contains_phrase_prefix('Data Expl')
    query.search().field('name').contains_phrase_prefix('FactSet Broadcast Streaming')
    query.search().field('name').contains_phrase_prefix('This text is not to be found')

    # FILTERING
    # Add filter expressions. 
    # All filter expressions are combined with AND. 
    # All of the filter expressions are casesensitive and must match per record.

    # FILTERING for products where a field is equal wiith value
    query.filters().field('partner.name').equals('FactSet')

    # FILTERING for products where a field is NOT equal with value
    query.filters().field('name').not_equals('FactSet Broadcast Streaming Exchange DataFeed')

    # FILTERING for products where a field is one of the values
    query.filters().field('name').any_of(['FactSet Streaming Exchange DataFeed', 'Data Exploration'])

    # FILTERING for products where a field is none of the values
    query.filters().field('name').none_of(['Not meant to match', 'Not meant to match as well'])

    # SORTING
    # Add sort expressions. 
    # All sort expressions are applied in order. 
    
    # Sorting products by name desc
    query.sort().field('name').desc()

    # Sorting products by partner.name asc
    query.sort().field('partner.name').asc()

    # Export the request body
    body = query.build()
    
    products: List[GetProductDto]
    statusCode: int
    headers: HTTPHeaderDict
    (products, statusCode, headers) = productsEndpoint.products_search_post_with_http_info(body=body)

    pagination: dict = json.loads(headers.get('X-Pagination'))

    print('\n####################### PRODUCTS #######################\n')
    print("Total products:  " + str(pagination['totalCount']))
    print("Total pages:     " + str(pagination['totalPages']))
    print("Current page:    " + str(pagination['currentPage']))
    print("Page size:       " + str(pagination['pageSize']))
    print('\n')

    for product in products:
        print("Product Identifier:  " + product.id)
        print("Product name:        " + product.name)
        print("Description:         " + product.detail)
        print("Partner name:        " + product.partner.name)
        print('\n')

except ApiException as e:
    print("Exception when calling ProductsApi->products_search_post: %s\n" % e)