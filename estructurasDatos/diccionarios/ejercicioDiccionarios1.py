"""En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}"""

capitales = {
      "Guatemala": "Ciudad de Guatemala",
      "El Salvador": "San Salvador", 
      "Honduras": "Honduras",
      "Nicaragua": "Managua", 
      "Costa Rica": "San Jose",
      "Panama": "Panama",
      "Argentina": "Buenos Aires",
      "Colombia": "Bogota",
      "Venezuela": "Caracas",
      "España": "Madrid"
}

#El usuario ingresa el pais
inputPais = input("Ingresa el pais para consultar la capital: ")
#Capitalizamos el input, es decir, le damos la primera letra en mayuscula porque las keys en el diccionario inician en mayus
paisCapitalizado = inputPais.capitalize().replace(' ','')
print(paisCapitalizado)
#Condicional que indica si el pais con la primera letra en mayus esta dentro del diccionario capitales
if paisCapitalizado in capitales:
    #Si es true imprimira lo que se encuentre en la consulta del value pasandole la key, diccionario[key] 
    print(capitales[paisCapitalizado])
else: #Si es false muestra que no se encuentra la informacion
    print("No data found")


# Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
#                 'P 0 3 ': 'Soft Computing'};

# Product_list = {x.replace(' ', ''): v 
# for x, v in Product_list.items()}

# print (" New dictionary : ", Product_list)