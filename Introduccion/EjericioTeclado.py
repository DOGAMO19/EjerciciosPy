#Importamos la lireria math para poder hacer uso de sqrt
import math


#ejercicio 1 - Formula General 
'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

#Condicional para saber si la resta de los valores dentro de la raiz es negativa, si es negativa arroja un comentario , si no arroja los resultados
if((b**2) - (4*a*c)) < 0:
    print("La raiz es negativa")
else: 
    resultadoNegativo = ((-b) - (math.sqrt((b**2) - (4*a*c))))/ (2*a)
    resultadoPositivo = ((-b) + (math.sqrt((b**2) - (4*a*c))))/ (2*a) 
    resultadoFinal = resultadoPositivo, resultadoNegativo
    print(resultadoFinal)

'''Ejercicio 2
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''


practicaUnoCalificacion = int(input("Caliicacion Primera Practica: "))
practicaDosCalificacion = int(input("Caliicacion Segunda Practica: "))
practicaTresCalificacion = int(input("Caliicacion Tercera Practica: "))
examenParcialCalificacion = float(input("Calificacion del Examen Parcial: "))
examenFinalCalificacion = float(input("Calificacion del Examen Final: "))

# Sacamos el promedio de las 3 practicas entregadas para despues sumarlo a la de los examenes (se divide entre 3 porque son 3 practicas las evaluadas)
practicasPromedio = int((practicaUnoCalificacion + practicaDosCalificacion + practicaTresCalificacion) / 3)
# Sacamos el premedio total del estudiante (se divide entre 3 el resultado de la suma porque son 3 calificaciones a evaluar)
promedioTotal = ((practicasPromedio + examenFinalCalificacion + examenParcialCalificacion) / 3)

print(promedioTotal)
