# Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

#Pedimos el inicio y fin de la serie para el range
inicioUsuario = int(input("Ingrese el inicio de su serie numerica: "))
finUsuario = int(input("Ingrese el fin de su serie numerica: "))

impar = [] #lista para guardar los numeros impares

#Recorremos con for en range el inicio y el final, se le agrega un 1 a finUsuario para que tome en cuenta el limite establecido
for i in range(inicioUsuario, finUsuario+1):
    if i % 2 != 0: #condicional si el residuo de la division entre cada valor (iterador) entre 2 es diferente de 0 (numero impar)
        impar.append(i) #Si el residuo es diferente de 0 se agrega a la lista impar con append agregando el iterador (i)

print(impar) #Imprimimos la lista una vez realizado todo el bucle



'''Otra forma de resolver este problema es con continue'''

# for j in range(inicioUsuario, finUsuario+1):
#     if j % 2 == 0:
#         continue #Si el residuo de la division del iterador entre 2 es igual a 0 (numero par) se salta esa eejcucion
#     print(j) #Si el residuo no es igual a 0 (impar) imprime el valor del iterador

