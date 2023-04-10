# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#Pedimos la edad al usuario
edad = int(input("Ingrese su edad: "))

#Inicializamos el iterador
i = 1 

#Bucle con condicion de si el iterador es menor o igual (para que tome en cuenta el ultimo numero) a la edad se ejecute 
while (i <= edad): 
    print("Cumpleanios numero: {}".format(i)) #Muestra todos los anios 
    i+=1 #Aumentamos en 1 al iterador 
    