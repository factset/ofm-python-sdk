from __future__ import absolute_import
import abc 
from typing import List
from ofm_client.v2.query_builder.filters.filter_term import FilterTerm
from ofm_client.v2.query_builder.search.search_term import SearchTerm
from ofm_client.v2.query_builder.sort.sort_term import SortTerm

class IQuery(abc.ABC):
    @property
    def searchTerms(self)->List[SearchTerm]:
        pass  

    @searchTerms.setter
    def searchTerms(self, searchTerms: List[SearchTerm]):
        pass  

    @property
    def filterTerms(self)->List[FilterTerm]:
        pass   

    @filterTerms.setter
    def filterTerms(self, filterTerms: List[FilterTerm]):
        pass

    @property
    def sortTerms(self)->List[SortTerm]:
        pass   

    @sortTerms.setter
    def sortTerms(self, sortTerms: List[SortTerm]):
        pass

    @property
    def limit(self)->int:
        pass

    @limit.setter
    def limit(self, limit: int)->int:
        pass    
        
    @property
    def page(self)->int:
        pass

    @page.setter
    def page(self, page: int)->int:
        pass    
        
    @property
    def fields(self)->List[str]:
        pass

    @fields.setter
    def fields(self, fields: List[str])->List[str]:
        pass    