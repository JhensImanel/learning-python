class Perro:  #Se tiene una clase llamada Perro, a este se le asigna un método(función).
    def ladra(self): #las funciones siempre usan self como indice y parametro
        print("Wuaf!") #se imprime un mensaje

mi_perro = Perro() #se crea una instancia de la clase Perro
mi_perro.ladra() #se llama al método habla de la instancia creada
print(isinstance(mi_perro, str)) #verifica si el objeto es una instancia de una clase o una tupla de clases
