#Importamos la lireria math para poder hacer uso de sqrt
import math

#Pedimos al usuario que ingrese su nombre por teclado 
nombreUsuario = input("Ingresa tu nombre de pila: ")

#Pedimos al usuario que ingrese su edad, le delcaramos int para indicar que lo trate como entero python 
edadUsuario = int(input("Ingresa tu edad: "))

#Pedimos al usuario que ingrese su estatura. Indicamos que python maneje este valor como flotante 
estaturaUsuario = float(input("Ingresa tu estatura en metros: "))
#Si nosotros no declaramos el int o float el valor que ingrese no sera numerico, sera un string

print(type(nombreUsuario))
print(type(edadUsuario))
print(type(estaturaUsuario))



