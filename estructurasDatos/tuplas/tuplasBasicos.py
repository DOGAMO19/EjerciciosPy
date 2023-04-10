#Una tupla es una estructura de datos que seran inmutales (siempre seran constantes)

#sintaxis de declaracion 1
tupla = (1,2,3,4,5,6)

#Sintaxis de declaracion 2
tupla2 = 1,2,3,4,5,6,7,8,9

#Acceder a un valor dentro de una tupla es igual que acceder a un valor de una lista
print(tupla[1]) #Imprime 2


#Podemos hacer debanado en tuplas 
print(tupla[ : : -1]) #imprime la tupla al reves
print(tupla[ : -1]) #imprime la tupla sin el ultimo elemento 
print(tupla[-1]) #Imprime el ultimo elemento de la tupla 
print(tupla[0:4]) #Imprime el 1,2,3,4
print(tupla[2: ]) #Imprime desde la posicion 2 hasta el final 
print(tupla[-3: ]) #Imprime desde la posicion -3 hasta el final


#Unir dos tuplas 
tuplaUnion = tupla + tupla2
print(tuplaUnion)