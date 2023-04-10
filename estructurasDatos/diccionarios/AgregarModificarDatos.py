
#Creamos el diccionario cliente
cliente = { 
    "nombre": "Daniel",
    "apellido": "Garcia",
    "edad": 22,
    "estatura": 1.76
}

#Imprime todo el diccionario con keys y values
print(cliente)

#Imprime las keys del dicionario
print(cliente.keys())

#Imprime los values del diccionario
print(cliente.values())

#Imprimir el value por su key 
print(cliente["nombre"])

#Agregar un nuevo key con su value al diccioanrio
cliente["ocupacion"] = "estudiante"
print(cliente)

#Modificar el value de un key 
cliente["nombre"] = "Osvaldo"
print(cliente)