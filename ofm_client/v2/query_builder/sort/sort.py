from __future__ import absolute_import, annotations
from ofm_client.v2.query_builder.sort.interfaces.i_sort import ISort
from ofm_client.v2.query_builder.sort.interfaces.i_sort_field import ISortField
from ofm_client.v2.query_builder.sort.sort_term import SortTerm
from ofm_client.v2.query_builder.sort.sort_operators import SortOperator

import ofm_client.v2.query_builder.query.interfaces.i_query as iquery


# import ofm_client.v2.query_builder.query.interfaces.i_query as iquery

from typing import List


class Sort(ISort, ISortField):
    def __init__(self, query: iquery.IQuery):
        self._query = query
        self._prepareField = ''

    def field(self, fieldName: str) -> ISortField:
        self._prepareField = fieldName
        return self

    def asc(self) -> ISort:
        self._query.sortTerms.append(SortTerm(self._prepareField,SortOperator.ASC))
        return self

    def desc(self) -> ISort:
        self._query.sortTerms.append(SortTerm(self._prepareField,SortOperator.DESC))
        return self

    @property
    def query(self) -> iquery.IQuery:
        return self._query
            