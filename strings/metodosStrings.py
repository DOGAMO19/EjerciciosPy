contenido = "texto a utitlizar en metodos de strings para practicar"
contenidoMayusculas = "TEXTO EN MAYUSCULAS PARA PRACTICAR LOS METODOS DE STRINGS"
contenidoMayusMins = "TexTo CoN PaLabras En MinS Y MayUs"
print(len(contenido)) #Devuelve el tamanio de la cadena
print(contenido.upper()) #Convierte el texto a mayusculas 
print(contenidoMayusculas.lower()) #Convierte el texto a minusculas
print(contenido.capitalize()) #Agrega mayusuclas a los inicios de las frases
print(contenido.title()) #Agrega mayusculas al inicio de cada palabra
print(contenidoMayusMins.swapcase()) #Convierte las mayus a mins y viceversa


#Ejercicio 1 Strings 

'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

amigo = "Te quiero solo como amigo"

print(amigo[0 : 2]) #Imprime los dos primeros caracteres (0 y 1) se coloca 2 porque el 2 no se imprime toma un -1
print(amigo[-3 : ]) #Impime los ultimos 3 caracteres de la cadena. -3 es el inicio hasta el final del string
print(amigo[ : : 2 ]) #Imprime cada dos caracteres de la cadena. Crea una copia del string [ : ] y luego indica el salto [ :2] -> [ : : 2]
print(amigo[ : : -1]) #Imprime el string a la inversa. Se crea una copia de la cadena [ : ] y el tercer parametro indica como imprimirlo, en este caso es desde el ultimo caracter del string ira imprimiendo -> [ : : -1]
print(amigo + amigo[ : : -1]) #Imprime la cadena original y se le concatena la cadena pero a la inversa


#Ejercicio 2 
'''Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); 
e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r'''

cadenaEjercicioDos = "eparado"
#El metodo replace sustituye un valor/caracter de la cadena por uno nuevo. El primer parametro es el caracter a remplazar y el segundo 
#parametro es el nuevo caracter/palara por la que se remplzara. Existe un tercer parametro que es el numero de veces que se remplazara
# En este caso agregamos la S por parte para que no aparezaca una coma al inicio de la palabra 
print("S",cadenaEjercicioDos.replace('',',')) 