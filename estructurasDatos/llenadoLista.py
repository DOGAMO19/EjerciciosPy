#Sumar dos listas. La suma es la unica operacion que se puede hacer con listas

lista1 = [1,2,3]
lista2 = [4,5,6]

#Sumamos las dos listas (juntamos) y obtenemos una sola lista
lista3 = lista1 + lista2

#Concatenar una lista. Para concatenar una lista no se puede usar el mas (+), se debe hacer con coma (,)
print(lista3)
print("La lista de ambas listas es: ",lista3)

#Llenado de lista manual 
#Declaramos la lista vacia
listaVacia = []
#PEdimos la edad por consola
edad = int(input("Ingresa tu edad: "))
listaVacia.append(edad) #Agregamos el valor que se ingrese por consola a la lista
print(listaVacia)