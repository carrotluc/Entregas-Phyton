#CAMBIAR EN FUNCIÓN DEL FICHERO CON EL QUE SE QUIERA TRABAJAR
proyecto = '../../' 
filepath = proyecto + "resources/lin_quijote.txt"
################################################################################
#EJEMPLO 6:

def contador_palabras(filepath, sep, p, encoding='utf-8'):
    p = p.lower()  
    n_palabra = 0
    with open(filepath, 'r', encoding=encoding) as f:
        for linea in f:
            linea = linea.lower()  
            terminos = linea.split(sep)   
            n_palabra += terminos.count(p)  
    return n_palabra 

def test1():
    resultado = contador_palabras(filepath, ' ', 'quijote')
    print(f'La palabra "proyecto" aparece {resultado} veces.')
################################################################################
#EJEMPLO 7:
def cont_lineas(filepath: str, cad: str) ->int:
    ls: list[str] = []
    with open(filepath, 'r') as f:
        for linea in f:
            if cad.lower() in linea.lower():  
                ls.append(linea.strip())  

    return ls

def test2():
    cadena = 'quijote'  
    resultado = cont_lineas(filepath, cadena)
    print(f'La palabra {cadena} aparece en las líneas {resultado}')
################################################################################
#EJEMPLO 8:
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
def test3():
    print(p_unicas(filepath, ' '))
################################################################################
#EJEMPLO 9:
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
    
    if total_lineas == 0:
        return None
    
    longitud_promedio = total_palabras / total_lineas
    return longitud_promedio
resultado = longitud_promedio_lineas(filepath)

if resultado is not None:
    print(f"La longitud promedio de palabras por línea es: {resultado:.2f}")
else:
    print("No se pudo calcular la longitud promedio.")
################################################################################
if __name__ == '__main__':
    test2()
