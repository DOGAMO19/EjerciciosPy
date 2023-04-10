myDictionary = { 
    "futbol": "mbappe",
    "tennis": "nadal",
    "americano": "lamar",
    "ufc": "moreno"
}

myDictionary2 = {
    "nombre": "daniel",
    "apellido" : "garcia",
    "edad": 22
}

print(myDictionary)

#Con pop() eliminamos el value del key que especifiquemos (tambien eliminara el key)
# myDictionary.pop("americano")
# print(myDictionary)

#Con clear() (no recibi ningun parametro) elimina todo el contenido del diccionario
# myDictionary.clear()
# print(myDictionary)

#Con get(key) obtiene el value de la key que se le debe de dar como parametro
# print(myDictionary.get("ufc"))

#Con setDefault(key , value) agrega un nuevo key con su value (esto si no existe), sino, retorna el valor de la key especificada
# myDictionary.setdefault("baseball", "urias")
# print(myDictionary)

#Con update actualizamos el diccionario con otro diccionario (se unen)
# myDictionary.update(myDictionary2)
# print(myDictionary)

#Con copy generamos una copia del diccionario 
# myDictionary.copy()
# print(myDictionary)
