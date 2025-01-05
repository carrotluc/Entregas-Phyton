from __future__ import annotations
from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import networkx as nx
import matplotlib.pyplot as plt

V = TypeVar('V')
E = TypeVar('E')

class Grafo(Generic[V, E]):
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}
        self.vecinos: Dict[V, Set[V]] = {}
        self.predecesores: Dict[V, Set[V]] = {}

    def __add_neighbors(self, vertice: V, vecino: V) -> None:
        if vertice not in self.vecinos:
            self.vecinos[vertice] = set()
        self.vecinos[vertice].add(vecino)

    def __add_predecessors(self, vertice: V, predecesor: V) -> None:
        if vertice not in self.predecesores:
            self.predecesores[vertice] = set()
        self.predecesores[vertice].add(predecesor)

    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        if origen not in self.adyacencias or destino not in self.adyacencias:
            raise ValueError("Ambos vértices deben existir en el grafo.")
        if origen == destino:
            raise ValueError("No se permiten bucles.")
        if destino in self.adyacencias[origen]:
            raise ValueError("Ya existe una arista entre estos vértices.")
        
        self.adyacencias[origen][destino] = arista
        self.__add_neighbors(origen, destino)

        if not self.es_dirigido:
            self.adyacencias[destino][origen] = arista
            self.__add_neighbors(destino, origen)
        else:
            self.__add_predecessors(destino, origen)

    def edge_weight(self, sourceVertex: V, targetVertex: V) -> Optional[E]:
        if sourceVertex in self.adyacencias and targetVertex in self.adyacencias[sourceVertex]:
            return self.adyacencias[sourceVertex][targetVertex]
        return None

    def add_vertex(self, vertice: V) -> bool:
        if vertice in self.adyacencias:
            return False
        self.adyacencias[vertice] = {}
        return True

    def edge_source(self, e: E) -> Optional[V]:
        for origen, destinos in self.adyacencias.items():
            for destino, arista in destinos.items():
                if arista == e:
                    return origen
        return None

    def edge_target(self, e: E) -> Optional[V]:
        for origen, destinos in self.adyacencias.items():
            for destino, arista in destinos.items():
                if arista == e:
                    return destino
        return None

    def vertex_set(self) -> Set[V]:
        return set(self.adyacencias.keys())
    
    def contains_edge(self, origen: V, destino: V) -> bool:
        return destino in self.adyacencias.get(origen, {})

    def predecessors(self, vertice: V) -> Set[V]:
        if self.es_dirigido:
            return {origen for origen, destinos in self.adyacencias.items() if vertice in destinos}
        return self.successors(vertice)

    def successors(self, vertice: V, tipo_recorrido: str = "FORWARD") -> Set[V]:
        if tipo_recorrido == "FORWARD":
            return set(self.adyacencias.get(vertice, {}).keys())
        elif tipo_recorrido == "BACK":
            return self.predecessors(vertice)
        return set()

    def inverse_graph(self) -> Grafo[V, E]:
        if not self.es_dirigido:
            return self
        inverso = Grafo(self.es_dirigido)
        for origen in self.adyacencias:
            inverso.add_vertex(origen)
            for destino, arista in self.adyacencias[origen].items():
                inverso.add_vertex(destino)
                inverso.add_edge(destino, origen, arista)
        return inverso

    def draw(self, titulo: str = "Grafo",
             lambda_vertice: Callable[[V], str] = str,
             lambda_arista: Callable[[E], str] = str) -> None:
        G = nx.DiGraph() if self.es_dirigido else nx.Graph()
    
        for vertice in self.vertex_set():
            G.add_node(vertice, label=lambda_vertice(vertice))  
        for origen in self.vertex_set():
            for destino, arista in self.adyacencias[origen].items():
                G.add_edge(origen, destino, label=lambda_arista(arista)) 
                
        pos = nx.spring_layout(G)  
        plt.figure(figsize=(8, 6))
        fig = plt.gcf()
        fig.canvas.manager.set_window_title(titulo)  
        nx.draw(G, pos, with_labels=True, node_color="#D8BFD8", font_weight="bold", node_size=500,
                labels=nx.get_node_attributes(G, 'label'), font_family='serif')

        edge_labels = nx.get_edge_attributes(G, "label")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family='serif')

        plt.title(titulo, fontfamily='serif')
        plt.show()

# Ejemplo de uso
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

    inverso = grafo.inverse_graph()
    print("Predecesores de 'B':", grafo.predecessors("B"))
    print("Sucesores de 'A' (FORWARD):", grafo.successors("A", "FORWARD"))
    print("Sucesores de 'A' (BACK):", grafo.successors("A", "BACK"))
    print("Grafo inverso:\n", inverso)
   
