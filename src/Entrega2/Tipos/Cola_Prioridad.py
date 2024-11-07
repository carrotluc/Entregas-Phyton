from typing import List, TypeVar, Generic, Tuple

E = TypeVar('E')
P = TypeVar('P')

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []

    @classmethod
    def of(cls) -> 'Cola_de_prioridad[E, P]':
        return cls()
    
    def elements(self) -> List[E]:
        return self._elements
    
    def priorities(self) -> List[P]:
        return self._priorities

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements

    def __index_order(self, priority: P) -> int:
        for index, p in enumerate(self._priorities):
            if priority < p:
                return index
        return len(self._priorities)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        for index, (element, priority) in enumerate(zip(self._elements, self._priorities)):
            if element == e:
                if new_priority < priority:
                    self._elements.pop(index)
                    self._priorities.pop(index)
                    self.add(e, new_priority)
                break

    def __str__(self) -> str:
        return f"ColaPrioridad({', '.join([f'({e}, {p})' for e, p in zip(self._elements, self._priorities)])})"
