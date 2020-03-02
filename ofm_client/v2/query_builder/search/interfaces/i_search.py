from __future__ import annotations, absolute_import
from typing import List
import abc 
import ofm_client.v2.query_builder.search.interfaces

class ISearch(abc.ABC):
    @abc.abstractmethod
    def field(self, fieldName: str) -> ofm_client.v2.query_builder.search.interfaces.ISearchField:
        pass
    
    @abc.abstractmethod
    def fields(self, fieldNames: List[str]) -> ofm_client.v2.query_builder.search.interfaces.ISearchFields:
        pass