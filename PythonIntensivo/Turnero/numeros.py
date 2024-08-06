def decorador(generador):
    """
        Decora el texto dependiendo del generador que hayamos introducido
        @:param generador : function
        @:return string
    """
    return f"Su turno es el {next(generador)}"


def turno_perfumeria():
    """
        Imprime el truno de perfumeria
        @:return string
    """
    for n in range(1, 1000):
        texto = "P-" + str(n)
        yield texto


def turno_farmacia():
    """
        Crea un string con el turno de Farmacia
        @:return string
    """
    for n in range(1, 1000):
        texto = "F-" + str(n)
        yield texto


def turno_cosmetica():
    """
        Crea un string con el turno de cosmetica
        @:return string
    """
    for n in range(1, 1000):
        texto = "C-" + str(n)
        yield texto
