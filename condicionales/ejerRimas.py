# Ejercicio 1

# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

cadena1 = input("Ingresa tu primera palabra: ")
cadena2 = input("Ingresa tu segunda palabra: ")

print(cadena1[-3: ])
print(cadena2[-3: ])

if(len(cadena1) < 3 or len(cadena2) < 3): #Comprabamos que las palabras sean mayores a 3 caracteres 
    print("Alguna de tus palabras es menor a 3 caracteres. Ingresa una palabra mas larga.")
elif( cadena1[-3: ] == cadena2[-3: ] ): #Si las ultimas 3 letras de la cadena1 es igual a las ultimas 3 letras de la cadena2
    print("Tus dos palabras riman")
elif( cadena1[-2: ] == cadena2[-2: ] ): #Si las ultimas 2 letras de la cadena1 es igual a las ultimas 2 letras de la cadena2
    print("Tus dos palabras riman, pero muy poco...")
else: #Si no son iguales las ultimas 3 o 2 letras de ambas cadenas las palabras no riman
    print("Tus dos palabras no riman en lo absoluto")