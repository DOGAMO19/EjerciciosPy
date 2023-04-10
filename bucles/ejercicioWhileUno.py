# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

#Pedimos la tabla a realizar
tabla = int(input("Ingrese la tabla de multiplicar a mostrar: "))

i = 1 #Inicializamos el iterador en 1 
resultado = 0  #Creamos una variable donde se ira guardando el resultado de multiplicar la tabla por el iterador

#Bucle mientras i sea menor o igual a 10, el igual se pone para que tome en cuenta el 10
while(i <= 10):
    resultado = i * tabla #Se realiza la multiplicacion del numero ingresado por cada ieteracion 
    print("El mutiplicar {} por {} es igual a: {}".format(tabla,i,resultado))
    i += 1 #Aumenta de 1 en 1 el iterador