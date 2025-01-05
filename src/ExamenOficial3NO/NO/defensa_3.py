from __future__ import annotations
from dataclasses import dataclass
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from typing import TypeVar, Generic, Dict, Set, Optional, Callable
from grafo import Grafo

V = TypeVar('V')  # Tipo para vértices
E = TypeVar('E')  # Tipo para aristas

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
