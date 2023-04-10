verdadero = True
falso = False 

print(type(verdadero))
print(type(falso))


#Metodos Booleanos 

cadena1 = "Esta es una cadena"
cadena2 = "esta es una cadena escrita en minusculas"
cadena3 = "ESTA ES UNA CADENA ESCRITA EN MAYUSUCLAS"

print(cadena1.startswith("E")) #True porque la cadena1 si empieza con la letra E mayuscula
print(cadena1.startswith("Esta")) #True porque la cadena1 si empieza con el texto Esta

print(cadena1.endswith("a")) #True porque la cadena1 si termina con la letra a 
print(cadena1.endswith("e")) #False porque la cadena1 no termina con la letra e

print(cadena2.islower()) #True porque la cadena2 si esta escrita totalmente en minisculas
print(cadena3.isupper()) #True porque la cadena3 si esta escrita totalmente en mayusculas
print(cadena1.islower()) #False porque cadena1 tiene unas letras mayusculas