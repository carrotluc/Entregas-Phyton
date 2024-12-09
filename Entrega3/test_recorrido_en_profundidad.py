
from datetime import date
from red_social import Red_social, Usuario
from recorridos import Recorrido
from typing import List

def test_recorrido_en_profundidad() -> None:
    red_social: Red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')

    dni_origen: str = '25143909I'
    dni_destino: str = '76929765H'

    usuario_origen: Usuario = red_social.get_usuario_por_dni(dni_origen)
    usuario_destino: Usuario = red_social.get_usuario_por_dni(dni_destino)
    recorrido: Recorrido = Recorrido(red_social, usuario_origen)
    camino: List[Usuario] = recorrido.path_to_origin(usuario_destino)

    if not camino:
        print(f"No hay conexión directa entre {dni_origen} y {dni_destino}.")
    else:
        print(f"El camino en profundidad entre {dni_origen} y {dni_destino} es:")
        for usuario in camino:
            print(usuario)

if __name__ == "__main__":
    test_recorrido_en_profundidad()

