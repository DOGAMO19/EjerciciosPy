class Rectangulo: 
    '''
    Clase que calculara el area de un rectangulo a traves del ingreso por consola de la base y la altura
    '''

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area_rectangulo(self):
        return self.base * self.altura
    
base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: "))
    
rectangulo1 = Rectangulo(base, altura)
print(f"El area de tu rectangulo es: {rectangulo1.calcular_area_rectangulo():.2f}")