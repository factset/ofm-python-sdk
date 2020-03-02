from __future__ import absolute_import
from typing import List
from ofm_client.v2.query_builder.sort.sort_operators import SortOperator


class SortTerm:
    def __init__(self, field: str, sorting: SortOperator):
        self._field = field
        self._sorting = sorting
        
    @property    
    def field(self):
        return self._field

    @field.setter    
    def field(self, field: str):
        self._field = field

    @property
    def sorting(self):
        return self._sorting  
    
    @sorting.setter
    def sorting(self, sorting:SortOperator):
        self._sorting = sorting      