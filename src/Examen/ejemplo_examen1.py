def funcion_p3(n:int, k:int, i:int=1)->int:
    assert n>0, f'{n} debe ser mayor que cero'
    assert k>0, f'{k} debe ser mayor que cero'
    assert i<k, f'{i} debe ser menr que {k}'
    assert i>0, f'{i} debe ser mayor que cero'
    
    s: int = 1
    for i in range(i,k+1):
        s = s*(n + i) 
    return s

from Examen.ejemplo_examen1 import funcion_p3
print(funcion_p3(2,5))
        
from math import factorial
def funcion_c3(n:int, k:int)->int:
    assert n>0, f'{n} debe ser mayor que cero'
    assert k>0, f'{k} debe ser mayor que cero'
    assert n>=(k-1), f'{n} debe ser mayor o igual que {k-1}'
    a:int= factorial(n+1)
    b: int = factorial(k)
    c: int = factorial(n-k+1)
    s = a/(b*c)
    return int(s) 
print(funcion_c3(1,2))


def funcion_s3(n:int, k:int)->float:
    assert n > 0, f'{n} debe ser mayor que cero'
    assert k > 0, f'{k} debe ser mayor que cero'
    assert n >= k, f'{n} debe ser mayor o igual que {k}'
    s = 0.0 
    for i in range(0, k + 1):
        num_comb = factorial(k) / (factorial(i) * factorial(k - i))
        term = (-1) ** i * num_comb * factorial(k - i) / factorial(n + i)
        s += term  
    return s
print(funcion_s3(4,2))

from typing import List, Tuple
from collections import Counter
import re

def palabrasMenosComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    # Validación de parámetros
    assert n > 1, f'n debe ser mayor que 1, se recibió {n}'

    # Inicializar un contador para las palabras
    word_count = Counter()
    
    # Leer el archivo y contar palabras
    with open(fichero, 'r', encoding='utf-8') as file:
        for line in file:
            # Usar una expresión regular para extraer palabras y convertirlas a minúsculas
            words = re.findall(r'\b\w+\b', line.lower())
            word_count.update(words)  # Actualizar el contador con las palabras encontradas
    
    # Obtener las palabras menos comunes (n)
    least_common_words = word_count.most_common()[-n:]  # Los n menos comunes
    least_common_words.sort(key=lambda x: x[1])  # Ordenar por frecuencia
    
    return least_common_words