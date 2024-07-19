letras = []

texto ="""Me gusta aprender de Python un monton 
ademas es increible 
lo rapido que aprendo."""
print("******Texto******")
print(texto)
"""Preguntamos al usuario las letras que quiere buscar"""
"""Tras crear una lista de letras lo agregamos con la funcion append"""
letras.append(input("Escribe una letra a buscar(Letra 1): ").lower())
letras.append(input("Escribe una letra a buscar(Letra 2): ").lower())
letras.append(input("Escribe una letra a buscar(Letra 3): ").lower())

print("******Numero de veces que aparecen las letras******")
"""Bajamos el texto a minusculas y buscamos la letra concreta, nuestro analizador no distingue entre mayusculas/min"""
print("La letra " + letras[0] + " aparrece ",texto.lower().count(letras[0]), " veces")
print("La letra " + letras[1] + " aparrece ",texto.lower().count(letras[1]), " veces")
print("La letra " + letras[2] + " aparrece ",texto.lower().count(letras[2]), " veces")

print("******PalabrasEnTotal******")
"""Contamos el tamaño de la lista generada"""
lista = texto.split()
print("Hay un total de ", len(lista), " palabras")

print("******Primera y ultima letra******")
"""Si escribos el numero 0 encontramos la letra 0 y si escribimos -1 la ultima, ponemos un if para saber si de verdad
    es la ultima letra"""
print("La primera letra es: " + texto[0].lower())
if texto[-1].isalpha():
    print("La ultima letra es: " + texto[-1].lower())
else:
    print("La ultima letra es: " + texto[-2].lower())

print("******TextoAlReves******")
"""Hacemos un split por cada espacio, le damos la vuelta a la lista y finalmente hacemos un join con suma de espacios"""
lista = texto.split(" ")
print(lista)
palabras_invertidas = lista[::-1]
print(" ".join(palabras_invertidas))

#print(texto[::-1])
"""Hacemos un booleano que nos escriba si esta la pabra Python o no"""
print("******¿Esta Python?******")
if "python" in texto.lower():
    print("si")
else :
    print("no")