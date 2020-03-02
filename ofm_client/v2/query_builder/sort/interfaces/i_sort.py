from __future__ import annotations, absolute_import
from typing import List
import abc 
import ofm_client.v2.query_builder.sort.interfaces.i_sort_field as iSortField

class ISort(abc.ABC):
    @abc.abstractmethod
    def field(self, fieldName: str) -> iSortField.ISortField:
        pass