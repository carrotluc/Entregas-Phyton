from Lecturas.lecturas import cont_lineas, contador_palabras, p_unicas, longitud_promedio_lineas

#CAMBIAR EN FUNCIÓN DEL FICHERO CON EL QUE SE QUIERA TRABAJAR
proyecto = '../../' 
filepath = proyecto + "resources/lin_quijote.txt"
################################################################################
#EJEMPLO 6:
def test1():
    resultado = contador_palabras(filepath, ' ', 'quijote')
    print(f'La palabra "proyecto" aparece {resultado} veces.')
################################################################################
#EJEMPLO 7:
def test2():
    cadena = 'quijote'  
    resultado = cont_lineas(filepath, cadena)
    print(f'La palabra {cadena} aparece en las líneas {resultado}')
################################################################################
#EJEMPLO 8:
def test3():
    print(p_unicas(filepath, ' '))
################################################################################
#EJEMPLO 9:
def test4():
    resultado = longitud_promedio_lineas(filepath)
    if resultado is not None:
        print(f"La longitud promedio de palabras por línea es: {resultado:.2f}")
    else:
        print("No se pudo calcular la longitud promedio.")
################################################################################
if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
