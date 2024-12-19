import networkx as nx
import matplotlib.pyplot as plt
from red_social import Red_social

def dibujar_red_social(red_social: Red_social):
    """
    Dibuja la red social como un grafo utilizando NetworkX y Matplotlib.
    """
    G = nx.DiGraph()  
    
    for usuario in red_social._Red_social__usuarios_dni.values():
        G.add_node(usuario.dni, label=usuario.nombre)

   
    for usuario1 in red_social._Red_social__usuarios_dni.values():
        for vecino in red_social.successors(usuario1):
           
            G.add_edge(usuario1.dni, vecino.dni)

    pos = nx.spring_layout(G, seed=42, k=0.3) 

    labels = nx.get_node_attributes(G, 'label') 
    plt.figure(figsize=(12, 10))  
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='purple', font_size=12, font_weight='bold', arrowsize=20, edge_color='gray')

    plt.title("Red Social", fontsize=16)
    plt.axis('off') 
    plt.show()

if __name__ == "__main__":
    
    red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')
    dibujar_red_social(red_social)
