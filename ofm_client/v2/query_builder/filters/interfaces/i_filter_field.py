from __future__ import annotations,absolute_import
import abc 
from typing import List
import ofm_client.v2.query_builder.filters.interfaces.i_filter as ifilter

class IFilterField(abc.ABC):
    @abc.abstractmethod
    def any_of(self, values: List[str]) -> ifilter.IFilter:
        pass

    @abc.abstractmethod
    def none_of(self, values: List[str]) -> ifilter.IFilter:
        pass
    
    @abc.abstractmethod
    def equals(self, value:str) -> ifilter.IFilter:
        pass
    
    @abc.abstractmethod
    def not_equals(self, value:str) -> ifilter.IFilter:
        pass
