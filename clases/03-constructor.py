#en un constructor(__init__), self hace refencia a los métodos y atributos de instancia de la clase
class Perro:
    def __init__(self, nombre, edad): #__init__ funciona como un constructor en otros lenguajes que usan POO
        self.nombre = nombre #self hace referencia al atributo nombre
        self.edad = edad #self hace referencia al atributo edad

    def habla(self): #self hace referencia a los atributos de la superclase
        #f conocida como (f-string) tiene una funcionalidad parecida a los backticks (``) que me permite incrustar expresiones dentro de una cadena
        print(f"{self.nombre} dice: Wuaf!")

mi_perro = Perro("Chanchito", 1) #se le coloca valores a la instancia de clase Perro en orden respectivamente(nombre:string, edad:number)
print(f"Mi perro {mi_perro.nombre} tiene {mi_perro.edad} año de edad.") #se llama e imprime el valor del atributos de la instancia
mi_perro.habla() #se llama al método habla() de la instancia
