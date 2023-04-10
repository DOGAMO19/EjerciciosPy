#Una lista es un array; un array es un conjunto de datos ordenados
#Las listas pueden ser homogeneas (un mismo tipo de dato) o heterogeneas (diferentes tipos de datos)

#Declaracion 
myLista = [ "Daniel", 98, "vaso", False, 34.98, [1,2,3,4,5] ]

print(myLista) #Imprimimos la lista 
print(len(myLista)) #Imprime el tamanio de la lista (numero de elementos que tiene la lista) (comienza de 1 no de 0)

#Modifica el elemento en la posicion 1 de la lista
myLista[1] = "Aqui antes era un 98"

#Obtenemos un valor de la lista donde el elemento es otra lista
print(myLista[5][2])
print(myLista)


#Debanado de listas (obtener elementos de la lista)

print(myLista[0:3]) #Obtiene los elementos en la posicion 0,1 y 2
print(myLista[ : 4]) #Obtiene los elementos en la posicion 0,1,2 y 3
print(myLista[3: ]) #Obtiene los elementos desde la posicion 3 hasta el elemento final de la lista
print(myLista[-1]) #Obtiene el ultimo elemento de la lista
print(myLista[-4 : -2]) #Obtiene el elemento en la posicion 4 hasta la 2 en conteo en retroceso
print(myLista[ : :-1]) #Obtiene la lista, crea una copia de ella y la muestra al reves

