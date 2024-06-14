class Perro:
    patas = 4 #instanciando patas

    def __init__(self, nombre, edad): #constructor
        self.nombre = nombre
        self.edad = edad

    def habla(self): #método
        print(f"{self.nombre} dice: Wuaf!")

Perro.patas = 3 #se instancia un nuevo valor a patas
mi_perro = Perro("Chanchito", 1) #se instancia valores a los atributos de Perro
mi_perro.patas = 5 #se cambia el valor de patas a la instancia de Pero
mi_perro2 = Perro("Felipe", 1) #se instancia valores a los atributos de Perro2
print(Perro.patas) #retorna 3

print(mi_perro.patas) #retorna 5
print(mi_perro2.patas) #retorna 3