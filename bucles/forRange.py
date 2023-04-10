#El range es un rango delimitado el cual podra recorrer el bucle 
#Range puede tomar 3 valores en su declaracion range(valorInicial, valorFinal, tipoSalto), donde el valorInicial siempre debe ser menor al valorFinal. tipoSalto es el parametro con el cual se recorrera dentro del rango 
#El valorFinal sera un parametro que se tomara en cuenta solo al anterior del declarado, es decir, si declaramos 10 solo tomara en cuenta hasta el 9


for i in range(0,21,5): #Bucle que recorre del 0 al 20 en saltos de 5 en 5 
    print(i)

print("**************")  

for j in range(-10,0): #Bucle que recorre del -10 al -1
    print(j)