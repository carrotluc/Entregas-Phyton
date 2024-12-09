
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List
from datetime import date, datetime
from grafo import Grafo
from recorridos import Recorrido_en_profundidad

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        if len(dni) != 9 or not dni[:-1].isdigit() or not dni[-1].isalpha():
            raise ValueError(f"DNI inválido: {dni}")
        if fecha_nacimiento >= date.today():
            raise ValueError(f"La fecha de nacimiento debe ser anterior a la fecha actual.")
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    @staticmethod
    def parse(cadena: str) -> Usuario:
        partes = cadena.split(",")
        if len(partes) != 4:
            raise ValueError("La cadena debe tener el formato 'dni,nombre,apellidos,fecha_nacimiento'.")

        dni = partes[0].strip()
        nombre = partes[1].strip()
        apellidos = partes[2].strip()
        fecha_nacimiento = datetime.strptime(partes[3].strip(), "%Y-%m-%d").date()
        return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self) -> str:
        return f"{self.dni} - {self.nombre}"

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __xx_num: int = 0

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__xx_num += 1
        return Relacion(Relacion.__xx_num, interacciones, dias_activa)

    def __str__(self) -> str:
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"

class Red_social(Grafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False, tipo_recorrido: str = "BACK") -> None:
        super().__init__(es_dirigido)
        self.__usuarios_dni: Dict[str, Usuario] = {}
        self.tipo_recorrido = tipo_recorrido

    @staticmethod
    def of(es_dirigido: bool = False, tipo_recorrido: str = "BACK") -> Red_social:
        return Red_social(es_dirigido, tipo_recorrido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False, tipo_recorrido: str = "BACK") -> Red_social:
        red_social = Red_social.of(es_dirigido, tipo_recorrido)

        with open(f1, 'r') as archivo_usuarios:
            for linea in archivo_usuarios:
                dni, nombre, apellidos, fecha_nacimiento = linea.strip().split(',')
                fecha_nacimiento = date.fromisoformat(fecha_nacimiento)
                usuario = Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
                red_social.__usuarios_dni[dni] = usuario

        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                dni1, dni2, interacciones, dias_activa = linea.strip().split(',')
                interacciones = int(interacciones)
                dias_activa = int(dias_activa)

                usuario1 = red_social.__usuarios_dni.get(dni1)
                usuario2 = red_social.__usuarios_dni.get(dni2)

                if usuario1 and usuario2:
                    relacion = Relacion.of(interacciones, dias_activa)
                    red_social.add_vertex(usuario1)
                    red_social.add_vertex(usuario2)
                    red_social.add_edge(usuario1, usuario2, relacion)

        return red_social

    def __str__(self) -> str:
        resultado = ""
        for usuario in self.__usuarios_dni.values():
            relaciones = self.get_relaciones(usuario)
            num_interacciones = sum(relacion.interacciones for relacion in relaciones)
            dias_activa = max(relacion.dias_activa for relacion in relaciones) if relaciones else 0
            resultado += f"({usuario.dni} - días activa: {dias_activa} - num interacciones: {num_interacciones})\n"
        return resultado

    def get_relaciones(self, usuario: Usuario) -> List[Relacion]:
        relaciones = []
        for vecino in self.successors(usuario):
            relaciones.append(self.edge_weight(usuario, vecino))
        return relaciones

    def get_usuario_por_dni(self, dni: str) -> Usuario:
        return self.__usuarios_dni.get(dni)
