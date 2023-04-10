
condicionInicial = 0

#While que verifica si la condicionInicial es menor a 10, si es verdadera ejecutara todo el codigo que este dentro
while condicionInicial < 10:
    print(condicionInicial) #Imprime del 0 al 9
    condicionInicial += 1 #Suma de 1 en 1 cada que pase la condicion
else:
    print("La condicion ya no es verdadera. El bucle ha terminado")

#Segundo Ejemplo *******************************************************************************************
valor = 0

while valor < 20: 
    valor += 1 #Aumenta de 1 en 1 cada que la condicion del while es valida
    if valor == 18: #Condicion si el valor es igual a 18
        print("Detener Bucle")
        break #Con break finalizamos el bucle, esto se da cuando tenemos condiciones especificas 
    print(valor) #Imprime cada aumento de 1 en 1 que se va realizando en valor