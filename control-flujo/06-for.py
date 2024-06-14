n=8
for numero in range(5): #bucle for repite el código para cada valor de la variable
    print(numero)
    if numero == n:
        print("encontrado", n)
        break
else:
    print("no encontre el numero buscado")

for x in "Ultimate Python": #string y range son iterables
    print(x)