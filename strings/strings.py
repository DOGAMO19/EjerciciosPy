#Escapar caracteres (Literal Strings)

#Uso de \ (Indicar que un caracter que es usado para declaracion sea tratado como texto)
cadenaTexto = "Este es un \"string\" donde usamos comillas dobles dentro de un string declarado con comillas dobles"

print(cadenaTexto)

#Uso de \n (salto de linea) y \t (tab)

cadenaSaltoTab = "String donde existe un salto de linea.\n \t Y existe un tab al inicio del siguiente renglon"
print(cadenaSaltoTab)

#Concatenacion de cadenas  

nombreUsuario = "Daniel Osvaldo"
apellidoUsuario = "Garcia Morales"

#Concatenamos las dos variables que contienen un string para que se conviertan en un solo string
print(nombreUsuario,apellidoUsuario)

#En una variable guardamos la concatenacion de un texto y las dos variables
nombreCompleto = "El nombre del usuario es:" ,nombreUsuario + apellidoUsuario
print(nombreCompleto)

#Debanado o seperacion o substrings 

frase = "Esta es una fraase para hacer pruebas de substrings"

print(frase[0]) #Recupera y muestra la posicion 0 del string frase 
print(frase[0:3]) #Recupera y muestra desde la posicion 0 a la 2 del string (El limite no se toma en cuenta)
print(frase[ : 10]) #Recupera y muestra desde la posicion 0 a la 9 del string, cuando no se coloca un parametro de inicio se toma como 0
print(frase[ 10 : ]) #Recupera y muestra desde la posicion 10 hasta el final del string, cuando no se coloca un limite se toma como hasta el fin del string
print(frase[-1]) #Recupera y muestra la posicion 1 de atras para adelante del string (Cuenta regresiva)


