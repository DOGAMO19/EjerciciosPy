# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    resultado = 1
    i = 1
    while i <= numero:
        resultado = i * resultado
        i += 1
        print(resultado) 

numeroFactorial = int(input("Ingrese el numero que desea conocer su factorial: "))

factorial(numeroFactorial)