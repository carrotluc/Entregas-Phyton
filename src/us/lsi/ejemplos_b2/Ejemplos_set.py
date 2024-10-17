'''
Created on 6 nov 2022

@author: migueltoro
'''

a: set[int] = {1, 2, 3, 4, 5, 6}
b: set[int] = {4, 5, 6, 7, 8}
 #Se tratan como los intervalos en matemáticas. 
 
if __name__ == '__main__':
    print("Unión:", a | b) 
    #La unión son los no comunes y los comunes en orden. 
    print("Intersección:", a & b)
    #Intersección: sólo los comunes. 
    print("Diferencia:", a - b)
    #A b se le quitan los valores que tenga en común con a. Si fuese b - a sería al revés, 
    print("Diferencia simétrica:", a ^ b)
    print({7,8,1,2,3} == a ^ b)
    #Los números que a no en común en común con b . 
    print(2 in b-a)
    #¿El 2 pertenece al conjunto a-b?
    print(a & b >= a | b)
    
    
    #Indexado: 