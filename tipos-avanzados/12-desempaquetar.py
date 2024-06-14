# lista = [1, 2, 3, 4]
# print(1, 2, 3, 4)
# print(*lista)

# # def n(n1, n2, n3):
# lista2 = [5, 6]

# combinada = ["Feliz",*lista, "mundo", *lista2, "chanchito"]
# print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)