#ACTIVIDAD 1 - ENTREGA 1:
def calcular_producto(n:int, k:int) -> int:
    if n <= k:
        return "ERROR: ¡n debe ser mayor que k!"
    s:int = 1  
    for i in range(0,k + 1):  
        s = s*(n - i + 1) 
    return s

#ACTIVIDAD 2 - ENTREGA 1:
def producto_secuencia_geo(a: int, r: int, k:int) -> int:
    s:int = 1
    for i in range(1, k+1): 
        ai= a*(r** (i-1))
        s =s * ai
    return s

#ACTIVIDAD 3 - ENTREGA 1: 
from math import factorial
def numero_combinatorio(n:int, k:int) -> int:
    if n < k:
        return "ERROR: ¡n debe ser mayor que k!"
    else: 
        nm: int = factorial(n)/(factorial(k)*factorial(n-k)) 
    return nm

#ACTIVIDAD 4 - ENTREGA 1:
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

#ACTIVIDAD 5 - ENTREGA 1:
from typing import Callable
#f es la función
#g es la función derivada
def m_newton(f: Callable[[float],[float]], g: Callable[[float],[float]], a:float, e:float)-> float:
    x = a
    while abs(f(x)) > e:
        x = x - f(x) / g(x)
    return x

#Se modifica lo que hay escrito después de la x: en función de la funcion con la que queramos trabajar. 
f:Callable[[float],[float]] = lambda x: 2.0*(x**2.0)
g: Callable[[float], float] = lambda x: 4*x




 
    

    
    
    
    
    
    