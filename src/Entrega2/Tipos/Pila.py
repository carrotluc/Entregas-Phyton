from Entrega2.Tipos.Agregado_Lineal import Agregado_lineal
from typing import TypeVar, Generic

E = TypeVar('E')

class Pila(Agregado_lineal[E], Generic[E]):
    def __init__(self):
        super().__init__()

    @classmethod
    def of(cls) -> 'Pila[E]':
        return cls()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def __str__(self) -> str:
        return f"Pila({', '.join(map(str, self._elements))})"
