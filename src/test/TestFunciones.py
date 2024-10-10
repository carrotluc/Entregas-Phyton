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
    
    
#########################################################################
if __name__ == '__main__':
    print(test1())
    print(test2())
    print(test3())



