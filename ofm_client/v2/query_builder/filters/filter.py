from __future__ import annotations, absolute_import

from ofm_client.v2.query_builder.filters.interfaces.i_filter import IFilter
from ofm_client.v2.query_builder.filters.interfaces.i_filter_field import IFilterField
from ofm_client.v2.query_builder.filters.filter_term import FilterTerm
from ofm_client.v2.query_builder.filters.filter_operators import FilterOperator

import ofm_client.v2.query_builder.query.interfaces.i_query as iquery

from typing import List

class Filter(IFilter, IFilterField):
    def __init__(self, query: iquery.IQuery):
        self._query = query
        self._prepareField = ''

    def field(self, fieldName: str)->IFilterField:
        self._prepareField = fieldName
        return self

    def any_of(self, values: List[str]) -> IFilter:
        self._query.filterTerms.append(FilterTerm(self._prepareField, values, FilterOperator.IN))
        return self

    def none_of(self, values: List[str]) -> IFilter:
        self._query.filterTerms.append(FilterTerm(self._prepareField, values, FilterOperator.NOT_IN))
        return self
    
    def equals(self, value:str) -> IFilter:
        self._query.filterTerms.append(FilterTerm(self._prepareField, [value], FilterOperator.IN))
        return self
    
    def not_equals(self, value:str) -> IFilter:
        self._query.filterTerms.append(FilterTerm(self._prepareField, [value], FilterOperator.NOT_IN))
        return self

    @property
    def query(self) -> iquery.IQuery:
        return self._query
            