# Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

letrasAbecedario = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

numeroUsuario = int(input("Ingrese el numero de letra: "))

#Condicional que pregunta si el numero que ingresa el usuario es menor o igual a 26 (total de letras) y mayor que 0 
if numeroUsuario <=26 and numeroUsuario > 0:
    #Si es valida imprime la letra que encuentre en el numero que ingreso el usuario menos uno, ya que la tupla inicia en 0 y como tal no hay 26 si no 25 , si ingresa el 2 imprimiria la letra c y no la b, por eso se resta una posicion 
    print(letrasAbecedario[numeroUsuario-1]) 
else: #Si ingresa un numero diferente 
    print("El numero no coincide con ninguna letra ") 