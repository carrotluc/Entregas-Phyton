from Entrega2.Tipos.Pila import Pila

def test_pila():
    pila = Pila.of()
    pila.add(1)
    pila.add(2)
    pila.add(3)
    print("Creación de una pila y se añaden los números: 1, 2, 3")
    print(f"Resultado de la pila: {pila}")
    
    removed_element = pila.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}")
    
    removed_elements = []
    while not pila.is_empty():
        removed_elements.append(pila.remove())
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}")

if __name__ == "__main__":
    test_pila()

