#Operadores Relacionales 
numero1 = 700
numero2 = 500
numero3= 700 

texto1 = "Cadena de pruebas"
texto2 = "Cadena de pruebas mas larga"
texto3 = "Cadena de pruebas"

#Comparacion de numeros
print(numero1 > numero2) #True 700 es mayor que 500
print(numero1 < numero2) #False 700 no es menor que 500
print(numero1 <= numero3) #True 700 no es menor que 700 pero si es igual a 700
print(numero2 >= numero1) #False 500 no es mayor ni igual a 700
print(numero1 == numero3) #True 700 es igual a 700

#Comparacion de cadenas
print(texto1 > texto2) #False la cadena 1 no es mas larga que la cadena 2 
print(texto1 == texto3) #True ambas cadenas son iguales
print(texto2 < texto3) #True la cadena 2 es mas corta que la cadena 3


#Operadores Logicos 

#and (ambas condiciones deben ser verdaderas para que sea true)
print(10 > 9 and 100 > 99) #True porque tanto como 10 es mayor que 9 y 100 es mayor que 99
print(1 > 100 and 100 == 100) #False porque 1 no es mayor que 100 pero 100 si es igual a 100, sin emabargo en and ambos tienen que ser true 

#or (aunque una condicion se verdadera sera true)
print(texto2 > texto1 or 1000 < 1) #True porque texto2 si es mas larga que texto1 aunque 1000 no es menor que 1, una es verdadera entonces es true
print(10 == 11 and 15 > 16) #False porque 10 no es lo mismo que 11 y 15 no es mayor que 16

#not (cambia el valor de la condicion, si es true la cambia a false y si es false la cambia a true)

print(not 10==10) #False, aunque 10 si es lo mismo que 10 y da true el not lo cambia a false


#Ehjercicios ****************************************************************************************************









