
def tablaMultiplicar(numero): #Definimos la funcion que recibira como parametro el numero de la tabla a realizar
    for i in range(11): #Bucle que recorrera del 0 al 10 (se pone 11 ya que el valor que se pone solo se toma hasta el anterior)
        resultado = i * numero #Multiplicamos el ietrador por el numero de tabla y lo guardamos en resultado
        print("{} x {} = {}".format(numero,i,resultado)) #Mostramos el resultado 

#Pedimos el numero de la tabla 
numeroTabla = int(input("Ingrese la tabla de multiplicar a conocer: "))

#Llamamos a la funcion y le pasamos como argumento el numero de tabla que ingreso el usuario
tablaMultiplicar(numeroTabla)