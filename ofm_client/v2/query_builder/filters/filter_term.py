
from __future__ import absolute_import
from ofm_client.v2.query_builder.filters.filter_operators import FilterOperator 
from typing import List


class FilterTerm():
    def __init__(self, field: str, values: List[str], operator: FilterOperator = FilterOperator.IN):
        self._field = field
        self._values = values
        self._operator = operator
        
    @property    
    def field(self)->str:
        return self._field

    @field.setter    
    def field(self, field: str):
        self._field = field

    @property
    def values(self)->List[str]:
        return self._values 
    
    @values.setter
    def values(self, values:List[str]):
        self._values = values      

    @property
    def operator(self)->FilterOperator:
        return self._operator;  
    
    @operator.setter
    def operator(self, operator: FilterOperator):
        self._operator = operator        