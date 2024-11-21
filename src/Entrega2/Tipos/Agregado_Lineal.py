from typing import List, TypeVar, Generic, Optional
from abc import ABC, abstractmethod

E = TypeVar('E')

class Agregado_lineal(ABC, Generic[E]):
    def __init__(self) -> None:
        self._elements: List[E] = []
        
    def elements(self) -> List[E]:
        return self._elements[:]
    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements: List[E] = self._elements[:]
        self._elements.clear()
        return removed_elements