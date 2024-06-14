numeros = [2, 55 ,694 , 4952, 12, 83]
numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# def ordena(elemento):
#     return elemento[1]

usuarios.sort(key=lambda el:el[1])
print(usuarios)