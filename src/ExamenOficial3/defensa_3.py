from __future__ import annotations
from dataclasses import dataclass
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from typing import TypeVar, Generic, Dict, Set, Optional, Callable

V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

#HE TENIDO PROBLEMAS A LA HORA DE IMPORTAR GRAFO Y RECORRIDO
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
                        self.tree[sucesor] = (vertice, 0)
                        pila.append(sucesor)

    def path_to(self, destino: V) -> List[V]:
        camino: List[V] = []
        while destino is not None:
            camino.insert(0, destino)
            destino = self.tree.get(destino, (None, 0))[0]
        return camino


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



@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a 0.")
        if not nombre or not tipo or not loc_cromosoma:
            raise ValueError("Los campos no pueden estar vacíos.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(cadena: str) -> 'Gen':
        partes = cadena.split(",")
        if len(partes) != 4:
            raise ValueError("La cadena debe tener el formato 'nombre,tipo,num_mutaciones,loc_cromosoma'.")
        nombre = partes[0].strip()
        tipo = partes[1].strip()
        num_mutaciones = int(partes[2].strip())
        loc_cromosoma = partes[3].strip()
        return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        if not (-1 <= conexion <= 1):
            raise ValueError(f"El valor de conexión debe estar entre -1 y 1. Dado: {conexion}")
        if not nombre_gen1 or not nombre_gen2:
            raise ValueError("Los nombres de los genes no pueden estar vacíos.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(cadena: str) -> 'RelacionGenAGen':
        partes = cadena.split(",")
        if len(partes) != 3:
            raise ValueError("La cadena debe tener el formato 'nombre_gen1,nombre_gen2,conexion'.")
        nombre_gen1 = partes[0].strip()
        nombre_gen2 = partes[1].strip()
        conexion = float(partes[2].strip())
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

    def __str__(self) -> str:
        return f"{self.nombre_gen1},{self.nombre_gen2},{self.conexion}"

class RedGenica(Grafo[Gen, RelacionGenAGen]):
    def __init__(self, es_dirigido: bool = False):
        super().__init__(es_dirigido)

    @staticmethod
    def parse(archivo_genes: str, archivo_relaciones: str, es_dirigido: bool = False) -> 'RedGenica':
        red_genica = RedGenica(es_dirigido)
        with open(archivo_genes, 'r') as f:
            for linea in f:
                gen = Gen.parse(linea.strip())
                red_genica.agregar_gen(gen)
        with open(archivo_relaciones, 'r') as f:
            for linea in f:
                relacion = RelacionGenAGen.parse(linea.strip())
                red_genica.agregar_relacion(relacion)
        return red_genica

    def agregar_gen(self, gen: Gen) -> None:
        self.add_vertex(gen)

    def agregar_relacion(self, relacion: RelacionGenAGen) -> None:
        gen1 = next((v for v in self.vertex_set() if v.nombre == relacion.nombre_gen1), None)
        gen2 = next((v for v in self.vertex_set() if v.nombre == relacion.nombre_gen2), None)
        if gen1 and gen2:
            self.add_edge(gen1, gen2, relacion)


if __name__ == "__main__":
    gen_prueba = "TP53,supresor tumoral,256,17p13.1"
    relacion_prueba = "TP53,EGFR,0.8"
    gen = Gen.parse(gen_prueba)
    print(f"Gen creado: {gen}")

    relacion = RelacionGenAGen.parse(relacion_prueba)
    print(f"Relación creada: {relacion}")
    print(f"Coexpresados: {relacion.coexpresados}")
    print(f"Antiexpresados: {relacion.antiexpresados}")

    red_genica = RedGenica.parse("genes.txt", "red_genes.txt", es_dirigido=False)
    print("Red génica creada.")

    # Aplicar el recorrido en profundidad desde KRAS hasta PIK3CA
    recorrido = Recorrido_en_profundidad(red_genica, "KRAS")
    camino = recorrido.path_to("PIK3CA")
    print(f"Camino encontrado: {camino}")

    # Crear el subgrafo a partir de los vértices del camino
    subgrafo = red_genica.subgraph(set(camino))

    # Dibujar el subgrafo
    pos = nx.spring_layout(subgrafo)
    labels = {v: v.nombre for v in subgrafo.nodes()}
    nx.draw(subgrafo, pos, with_labels=True, labels=labels, node_color="#D8BFD8", font_weight="bold", node_size=500)
    plt.title("Subgrafo de KRAS a PIK3CA")
    plt.show()
