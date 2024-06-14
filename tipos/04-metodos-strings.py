animal = " chanCHito feliz "
print(animal.upper()) #mayúsculas
print(animal.lower()) #minúsculas
print(animal.strip().capitalize()) #quitar espacio y 1 letra mayúsculas
print(animal.title()) #iniciales en mayúscula
print(animal.strip()) #quitar espacios
print(animal.lstrip()) #quitar espacios del lado izquierdo
print(animal.rstrip()) #quitar espacios del lado derecho
print(animal.find("CH")) #devuelve el índice de la cadena de caracteres
print(animal.find("j")) #si indica -1, no existe
print(animal.replace("nCH", "j"))
print("nCH" in animal) #busca si se encuentra
print("nCH" not in animal) #busca sino se encuentra