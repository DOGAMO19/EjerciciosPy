# Ejercicio 1

# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

lista = [20, 50, "Curso", 'Python', 3.14]

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

lista[0] = nombre
lista[1] = apellido

print(lista)