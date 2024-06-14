class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # el decorador @classmethod me permite hacer "referencia" del método de la clase sin realizar instancias de la clase
    @classmethod
    def habla(cls):
        print("Wuaf!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)

perro1 = Perro("chanchito", 2)
perro2 = Perro("felipe", 3)
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)
Perro.habla()
