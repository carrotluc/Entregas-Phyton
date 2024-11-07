from Entrega2.Tipos.Lista_Ordenada_Sin_Repeticion import Lista_ordenada_sin_repeticion

def test_lista_ordenada_sin_repeticion():
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
    for num in [23, 47, 47, 1, 2, -3, 4, 5]:
        lista.add(num)
    print(f"Resultado de la lista ordenada sin repetición: {lista}")
    
    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}")
    
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}")
    print("Comprobando si se añaden los números en la posición correcta...")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")

if __name__ == "__main__":
    test_lista_ordenada_sin_repeticion()
