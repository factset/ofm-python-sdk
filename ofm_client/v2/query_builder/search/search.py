from __future__ import absolute_import, annotations
from ofm_client.v2.query_builder.search.interfaces.i_search import ISearch
from ofm_client.v2.query_builder.search.interfaces.i_search_field import ISearchField
from ofm_client.v2.query_builder.search.interfaces.i_search_fields import ISearchFields
from ofm_client.v2.query_builder.search.search_term import SearchTerm

import ofm_client.v2.query_builder.query.interfaces.i_query as iquery

from typing import List


class Search(ISearch, ISearchField, ISearchFields):
    def __init__(self, query: iquery.IQuery):
        self._query = query
        self._prepareField = ''
        self._prepareFields = []

    def field(self, fieldName: str) -> ISearchField:
        self._prepareField = fieldName
        return self

    def fields(self, fieldNames: List[str]) -> ISearchFields:
        self._prepareFields = fieldNames
        return self

    def contain_keywords_prefix(self, value: str) -> ISearch:
        for field in self._prepareFields:
            self._query.searchTerms.append(SearchTerm(field,value))
        return self

    def contains_phrase_prefix(self, value: str) -> ISearch:
        self._query.searchTerms.append(SearchTerm(self._prepareField, '\"'+value+'\"'))
        return self

    @property
    def query(self) -> iquery.IQuery:
        return self._query
            