from __future__ import absolute_import
from typing import List


class SearchTerm:
    def __init__(self, field: str, value: str):
        self._field = field
        self._value = value
        
    @property    
    def field(self):
        return self._field

    @field.setter    
    def field(self, field: str):
        self._field = field

    @property
    def value(self):
        return self._value  
    
    @value.setter
    def value(self, value:str):
        self._value = value      