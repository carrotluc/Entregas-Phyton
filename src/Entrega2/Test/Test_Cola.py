from Entrega2.Tipos.Cola import Cola

def test_cola():
    cola = Cola.of()
    cola.add_all([23, 47, 1, 2, -3, 4, 5])
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    print(f"Resultado de la cola: {cola}")
    
    removed_elements = cola.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}")

if __name__ == "__main__":
    test_cola()

