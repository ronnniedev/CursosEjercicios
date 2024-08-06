def cambiar_letras(tipo):

    def mayusucula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayusucula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras("may")

operacion("palabra")


