import random
global palabra
palabras = ["papa", "sake", "novio", "diego"]
palabra = random.choice(palabras)
letras_acertadas = []
letras_incorrectas = []
ganador = False
vidas = 6

"""
    Esta funcion pide una letra al usuario
    @:return char
"""


def pedir_letra():

    letra = input("Por favor ingresa una letra: ")

    while not validar_letra(letra):
        print("Error: Letra no admitida, ingrese otra")
        letra = input("Por favor ingresa una letra: ")
    return letra


"""
    Valida si la letra  introducida esta entre los valores validos
    @:param letra
"""


def validar_letra(letra):
    letrasaceptadas = "abcdefghijklmnopqrstuvwxyz"
    comprobante = []
    for character in letrasaceptadas:
        comprobante.append(character)

    if letra in comprobante:
        return True
    else:
        return False


"""
    Chequea si la letra introducida esta dentro de la palabra para ganar
"""

def chequear_letra(letra):
    letras_palabra = []
    for character in palabra:
        letras_palabra.append(character)

    letras_palabra = list(set(letras_palabra))

    if letra in letras_palabra:
        return True
    else:
        return False


"""
    Comprueba si el jugador ha ganado la partida
    @:param list : letras_acertadas
    @:return boolean
"""
def ver_si_gano(letras_acertadas):
    letras_palabra = []
    para_imprimir = ""
    for character in palabra:
        letras_palabra.append(character)

    letras_palabra = list(set(letras_palabra))

    if len(letras_acertadas) == len(letras_palabra):
        print("Enhorabuena has ganado!")
        print(f"La palabra era {palabra}")
        return True

    return False


"""
    Imprime las letras acertadas sin contar las ausentes
"""

def imprimir(letras_acertadas):
    para_imprimir = ""

    for character in palabra:
        if character in letras_acertadas:
            para_imprimir += character
        else:
            para_imprimir += "_"
    return para_imprimir


"""
    Juego del ahorcado, tienes 6 vidas si llegas a 0 pierdes 
"""

while vidas != 0 and not ganador:
    print(f"Te quedan {vidas} vidas")
    letra = pedir_letra()

    if chequear_letra(letra) and letra not in letras_acertadas:
        letras_acertadas.append(letra)
        ganador = ver_si_gano(letras_acertadas)
    elif chequear_letra(letra) and letra in letras_acertadas:
        print("Ya has introducido esa letra correcta, intentalo de nuevo")
    else:
        letras_incorrectas+=letra
        vidas -= 1

    print(imprimir(letras_acertadas))
    print("\nEstas son las letras incorrectas: ", "-".join(letras_incorrectas))

if not ganador:
    print("Lo sentimos, vuelve a intentarlo mas tarde")