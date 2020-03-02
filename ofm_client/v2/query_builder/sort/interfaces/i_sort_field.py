from __future__ import annotations,absolute_import
import abc 
from typing import List
import ofm_client.v2.query_builder.sort.interfaces.i_sort as iSort

class ISortField(abc.ABC):
    @abc.abstractmethod
    def asc(self) -> iSort.ISort:
        pass

    @abc.abstractmethod
    def desc(self) -> iSort.ISort:
        pass
    