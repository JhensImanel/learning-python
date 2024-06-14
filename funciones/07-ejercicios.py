def no_space (texto):
    nuevo_texto = ""
    for char in texto: #iterando la variable
        if char != " ": #si es diferente de espacio
            nuevo_texto += char #concatenando la variable
    return nuevo_texto

def reverse (texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves #volteando la variable concatenada
    return texto_al_reves

def es_palindromo(texto): #función que contiene una variable palindromo
    texto = no_space(texto) #creando una nueva función 'no_space'
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

print (es_palindromo("Amo la Paloma"))
print (es_palindromo("Hola Mundo"))
print (es_palindromo("Reconocer"))
print (es_palindromo("Somos o no Somos"))