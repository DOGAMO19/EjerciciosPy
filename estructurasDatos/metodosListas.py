myList = [1,5,2,5,3,4,5]
addListInOtherList = ["Daniel", "Osvaldo", "Garcia", "Morales"]
objectAdd = {
    "name": "Daniel",
    "lastname" : "Garcia"
}

#Agrega un elemento al final de la lista
#myList.append(6) 

#Agrega un elemento a lista en una posicion definida, El primer valor es la posicion en la cual se va agregar el elemento del segundo valor
#myList.insert(1,"Nuevo Elemento")

#Cuenta cuantos elementos con el valor indicado existen en la lista. 
#print(myList.count(5)) #Regresa 3 porque hay 3 cincos en la lista

#Retorna la posicion del primer elemento en la lista del valor especificado
#print(myList.index(5)) #Regresa 1 porque el primer cinco en la lista esta en la posicion 1 

#Ordena la lista (en numero de menor a mayor)
#myList.sort()
#print(myList)

#Ordena la lista de forma inversa (al reves)
#myList.reverse()
#print(myList)

#Agrega un valor iterable (array, tuplas, string ) 
#myList.extend(addListInOtherList)
# myList.extend([9,8,7,6])

#Elimina un elemento de la lista en la posicion especificada, si no se coloca la posicion borrara el ultimo elemento de la lista
#myList.pop(3)

#Elimina el primer elemento de la lista que encuentre con el valor especificado
#myList.remove(2)
print(myList)