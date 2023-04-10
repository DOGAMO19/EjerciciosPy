# Ejercicio 2

# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

# Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula

# A = Rojo 
# B = Verde
# C = Azul

votoUsuario = input("Ingresa el candidato por el cual votas: ")

if( votoUsuario.upper() == 'A' ):
    print("Votaste por el partido Rojo")
elif(votoUsuario.upper() == 'B'):
    print("Votaste por el partido Verde")
elif(votoUsuario.upper() == 'C'):
    print("Votaste por el partido Azul")
else:
    print("Tu voto no ha sido reconocido...")