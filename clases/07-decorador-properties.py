class Perro():
    def __init__(self, nombre):
        self.nombre = nombre,

     #me genera una propieda privada
    @property
    def nombre(self): #property se debe usar con los métodos que devuelven un valor (getter)
        print("pasando por el getter")
        return self._nombre

    #esta función me retorna vacío
    @nombre.setter
    def nombre(self, nombre): #método que setea un valor
        print("pasando por el setter")
        if nombre.strip():
            self._nombre = nombre
        return

perro = Perro("Choclo")
print(perro.get_nombre())