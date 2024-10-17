################################################################################
#EJEMPLO 1:
from pygments.lexers import int_fiction


def calcular_producto(n:int, k:int) -> int:
    if n <= k:
        return "ERROR: ¡n debe ser mayor que k!"
    s:int = 1  
    for i in range(0,k + 1):  
        s = s*(n - i + 1) 
    return s

def test1(): 
    n:int = 4
    k:int = 2
    r = calcular_producto(n,k)
    print(f'Para el caso de n={n} y k={k}, \nla solución del enunciado será {r}.')
################################################################################
#EJEMPLO 2:
def producto_secuencia_geo(a: int, r: int, k:int) -> int:
    s:int = 1
    for i in range(1, k+1): 
        ai= a*(r** (i-1))
        s =s * ai
    return s

def test2(): 
    a: int = 3
    r:int = 5
    k:int = 2
    resultado = producto_secuencia_geo(a, r, k)
    print(f"El producto de los primeros {k} términos es: {resultado}")
##############################################################################      
#EJEMPLO 3: 
from math import factorial
def numero_combinatorio(n:int, k:int) -> int:
    if n < k:
        return "ERROR: ¡n debe ser mayor que k!"
    else: 
        nm: int = factorial(n)/(factorial(k)*factorial(n-k)) 
    return nm

def test3():
    n: int = 4
    k: int = 2
    sol = numero_combinatorio(n,k)
    print(f'La solución al problema es {sol}')
###########################################################################################
#EJEMPLO 4:
from math import factorial
def producto_s(n:int, k:int) -> float:
    if n < k:
        return "ERROR: ¡n debe ser mayor que k!"
    else: 
        s= 0
        a: float = 1/factorial(k)
        for i in range(0,k): #Es hasta k ya que en los rangos el últ no está incluido
            c: float = (-1)**i
            b: float = numero_combinatorio(k+1,i+1)
            d: float = (k-i)**n
            s:int = s + (a*c*b*d)
        return s

def test4():
    print(producto_s(4,2))
    
###########################################################################################
#EJEMPLO 5:
from typing import Callable
def m_newton(f: Callable[[float],[float]], g: Callable[[float],[float]], a:float, e:float)-> float:
    x = a
    while abs(f(x)) > e:
        x = x - f(x) / g(x)
    return x

#Se modifica lo que hay escrito después de la x: en función de la funcion con la que queramos trabajar. 
f:Callable[[float],[float]] = lambda x: 2.0*(x**2.0)
g: Callable[[float], float] = lambda x: 4*x

def test5():
    a = 3.0
    e = 0.001
    root = m_newton(f, g, a, e)
    print(f"La raíz es aproximadamente: {root}")
#########################################################################
if __name__ == '__main__':
    print(test1())
    print(test2())
    print(test4())



