from __future__ import annotations
from typing import TypeVar, Generic, Dict, Set, Optional, Callable
import matplotlib.pyplot as plt
import networkx as nx

V = TypeVar('V')  
E = TypeVar('E')  


class Grafo(Generic[V, E]):
    def vertex_set(self) -> Set[V]:
        """
        Devuelve el conjunto de vértices del grafo.

        :return: Conjunto de vértices.
        """
        return set(self.adyacencias.keys())

    """
    Representación de un grafo utilizando un diccionario de adyacencia.
    """
    def __init__(self, es_dirigido: bool = True):
        self.es_dirigido: bool = es_dirigido
        self.adyacencias: Dict[V, Dict[V, E]] = {}
    
    @staticmethod
    def of(es_dirigido: bool = True) -> Grafo[V, E]:
        """
        Método de factoría para crear un nuevo grafo.
        
        :param es_dirigido: Indica si el grafo es dirigido (True) o no dirigido (False).
        :return: Nuevo grafo.
        """
        return Grafo(es_dirigido)
    
    def __add_neighbors(self, vertice: V, vecino: V, arista: E) -> None:
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
        self.adyacencias[vertice][vecino] = arista

    def __add_predecessors(self, vertice: V, predecesor: V, arista: E) -> None:
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = {}
            self.adyacencias[predecesor][vertice] = arista

    
    
    def add_edge(self, origen: V, destino: V, arista: E) -> None:
        if origen not in self.adyacencias or destino not in self.adyacencias:
            raise ValueError("Ambos vértices deben existir en el grafo.")
        if origen == destino:
            raise ValueError("No se permiten bucles.")
        if destino in self.adyacencias[origen]:
            raise ValueError("Ya existe una arista entre estos vértices.")
        self.adyacencias[origen][destino] = arista
        if not self.es_dirigido:
            self.adyacencias[destino][origen] = arista
        self.__add_neighbors(origen, destino, arista)
        if self.es_dirigido:
            self.__add_predecessors(destino, origen, arista)

    
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
        """
        Dibuja el grafo utilizando NetworkX y Matplotlib. las funciones lambda permiten personalizar la representación
        de los vértices y aristas.

        :param titulo: Título del gráfico
        :param lambda_vertice: Función lambda para representar los vértices
        :param lambda_arista: Función lambda para representar las aristas
        """
        
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



    def __str__(self) -> str:
        resultado = ""
        for origen, destinos in self.adyacencias.items():
            aristas = ", ".join(f"{destino} ({arista})" for destino, arista in destinos.items())
            resultado += f"{origen} -> {aristas}\n"
        return resultado

if __name__ == '__main__':
    grafo = Grafo.of(es_dirigido=True)
    grafo.add_vertex("A")
    grafo.add_vertex("B")
    grafo.add_vertex("C")
    grafo.add_vertex("D")
    grafo.add_edge("A", "B", 5)
    grafo.add_edge("B", "C", 3)
    grafo.add_edge("C", "D", 1)
    
    grafo.draw(
        titulo="Mi Grafo Dirigido",
        lambda_vertice=str,
        lambda_arista=lambda peso: str(peso)  
    )
    
    grafo.inverse_graph().draw(
        titulo="Inverso del Grafo Dirigido",
        lambda_vertice=str,
        lambda_arista=lambda peso: str(peso)  
    )




