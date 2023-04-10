nombreUsuario = "Daniel Garcia"
edadUsuario = 22

#Muestra en pantalla el texto con la informacion de las variales, en format deben de ir en orden como queremos que aprezcan en el texto
print("Hola {} tu tienes {} anios de edad".format(nombreUsuario, edadUsuario))

'''Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

# vocal = input("Ingresa una vocal en minuscula:")
# # letra = input("Igresa cualquier letra: ")

# if(vocal != "a" or "e" or "i" or "o" or "u"):
#     print("El caracter ingresado no es una vocal")
# else:
#     print("Tu vocal en mayus es:\n",vocal.upper())

'''Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo: ")

print("Tu nombre es:\n {} \nTu edad es:\n {} \nTu sexo es:\n {}".format(nombre, edad, sexo))