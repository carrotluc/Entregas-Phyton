#ACTIVIDAD 1 - ENTREGA 1:
def calcular_producto(n:int, k:int) -> int:
    if n <= k:
        return "ERROR: ¡n debe ser mayor que k!"
    s:int = 1  
    for i in range(k + 1):  
        s *= (n - i + 1) 
    return s

#ACTIVIDAD 2 - ENTREGA 1:
def producto_secuencia_geo(a: int, r: int, k:int) -> int:
    s:int = 1
    for i in range(1, k+1): 
        ai= a* (r** (i-1))
        s *= ai
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
def producto_s(n:int, k:int) -> int:
     if n < k:
        return "ERROR: ¡n debe ser mayor que k!"
    s:int = 1  
    for i in range(1, factorial(k)):  
        s *= (-1)*i*() _???
    return s
    
    
    
    
    
    