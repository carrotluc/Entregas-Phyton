from red_social import Red_social
from typing import List

def mostrar_predecesores_y_vecinos(red_social: Red_social) -> None:
    """
    Muestra el número de predecesores y vecinos de cada vértice en la red social.
    """
    print("Nº Predecesores de cada vértice")
    for usuario in red_social._Red_social__usuarios_dni.values():
        predecesores: List[Red_social.Usuario] = [
            u for u in red_social._Red_social__usuarios_dni.values() if red_social.edge_weight(u, usuario) is not None
        ]
        print(f"{usuario.dni} - {usuario.nombre} -- {len(predecesores)}")

    print("Nº Vecinos de cada vértice")
    for usuario in red_social._Red_social__usuarios_dni.values():  
        vecinos: int = len(red_social.successors(usuario))
        print(f"{usuario.dni} - {usuario.nombre} -- {vecinos}")

if __name__ == "__main__":
    red_social: Red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')
    mostrar_predecesores_y_vecinos(red_social)
