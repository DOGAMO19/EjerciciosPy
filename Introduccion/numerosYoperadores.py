numero1 = 19 
numero2 = 88.02

print(numero1)
print(float(numero1)) #Convierte el numero1 a flotante (esto es solo para que el lenguaje lo detecte)


print(numero2)
print(int(numero2)) #convierte el numero2 a entero  (esto es solo para que el lenguaje lo recnozca como entero)


#Jerarquia 

valor1 = 2
valor2 = 5
valor3 = 10
valor4 = 3

#Primero se hacen las operaciones que estan entre parentesis de forma interna, posteriomente se realizan las
#multiplicaciones y divisiones y al final las sumas y restas 
operacion = valor3 * (valor4 + valor2) / (valor3 - valor1)
#           (  10      *    8   )      /   (     8     )  = 10 
print(operacion)

#Ejercicio operacion aritmetica 1 **************************************
#( 3 + 2 / 2* 5 )^2

resultado = ((3+2) / (2*5) )**2
print(resultado)

#Ejercicio operacion aritmetica 2 
'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
realiza un programa que muestre el peso total de toda la venta.'''

pesoPayaso = 112
pesoMunieca = 75

clientePayasos = 23 
clienteMuniecas = 54

conversionKilos = 1000


calculoTotalPeso =  ((pesoPayaso * clientePayasos) + (pesoMunieca * clienteMuniecas)) / conversionKilos

print(calculoTotalPeso)