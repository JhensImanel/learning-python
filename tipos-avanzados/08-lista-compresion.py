usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombre = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]
# filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)
print(menosUsuarios)
