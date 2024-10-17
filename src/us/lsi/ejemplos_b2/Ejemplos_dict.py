'''
ESTO SÍ LO ENTIENDES EH :)))
Created on 6 nov 2022

@author: migueltoro
'''

from collections import Counter
import random

def test1():
    diccionario = {"clave1": "valor1", "clave2": "valor2","clave3": "valor3"}
    print(set(diccionario.keys()))
    print(set(diccionario.values()))
    print(set(diccionario.items()))
    
    
def test2():
    iterable:list[int] = (random.randint(0,100) for _ in range(100))
    frecuencias:Counter[int] = Counter(iterable)
    #CONTADOR: CUENTA CUÁNTAS COSAS HAY DE CADA y te devuelve el numero de veces que se repite. 
    #ESTRUCTURA --> counter(nombredeliterable). 
    mc:list[tuple[int,int]] = frecuencias.most_common(5)
    #MOST COMMON ES UNA FUNCIÓN de PUNTO (MÉTODO): nombrelista.most_common[número de veces que se repite]
    fc:tuple[int,int] = frecuencias.most_common(1)[0][0] #Se repite 1,  vez es el número 1 de la lista y, a su vez, el 1 de la tupla de dentro de la lista
    print(frecuencias)
    print('____________')
    print(mc)
    print(fc)
    print('____________')
    print(set(frecuencias.keys()))
    print(set(frecuencias.values()))
    print(set(frecuencias.items()))
    print(frecuencias[22])
    
    
    print(frecuencias.get(22,0)) #Cuando un número no está o no lo encuentra, te pondrá un cero (porque tú así lo indicas)
    #Un iterable es todo aquello que se puede poner en un for. 
    

if __name__ == '__main__':
    test2()
    
    