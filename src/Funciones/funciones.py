#ACTIVIDAD 1 - ENTREGA 1:
def calcular_producto(n, k) -> int:
    #Verificar que n > k:
    if n <= k:
        return "ERROR: n debe ser mayor que k"
    s = 1  #Puesto que i=0, el for se inicia en 1. 
    for i in range(k + 1):  
        s *= (n - i + 1) 
    return s
#EJEMPLO 1:
n=11
k=1
r = calcular_producto(n,k)
print(f'Para el caso de n={n} y k={k}, la solución del enunciado será {r}.')