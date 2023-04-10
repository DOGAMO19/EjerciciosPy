#For se encarga de iterar elementos iterables (listas, diccionarios, tuplas), ya que el iterador tomara cada valor del elemento

dictionario = {
    "name": "daniel",
    "apellido": "garcia",
    "edad": 22,
    "ocupacion": "estudiante",
    "trabaja": False
}

lista = [1,2,3,4,"daniel", "python", "basico", 5,6,7]

tupla = ("esta", "es", "mi", "tupla", 1,2,3,4)


for i in dictionario.values():
    print(i)

print("****************************************")

for j in lista:
    print(j)


print("****************************************")


for k in tupla:
    print(k)