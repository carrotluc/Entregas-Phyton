'''
Created on 18 sept 2022

@author: migueltoro
'''
'''
from typing import Iterable
from us.lsi.tools.Iterable import distinct, flat_map, iterate
from us.lsi.tools.File import lineas_de_csv,absolute_path, iterable_de_fichero, encoding
from itertools import accumulate
from operator import mul
import re
'''
'''
APUNTES
(exp(x) for x in iterable if p(x)): Generador
[exp(x) for x in iterable if p(x)]: Lista
{exp(x) for x in iterable if p(x)}: Conjunto
{exp1(x):exp2(x) for x in iterable if p(x)}: Diccionario'''
'''
def test0():
    print(encoding(absolute_path('/resources/lin_quijote.txt'))) #Sirve para preguntarle qué encoding tiene

def test1():
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            pass
        
    r:Iterable[int] = (x**2 for x in range(3, 70) if x % 3 == 0)
    
    for e in r:
        print(e)
    
def test2():
    sr: list[int] = []
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sr.append(t)

    s:list[int] = [x**2 for x in range(3, 70) if x % 3 == 0]
    print(s)
    print(sr) 
    'Similar al lambda, sigue la estructura:
    [exp(x) for x in iterable if p(x)],
    siendo p(x) el predicado: '''
    
        
def test3():
    sts: set[int] = set()
    for x in range(3, 70):
        if x % 3 == 0:
            t = x**2
            sts.add(t)
        
    st:set[int] = {x**2 for x in range(3, 70) if x % 3 == 0} #'''MISMA ESTRUCTURA PARA EL CONJUNTO,
    #SON LLAMADAS LISTAS DE COMPRENSIÓN, SE DIFERENCIAN EN QUE UNO ES CON LLAVES Y EL OTRO CON CORCHETES'''
    print(sts)
    print(st)
    
def test4():
    dtr: dict[int,int] = {}
    for x in range(3, 70):
        if x % 3 == 0:
            t1 = x**2
            t2 = x**3
            dtr[t1] = t2

    dt:dict[int,int] = {x**2:x**3 for x in range(3, 70) if x % 3 == 0}
    print(dtr)
    print(dt)
    
def test5():
    nombres:list[str] = ["Miguel", "Ana", "Jose Maria", "Guillermo", "Maria", "Luisa"] 
    #'''Esta función está definida de forma explícita'''
    ranking:dict[str,int] = {nombre: nombres.index(nombre) for nombre in nombres} 
    #'''nombres.index(nombre) te dice la posición del nombre'''
    #'''Esta función está definida por comprensión'''
    print(f'ranking = {ranking}')

def test6():  
    texto:str = "este es un pequeño texto para probar la siguiente definicion por comprension"
    iniciales:set[str] = {p[0] for p in texto.split()}
    palabras: set[str] = {p for p in texto.split()}
    palabras_por_iniciales: dict[str, list[str]] = {c: [p for p in palabras if p[0]==c] for c in iniciales}
    print(f'palabras_por_iniciales = {palabras_por_iniciales}')
    
def test7():
    fichero:str= absolute_path("/datos/datos_3.txt")
    it3:Iterable[list[str]] = lineas_de_csv(fichero)
    it4:Iterable[str] = flat_map(it3,key=lambda x:x) 
    print(list(it4)) #Debe declararse como lista, ya que si sólo es iterable NO puede imprimirse
    #El flat_map sirve para covertir una lista dentro de una lista en una lista a secas
    it5:Iterable[int] = map(lambda e:int(e),it4)
    #Map es una función que coje un iterable y lo convierte en otro. 
    it6:Iterable[int] = distinct(it5)
    #Distinct coje un iterable y elimina los repetidos.
    r0:list[int] = sorted(it6,key=lambda x:x)
    #Sorted coje un  iterable y lo ordena, convirtiéndolo en una lista. 
    
    print(f'sorted = {r0}')
    
def test8():
    r7:Iterable[str] = flat_map(iterable_de_fichero(absolute_path("/datos/datos_3.txt")),key=lambda ln: re.split(',',ln))
    print(list(r7))
    print('________________')
    r8:Iterable[str] = flat_map(lineas_de_csv(absolute_path('/resources/lin_quijote.txt'), encoding='ISO-8859-1',delimiter=' '))
    #Un csv es un fichero que cada elemento de la línea está separado por coma (si quieres cambiarlo: delimiter='loquesea')
    r9:Iterable[str] = filter(lambda x: len(x)>0,r8)
    print(list(r9))
    
def test9():
    cadena:str = "lunes,martes,miercoles,jueves,viernes,sabado,domingo"
    it7:Iterable[tuple[int,str]] = enumerate(cadena)
    it8:Iterable[tuple[int,str]] = filter(lambda e:e[0]%2==0,it7)
    it9:Iterable[str] = map(lambda e: e[1],it8)
    print(list(it9))
    
def test10():
    a:int = 0
    b:int = 200
    c:int = 5
    d:int = 4
    it1:Iterable[int] = map(lambda x:x**2,range(a,b,c))
    it2:Iterable[int] = filter(lambda x:x%d==0, it1)
    print(list(it2))
    
def test11():
    versions:list[int] = [14, 3, 6]
    r5:Iterable[int] = accumulate(versions,mul)
    print(list(r5))
    
def test12():
    r6:Iterable[int] = iterate(3,lambda x:x*7,lambda x: x<1000)
    print(f'Iterate = {list(r6)}')
    
def test13():
    languages:list[str] = ['Java', 'Python', 'JavaScript']
    versions:list[int] = [14, 3, 6]   
    r1:Iterable[tuple[str,int]] = zip(languages, versions)
    print(list(r1))
    dias:list[str] = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
    r2:Iterable[tuple[int,str]] = enumerate(dias)
    r3:list[tuple[int,str]] = list(r2)
    print(list(r3))
    r4:dict[int,str]  = dict(r3)
    print(r4)


def test14():
    #Definir un diccionario que asocie la segunda letra de cada palabra, todas las palabras que tengan la s en la segunda posición"
    texto:str = "Tu puta madre la muy perra"
    iniciales:set[str] = {p[1] for p in texto.split()}
    palabras: set[str] = {p for p in texto.split()}
    palabras_por_iniciales: dict[str, list[str]] = {c: [p for p in palabras if p[1]==c] for c in iniciales}
    print(f'palabras_por_iniciales = {palabras_por_iniciales}')

if __name__ == '__main__':
    test14()
    