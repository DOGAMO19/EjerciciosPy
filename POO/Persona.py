class Persona: 
    def __init__(self, nombre, apellido, edad, *valoresTupla, **valoresDiccionario): #Creamos los atributos que tendran los objetos que se instancien desde la clase, self hace referencia al mismo objeto que se crea, el usar un asteristica significa que sera una lista de valores en formato tupla y si colocamos dos asteriscos significa que seran valores en formato de un diccionario
        self.nombre = nombre #Creamos el atributo nombre, el que tiene self es el atributo de la clase y el que no tiene es el parametro que recibe
        self.apellido = apellido
        self.edad = edad
        self.valoresTupla = valoresTupla
        self.valoresDiccionario = valoresDiccionario

    def imprimir_valores(self): #Creamos el metodo imprimir_valores para los objetos, se coloca el self para que tome como referencia al objeto que llame al metodo
        print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valoresTupla} {self.valoresDiccionario}") #Imprimimos los valores, ingresamos a los valores de la clase con el self

persona1 = Persona("Daniel", "Garcia", 22, "Este","Sera","mi tupla", 1,2,3,4,5, lenguaje = "Python", objetivoUno="Ciberseguridad", objetivoDos="Analisis De Datos") #Creamos la instancia (objeto) persona1 de la clase Persona y le pasamos por argumento los atributos que necesita, los valores desde "Este" hasta el numero 5 sea una tupla y los ultimos  seran parte de un diccionario
persona1.imprimir_valores() #Mandamos a llamar al metodo desde la instancia persona1
# print(persona1.nombre,persona1.apellido,persona1.edad) #Imprimimos los atributos que tiene la clase

persona2 = Persona("Fernanda","Vazquez",21)
persona2.imprimir_valores() #Mandamos a llamar al metodo desde la instancia persona2
# print(f"Persona2: {persona2.nombre} {persona2.apellido} {persona2.edad}")


