from __future__ import annotations,absolute_import
import abc 
from typing import List
import ofm_client.v2.query_builder.search.interfaces

class ISearchField(abc.ABC):
    @abc.abstractmethod
    def contains_phrase_prefix(self, value:str) -> ofm_client.v2.query_builder.search.interfaces.ISearch:
        pass
    