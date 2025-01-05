from typing import List, Dict, Tuple, Optional, TypeVar, Generic, Set
from grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(Generic[V, E]):
    def __init__(self, grafo: Grafo[V, E], origen: V):
        self.tree: Dict[V, Tuple[Optional[V], float]] = {}
        self.path: List[V] = []
        self.grafo = grafo
        self._recorrer(origen)

    def _recorrer(self, origen: V) -> None:
        cola: List[V] = [origen]
        self.tree[origen] = (None, 0)
        while cola:
            vertice: V = cola.pop(0)
            self.path.append(vertice)
            for sucesor in self.grafo.successors(vertice):
                if sucesor not in self.tree:
                    self.tree[sucesor] = (vertice, self.tree[vertice][1] + 1)
                    cola.append(sucesor)

    def path_to_origin(self, vertice: V) -> List[V]:
        camino: List[V] = []
        while vertice is not None:
            camino.insert(0, vertice)
            vertice = self.tree.get(vertice, (None, 0))[0]
        return camino

    def origin(self, vertice: V) -> Optional[V]:
        return self.tree.get(vertice, (None, 0))[0]

    def groups(self) -> Dict[V, Set[V]]:
        grupos: Dict[V, Set[V]] = {}
        for vertice, (predecesor, _) in self.tree.items():
            if predecesor is not None:
                if predecesor not in grupos:
                    grupos[predecesor] = set()
                grupos[predecesor].add(vertice)
        return grupos

class Recorrido_en_profundidad(Recorrido[V, E]):
    @staticmethod
    def of(grafo: Grafo[V, E], origen: V) -> 'Recorrido_en_profundidad':
        return Recorrido_en_profundidad(grafo, origen)

    def __init__(self, grafo: Grafo[V, E], origen: V) -> None:
        super().__init__(grafo, origen)
        self._recorrer_en_profundidad(origen)

    def _recorrer_en_profundidad(self, origen: V) -> None:
        pila: List[V] = [origen]
        self.tree[origen] = (None, 0)  
        while pila:
            vertice: V = pila.pop()
            if vertice not in self.tree: 
                self.path.append(vertice)
                for sucesor in self.grafo.successors(vertice):
                    if sucesor not in self.tree:
                        self.tree[sucesor] = (vertice, self.tree[vertice][1] + 1)
                        pila.append(sucesor)

    def traverse(self, origen: V) -> None:
        self._recorrer_en_profundidad(origen)
    
    def path_to(self, destino: V) -> List[V]:
        camino: List[V] = []
        vertice: V = destino
        while vertice is not None:
            camino.insert(0, vertice)
            vertice = self.tree.get(vertice, (None, 0))[0]
        return camino

if __name__ == '__main__':
    grafo = Grafo(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_edge("A", "B", 1)
    grafo.add_edge("A", "C", 2)
    grafo.add_edge("B", "D", 1)
    grafo.add_edge("C", "D", 3)

    recorrido = Recorrido_en_profundidad.of(grafo, "A")
    recorrido.traverse("A")
    print(f"Camino recorrido en DFS: {recorrido.path}")
    print(f"Árbol de recorrido: {recorrido.tree}")
