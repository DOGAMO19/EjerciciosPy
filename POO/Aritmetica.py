class Aritmetica:
    '''
    Clase Aritmetica que realizara las operaciones de restar, multiplicar, dividir, sumar, etc. 
    '''
    def __init__(self, valorA, valorB):
        self.valorA = valorA
        self.valorB = valorB
    
    def sumar(self):
        return self.valorA + self.valorB
    
    def restar(self):
        return self.valorA - self.valorB

    def multiplicar(self):
        return self.valorA * self.valorB
    
    def dividir(self):
        return self.valorA / self.valorB

aritmetica1 = Aritmetica(10,10)
print(f"La suma de los dos digitos es: {aritmetica1.sumar()}")
print(f"La resta de los dos digitos es: {aritmetica1.restar()}")
print(f"La multiplicacion de los dos digitos es: {aritmetica1.multiplicar()}")
print(f"La division de los dos digitos es: {aritmetica1.dividir():.2f}")