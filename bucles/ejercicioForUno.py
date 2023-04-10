# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

#pedimos los valores de inicio y fin al usuario
inicioUsuario = int(input("Ingrese el inicio de su serie numerica: "))
finUsuario = int(input("Ingrese el fin de su serie numerica: "))

#Recorremos con un range los valores dados por el usuario pero, a finUsuario le sumamos un 1 para que tome el valor que ingreso el usuario (si ingresa 20 va a tomar el 2o tomando como limite el 21, recordando que no se toma el 20 en cuenta si ese es el numero elegido como limite)
for i in range(inicioUsuario,finUsuario+1): 
    print(i)