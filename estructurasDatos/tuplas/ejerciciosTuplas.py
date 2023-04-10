'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

#Creamos la tupla con los meses del anio 
mesesAnio = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

#Pedimos al usuario ingresar el numero de mes
numeroMes = int(input("Ingresa el numero de mes que deseas conocer: "))

#Condicional si el numero que ingresa el usuario es menor o igual a 12, ya que no hay mas de 12 meses
if numeroMes <= 12:
    print(mesesAnio[numeroMes -1]) #Imprime el mes dado el numero que ingreso, pero se le resta 1 al numero que ingreso porque la tupla inicia en 0 
else: #Si el valor es mayor a 12 
    print("El numero de mes no coincide")

