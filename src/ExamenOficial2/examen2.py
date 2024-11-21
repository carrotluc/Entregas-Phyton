from typing import List, TypeVar, Generic, Callable, Optional
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

    def add_all(self, lista: List[E]) -> None:
        for e in lista:
            self.add(e)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements: List[E] = self._elements[:]
        self._elements.clear()
        return removed_elements

    def contains(self, e: E) -> bool:
        return e in self._elements

    def find(self, funcion: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if funcion(element):
                return element
        return None

    def filter(self, funcion: Callable[[E], bool]) -> List[E]:
        return [e for e in self._elements if funcion(e)]

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int) -> None:
        super().__init__()
        self.capacidad: int = capacidad

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena")
        self._elements.append(e)

    def is_full(self) -> bool:
        return len(self._elements) >= self.capacidad

    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite":
        return cls(capacidad)

def pruebas():
    try:
        cola: ColaConLimite[str] = ColaConLimite.of(3)
        cola.add("Tarea 1")
        cola.add("Tarea 2")
        cola.add("Tarea 3")
        print("Cola creada y elementos añadidos correctamente")
    except Exception as e:
        print(f"Error al crear una cola o al añadir elementos. Detalles: {e}")

    try:
        cola.add("Tarea 4")
    except OverflowError:
        pass
    except Exception as e:
        print(f"Se esperaba un OverflowError, pero ocurrió otro error: {e}")

    try:
        assert cola.remove() == "Tarea 1"
        print("Eliminar el primer elemento exitosamente")
    except Exception as e:
        print(f"Hubo un problema al eliminar el elemento 'Tarea 1'. Detalles: {e}")

    try:
        assert cola.size() == 2
        print("El tamaño de la cola es correcto")
    except Exception as e:
        print(f"El tamaño de la cola debería ser 2, pero no lo es. Detalles: {e}")

    try:
        assert cola.contains("Tarea 2")
        print("Elemento 'Tarea 2' encontrado en la cola")
    except Exception as e:
        print(f"El elemento 'Tarea 2' no se encontró en la cola. Detalles: {e}")

    try:
        result = cola.find(lambda x: "Tarea" in x)
        assert result == "Tarea 2"
        print("Elemento 'Tarea 2' encontrado con find")
    except Exception as e:
        print(f"El elemento esperado 'Tarea 2' no fue encontrado. Detalles: {e}")

    try:
        result = cola.filter(lambda x: "3" in x)
        assert result == ["Tarea 3"]
        print("Filtrado de elementos correcto")
    except Exception as e:
        print(f"El filtro no devolvió los resultados esperados. Detalles: {e}")

    try:
        cola.remove()
        cola.remove()
        cola.remove()  
    except AssertionError:
        pass  
    except Exception as e:
        print(f"Se esperaba un AssertionError, pero ocurrió otro error. Detalles: {e}")

if __name__ == "__main__":
    pruebas()
