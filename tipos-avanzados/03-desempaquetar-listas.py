numero = [1, 2, 3]

# primero = numero[0]
# segundo = numero[1]
# tercero = numero[2]

# primero, segundo, tercero = numero
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penultimo, ultimo = numero
print(primero, segundo, penultimo, ultimo, otros)