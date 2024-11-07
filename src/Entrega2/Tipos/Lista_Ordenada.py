from Entrega2.Tipos.Agregado_Lineal import Agregado_lineal
from typing import List, Callable, TypeVar, Generic

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()

        self._order = order

    @classmethod
    def of(cls, order: Callable[E, R]) -> 'Lista_ordenada[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        for index, element in enumerate(self._elements):
            if self._order(e) < self._order(element):
                return index
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)