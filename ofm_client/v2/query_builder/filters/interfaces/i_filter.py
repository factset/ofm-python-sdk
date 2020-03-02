from __future__ import annotations,absolute_import
import abc 
import ofm_client.v2.query_builder.filters.interfaces.i_filter_field as ifilterfield

class IFilter(abc.ABC):
    @abc.abstractmethod
    def field(self, fieldName: str) -> ifilterfield.IFilterField:
        pass