from collections import Counter
from math import factorial

def funcion_p2(n: int, k:int, i:int=1)->int:
    assert n>0, f'{n} debe ser positiva'
    assert k>0, f'{k} debe ser positiva'
    assert i>0, f'{i} debe ser positiva'
    assert i<(k+1), f'{i} debe ser menor que {k+1}'
    assert n >= k, f'{n} debe ser mayor o igual a {k}'
    s: int = 1
    for i in range(i, k-1):
        s *= (n-i+1)
    return s



def funcion_c2(n: int, k:int)->int:
    assert n>0, f'{n} debe ser positiva'
    assert k>0, f'{k} debe ser positiva'
    assert n > k, f'{n} debe ser mayor que {k}'
    a: int = k+1
    s = factorial(n) // (factorial(a) * factorial(n - a))
    return s



def funcion_s2(n: int, k:int)->float:
    assert n>0, f'{n} debe ser positiva'
    assert k>0, f'{k} debe ser positiva'
    assert n >= k, f'{n} debe ser mayor o igual a {k}'
    a: int = factorial(k)
    b: int = n*(factorial(k+2))
    s: int = 0
    for i in range(0,k+1):
        d: int = (-1)**i 
        num: int = (factorial(k)) / (factorial(i)*(factorial(k-i)))
        e: int = (k-i)**(n+1)
        s += d*num*e
    t: int = (a/b)*s
    return t

#print(funcion_s2(10,7))

proyecto = '../../' 
fichero = proyecto + "resources/palabras_random.csv"
def palabrasMasComunes(fichero:str, n:int=5)->list[tuple[str, int]]:
    assert n>1, f'{n} debe ser mayor que 1'
    with open(fichero, 'r', encoding='utf-8') as file:
        texto = file.read().lower()
    palabras = texto.split(',')
    conteo_palabras = Counter(palabras)
    palabras_comunes = conteo_palabras.most_common(n)
    return palabras_comunes
    
#print(palabrasMasComunes(fichero, 5))
    
if __name__ == '__main__':
    try: 
        f1: int = funcion_p2(4, 2)
        print(f'La solución a la primera actividad es {f1}, para n=4 y k=2')
    except AssertionError as e:
        print(f'Error en funcion_p2: {e}')
    try:
        f2: int = funcion_c2(4, 2)
        print(f'La solución a la segunda actividad es {f2}, para n=4 y k=2')
    except AssertionError as e:
        print(f'Error en C2: {e}')
    try: 
        f3: int = funcion_s2(4, 2)
        print(f'La solución a la tercera actividad es {f3}, para n=4 y k=2')
    except AssertionError as e:
        print(f'Error en S2: {e}')
    try: 
        f4: str = palabrasMasComunes(fichero,5)
        print(f'Las cinco palabras que más se repiten son {f4}')
    except Exception as e:
        print(f'Error en palabrasMasComunes: {e}')
    #Ten en cuenta que la ubicación del fichero es la siguiente:
    #proyecto = '../../' 
    #fichero = proyecto + "resources/palabras_random.csv"
    
    