#if-else
edad = int(input("Ingresa tu edad para saber si eres mayor de edad: "))

if (edad >= 18):
    print("Ya eres mayor de edad!")
else:
    print("Aun no eres mayor de edad")

#Elif

letra = input("Ingresa una letra para saber si es vocal o no: ")

if letra.lower() == "a":
    print("Tu letra es la vocal A")
elif letra.lower() == "e":
    print("Tu letra es la vocal E")
elif letra.lower() == "i":
    print("Tu letra es la vocal I")
elif letra.lower() == "o":
    print("Tu letra es la vocal O")
elif letra.lower() == "u":
    print("Tu letra es la vocal U")
else:
    print("Tu letra no es una vocal")


#If anidados 

nombre = "Raul"
edadUsuario = 22

if(nombre == "Daniel"): #Primer if
    if(edadUsuario >= 18): #If anidado para saber si el usuario es Daniel y si es mayor de edad (2do If)
        print("Eres Daniel y eres mayor de edad")
    else:
        print("Eres Daniel pero no eres mayor de edad")
else:
    print("No eres Daniel")



