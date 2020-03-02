from __future__ import absolute_import, annotations

import re
import time
from pprint import pprint
from typing import List
from ofm_client.v2.query_builder.query.interfaces.i_query import IQuery
from ofm_client.v2.query_builder.filters.filter_term import FilterTerm
from ofm_client.v2.query_builder.search.search_term import SearchTerm
from ofm_client.v2.query_builder.sort.sort_term import SortTerm


class Query(IQuery):
    def __init__(self):
        self._limit = 10
        self._page = 1
        self._filterTerms = []
        self._searchTerms = []
        self._sortTerms = []
        self._fields = []
        self._sort = []

    @property
    def searchTerms(self)->List[SearchTerm]:
        return self._searchTerms    

    @searchTerms.setter
    def searchTerms(self, searchTerms: List[SearchTerm]):
        self._searchTerms = searchTerms  

    @property
    def filterTerms(self)->List[FilterTerm]:
        return self._filterTerms    

    @filterTerms.setter
    def filterTerms(self, filterTerms: List[FilterTerm]):
        self._filterTerms = filterTerms  

    @property
    def sortTerms(self)->List[SortTerm]:
        return self._sortTerms    

    @sortTerms.setter
    def sortTerms(self, sortTerms: List[SortTerm]):
        self._sortTerms = sortTerms  

    @property
    def limit(self)->int:
        return self._limit

    @limit.setter
    def limit(self, limit: int)->int:
        self._limit = limit    
        
    @property
    def page(self)->int:
        return self._page

    @page.setter
    def page(self, page: int)->int:
        self._page = page    
        
    @property
    def fields(self)->List[str]:
        return self._fields

    @fields.setter
    def fields(self, fields: List[str])->List[str]:
        self._fields = fields    