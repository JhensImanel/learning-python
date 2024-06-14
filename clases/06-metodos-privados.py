class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre #para que la propiedad sea privada se le coloca __x delante de x.
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Wuaf!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
print(perro1.__dict__)
#__dic__ es un diccionario que contiene todas las propiedades que tiene una instancia de un objeto
#retorna {'_Perro__nombre': 'Chanchito feliz', 'edad': 4}, para nombrar una propiedad privada debo copiar el primero
#print(perro1,_Perro__nombre) el cual me retorna el valor del nombre(propiedad privada)