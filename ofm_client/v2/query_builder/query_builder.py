from __future__ import annotations, absolute_import

import re
from typing import Callable,List

from ofm_client.v2.query_builder.query.query import Query
from ofm_client.v2.query_builder.search.search_term import SearchTerm
from ofm_client.v2.query_builder.filters.filter_term import FilterTerm
from ofm_client.v2.query_builder.filters.filter_operators import FilterOperator
from ofm_client.v2.query_builder.search.search import Search
from ofm_client.v2.query_builder.search.interfaces.i_search import ISearch
from ofm_client.v2.query_builder.filters.filter import Filter
from ofm_client.v2.query_builder.filters.interfaces.i_filter import IFilter
from ofm_client.v2.query_builder.sort.interfaces import ISort
from ofm_client.v2.query_builder.sort import Sort, SortOperator, SortTerm


class QueryBuilder():
    def __init__(self):
        self._query = Query()
        self._filters = Filter(Query())
        self._search = Search(Query())
        self._sort = Sort(Query())

    def limit(self, limit: int) -> QueryBuilder:
        self._query.limit = limit 
        return self
        
    def page(self, page: int) -> QueryBuilder:
        self._query.page = page    
        return self  

    def fields(self, fields: List[str]) -> QueryBuilder:
        self._query.fields = fields    
        return self  

    def search(self)-> ISearch:
        return self._search

    def filters(self) -> IFilter:
        return self._filters    

    def sort(self) -> ISort:
        return self._sort    

    def build(self) -> object:
        body = {}
        body['limit'] = self._query.limit
        body['page'] = self._query.page
        body['fields'] = ','.join(self._query.fields) 

        for filterTerm in self._filters.query.filterTerms:
            self._query.filterTerms.append(filterTerm)     

        for searchTerm in self._search.query.searchTerms:
            self._query.searchTerms.append(searchTerm)    

        for sortTerm in self._sort.query.sortTerms:
            self._query.sortTerms.append(sortTerm)

        normalizeValue: Callable[[str], str] = lambda x: re.sub(',', ',,', re.sub('!', '!!', re.sub(':', '::', x)))

        filterOperator: Callable[[FilterTerm], str] = lambda x: ':' if x.operator == FilterOperator.IN else ':!'
        parseFilterTerms: Callable[[FilterTerm], str] = lambda x: x.field + filterOperator(x) + filterOperator(x).join(map(normalizeValue,x.values))
        
        parseSearchTerms: Callable[[SearchTerm],str] = lambda x: x.field + ':' + normalizeValue(x.value)

        sortOperator: Callable[[SortTerm], str] = lambda x: 'asc' if x.sorting == SortOperator.ASC else 'desc'

        parseSortTerms: Callable[[SortTerm], str] = lambda x: x.field + ':' +  sortOperator(x)

        body['search'] = ','.join(map(parseSearchTerms,self._query.searchTerms))
        body['filter'] = ','.join(map(parseFilterTerms,self._query.filterTerms))
        body['sort'] = ','.join(map(parseSortTerms, self._query._sortTerms))

        return body 

        