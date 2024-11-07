from Entrega2.Tipos.Lista_Ordenada import Lista_ordenada

def test_lista_ordenada():
    lista: list[int] = Lista_ordenada.of(lambda x: x)
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}")
    
    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}")
    
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}")
    
    lista.add(1)
    lista.add(2)
    lista.add(3)
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")

if __name__ == "__main__":
    test_lista_ordenada()

