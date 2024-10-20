#ACTIVIDAD 6 - ENTREGA 1:
#Ruta al archivo. 
proyecto = '../../' 
filepath = proyecto + "resources/palabras_random.csv"

def contador_palabras(filepath: str, sep: str, p:str, encoding='utf-8') ->int:
    p = p.lower()  
    n_palabra = 0
    with open(filepath, 'r', encoding=encoding) as f:
        for linea in f:
            linea = linea.lower()  
            terminos = linea.split(sep)   
            n_palabra += terminos.count(p)  
    return n_palabra  

#ACTIVIDAD 7 - ENTREGA 1:
def cont_lineas(filepath: str, cad: str) ->int:
    ls: list[str] = []
    with open(filepath, 'r') as f:
        for linea in f:
            if cad.lower() in linea.lower():  
                ls.append(linea.strip())  

    return ls

#ACTIVIDAD 8 - ENTREGA 1:
def p_unicas(filepath, sep=' '):
    n_palabras = {}  
    with open(filepath, 'r') as f:
        for linea in f:
            linea = linea.lower()
            terminos = linea.split(sep)
            for termino in terminos:
                palabra = termino.strip()
                if palabra: 
                    if palabra in n_palabras:
                        n_palabras[palabra] += 1  
                    else:
                        n_palabras[palabra] = 1  
    palabras_unicas = [palabra for palabra, conteo in n_palabras.items() if conteo == 1]
    return palabras_unicas

#ACTIVIDAD 9 - ENTREGA 1:
from typing import Optional

def longitud_promedio_lineas(filepath: str) -> Optional[float]:
    total_palabras = 0  
    total_lineas = 0
    with open(filepath, 'r') as f:
        for linea in f:
            linea = linea.lower()
            palabras = linea.split(',') 
            n_palabras = len(palabras)  
            total_palabras += n_palabras  
            total_lineas += 1  
    # Evitar división por cero
    if total_lineas == 0:
        return None
    
    # Calcula la longitud promedio de palabras por línea
    longitud_promedio = total_palabras / total_lineas
    return longitud_promedio

resultado = longitud_promedio_lineas(filepath)

if resultado is not None:
    print(f"La longitud promedio de palabras por línea es: {resultado:.2f}")
else:
    print("No se pudo calcular la longitud promedio.")
    
