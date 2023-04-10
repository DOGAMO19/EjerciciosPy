#Un conjunto es una estructura de datos que nos permite tener agrupados dichos datos, estos datos no puden repetirse dentro de un mismo conjunto

#Sintaxis de declaracion de un conjunto

#sintaxis 1 
primerConjunto = {1,2,3,4,5} 

#sintaxis 2
segundoConjunto = set[(1,2,3,4,5)]

#sintaxis 3
tercerConjunto = set((1,2,3,4,5,5,5,5)) #Al impirmir este conjunto solo saldra una vez el 5 , ya que no se pueden repetir

print(tercerConjunto)

print(type(primerConjunto)) #Devuelve set(conjunto)
print(type(segundoConjunto)) #Devuelve types.GenericAlias = Conjunto
print(type(tercerConjunto)) #Devulve set