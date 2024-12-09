from typing import List, Dict, Tuple, Optional, TypeVar, Generic, Set
from grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(Generic[V, E]):
    """
    Representa un recorrido en un grafo desde un vértice inicial hasta otros vértices en el grafo.
    """

    def __init__(self, grafo: Grafo[V, E], origen: V):
        """
        Inicializa el recorrido sobre el grafo desde un vértice de origen.

        :param grafo: El grafo sobre el que se realiza el recorrido.
        :param origen: El vértice de origen desde donde comienza el recorrido.
        """
        self.tree: Dict[V, Tuple[Optional[V], float]] = {}
        self.path: List[V] = []
        self.grafo = grafo
        self._recorrer(origen)

    def _recorrer(self, origen: V) -> None:
        """
        Realiza el recorrido en el grafo y llena la estructura de árbol de recorrido.
        """
        cola: List[V] = [origen]
        self.tree[origen] = (None, 0)

        while cola:
            vertice = cola.pop(0)
            self.path.append(vertice)

            for sucesor in self.grafo.successors(vertice):
                if sucesor not in self.tree:
                    self.tree[sucesor] = (vertice, self.tree[vertice][1] + 1)
                    cola.append(sucesor)

    def path_to_origin(self, vertice: V) -> List[V]:
        """
        Devuelve el camino hacia el origen desde un vértice dado, siguiendo los predecesores.

        :param vertice: El vértice desde el que se debe construir el camino hacia el origen.
        :return: Lista de vértices que forman el camino desde el vértice dado hasta el origen.
        """
        camino: List[V] = []
        while vertice is not None:
            camino.insert(0, vertice)
            vertice = self.tree.get(vertice, (None, 0))[0]
        return camino

    def origin(self, vertice: V) -> Optional[V]:
        """
        Devuelve el origen del recorrido desde un vértice dado.

        :param vertice: El vértice desde el cual encontrar el origen.
        :return: El vértice origen del recorrido.
        """
        return self.tree.get(vertice, (None, 0))[0]

    def groups(self) -> Dict[V, Set[V]]:
        """
        Organiza los vértices del grafo en grupos según su predecesor.

        :return: Un diccionario donde las claves son los vértices de origen
                 y los valores son conjuntos de vértices que pertenecen a ese origen.
        """
        grupos: Dict[V, Set[V]] = {}
        for vertice, (predecesor, _) in self.tree.items():
            if predecesor is not None:
                if predecesor not in grupos:
                    grupos[predecesor] = set()
                grupos[predecesor].add(vertice)
        return grupos


class Recorrido_en_profundidad(Recorrido[V, E]):
    """
    Clase que extiende la clase Recorrido para realizar un recorrido en profundidad (DFS) sobre un grafo.
    """

    @staticmethod
    def of(grafo: Grafo[V, E], origen: V) -> 'Recorrido_en_profundidad':
        """
        Método de factoría para crear una nueva instancia de Recorrido_en_profundidad.

        :param grafo: El grafo sobre el que realizar el recorrido.
        :param origen: El vértice de origen desde donde empieza el recorrido.
        :return: Una nueva instancia de Recorrido_en_profundidad.
        """
        return Recorrido_en_profundidad(grafo, origen)

    def __init__(self, grafo: Grafo[V, E], origen: V) -> None:
        """
        Inicializa el recorrido en profundidad desde un vértice de origen.

        :param grafo: El grafo sobre el que se realiza el recorrido.
        :param origen: El vértice de origen desde donde comienza el recorrido.
        """
        super().__init__(grafo, origen) 
        self._recorrer_en_profundidad(origen) 

    def _recorrer_en_profundidad(self, origen: V) -> None:
        """
        Realiza el recorrido en profundidad utilizando una pila para explorar los vértices.
        """
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
        """
        Realiza un recorrido en profundidad (DFS) comenzando desde el vértice fuente.
        Este método usa la pila para explorar los vértices recursivamente y marca los visitados.

        :param origen: El vértice de origen para el recorrido DFS.
        """
        self._recorrer_en_profundidad(origen)


if __name__ == '__main__':
    grafo = Grafo.of(es_dirigido=True)
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
