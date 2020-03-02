from __future__ import annotations, absolute_import
import abc 
import ofm_client.v2.query_builder.search.interfaces

class ISearchFields(abc.ABC):
    @abc.abstractmethod
    def contain_keywords_prefix(self, value: str) -> ofm_client.v2.query_builder.search.interfaces.ISearch:
        pass
    