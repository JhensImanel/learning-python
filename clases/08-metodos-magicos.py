class Perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self): #método destructor
        print(f"Chao perro {self.nombre}")

    def __str__(self): #método string
        return f"Clase perro: {self.nombre}"

     #me genera una propieda privada
    def habla(self):
        print(f"{self.nombre} dice Guau!")

perro = Perro("Chanchito", 8)
# texto = str(perro)
# print(texto)
del perro