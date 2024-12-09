import networkx as nx
import matplotlib.pyplot as plt
from red_social import Red_social

def dibujar_red_social(red_social: Red_social):
    """
    Dibuja la red social como un grafo utilizando NetworkX y Matplotlib.
    """
    # Crear un grafo vacío de NetworkX
    G = nx.DiGraph()  # Usamos DiGraph si la red social es dirigida, Grafo no dirigido: nx.Graph()

    # Agregar vértices (usuarios) al grafo
    for usuario in red_social._Red_social__usuarios_dni.values():
        G.add_node(usuario.dni, label=usuario.nombre)

    # Agregar aristas (relaciones) al grafo
    for usuario1 in red_social._Red_social__usuarios_dni.values():
        for vecino in red_social.successors(usuario1):
            # Aquí, usamos el DNI de los usuarios para identificar los vértices
            G.add_edge(usuario1.dni, vecino.dni)

    # Dibujar el grafo
    pos = nx.spring_layout(G, seed=42, k=0.3)  # Ajustar k para espaciar más los nodos

    labels = nx.get_node_attributes(G, 'label')  # Usamos el nombre del usuario como etiqueta

    plt.figure(figsize=(12, 10))  # Tamaño de la figura
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20, edge_color='gray')

    # Asegurarnos de que las etiquetas sean legibles
    plt.title("Red Social", fontsize=16)
    plt.axis('off')  # Desactivar el eje para una visualización más limpia
    plt.show()

if __name__ == "__main__":
    # Cargar la red social desde los archivos en la carpeta 'resources'
    red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')

    # Dibujar la red social
    dibujar_red_social(red_social)
