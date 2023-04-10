# Ejercicio 1

# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letraUsuario = input("Ingresa la letra a verificar: ")

if(letraUsuario in 'aeiou'): #if in verifica que letraUsuario este en la cadena aeiou, si esta en la cadena devuelve True , caso contrario devuelve False
    print("Tu letra es vocal")
else: 
    print("Tu letra no es una vocal")