# Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numeroUsuario = int(input("Ingresa tu numero: "))

if(numeroUsuario < 0): #si el numero ingresado es negativo 
    print("El numero absoluto de {} es:".format(numeroUsuario),numeroUsuario * -1) #Si el numero ingresado es negativo se mulipica por -1 
    #print("El numero absoluto de {} es: {}".format(numeroUsuario, abs(numeroUsuario))) #abs() devuelve el valor absoluto de un numero
else:
    print("El numero absoluto de {} es: {}".format(numeroUsuario, numeroUsuario))