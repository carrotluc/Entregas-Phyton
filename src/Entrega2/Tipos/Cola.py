from Entrega2.Tipos.Agregado_Lineal import Agregado_lineal
from typing import TypeVar, Generic

E = TypeVar('E')

class Cola(Agregado_lineal[E], Generic[E]):
    def __init__(self):
        super().__init__()

    @classmethod
    def of(cls) -> 'Cola[E]':
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def remove(self) -> E:
        if not self._elements:
            raise IndexError("remove from empty queue")
        return self._elements.pop(0)

    def __str__(self) -> str:
        return f"Cola({', '.join(map(str, self._elements))})"
