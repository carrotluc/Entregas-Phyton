
from datetime import date
from red_social import Red_social, Usuario
from recorridos import Recorrido
from typing import List

def test_recorrido_en_anchura() -> None:
    red_social: Red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')

    dni_origen: str = '25143909I'
    dni_destino: str = '87345530M'

    usuario_origen: Usuario = red_social.get_usuario_por_dni(dni_origen)
    usuario_destino: Usuario = red_social.get_usuario_por_dni(dni_destino)
    recorrido: Recorrido = Recorrido(red_social, usuario_origen)
    camino: List[Usuario] = recorrido.path_to_origin(usuario_destino)

    print(f"El camino más corto desde {dni_origen} hasta {dni_destino} es:")
    for usuario in camino:
        print(usuario)
    distancia_minima: int = len(camino) - 1
    print(f"La distancia mínima es: {distancia_minima} pasos")

if __name__ == "__main__":
    test_recorrido_en_anchura()



