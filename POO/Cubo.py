class Cubo:
    '''
    Clase donde se realizara el volumen de un cubo
    '''

    def __init__(self,ancho,profundidad, altura) -> None:
        self.ancho = ancho
        self.profundidad = profundidad
        self.altura = altura

    def calcular_volumen(self):
        return self.ancho * self.profundidad * self.altura
    
ancho = float(input("Ingresa el ancho del cubo: "))
profundidad = float(input("Ingresa la profundidad del cubo: "))
altura = float(input("Ingresa la altura del cubo: "))

cubo1 = Cubo(ancho,profundidad,altura)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")