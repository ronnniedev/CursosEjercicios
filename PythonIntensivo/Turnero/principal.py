from numeros import *

"""
    Sistema que establece los turnos dentro de una farmacia 
    y le pregunta al cliente si necesita imprimir mas
"""


def menu_farmacia():
    """
    Le pregunta al usuario a que seccion de la farmacia quiere acudir
    @:return string
    """
    print("Seleccione una seccion para imprimir su turno: \n"
          "P- Perfumeria\n"
          "F- Farmacia\n"
          "C- Cosmetica\n")
    return input("Escriba aqui: ")


def imprimir_turno(comando):
    """
        Ejecuta la funcion dependiendo de el comando introducido
        @:return string
    """
    match comando.lower():
        case "p":
            return decorador(cont_perfumeria)
        case "f":
            return decorador(cont_farmacia)
        case "c":
            return decorador(cont_cosmetica)
        case _:
            return "ERROR: Asegurese de introducir uno de los comandos sugeridos"


COMANDO = ""
cont_farmacia = turno_farmacia()
cont_cosmetica = turno_cosmetica()
cont_perfumeria = turno_perfumeria()


while COMANDO != "n":
    COMANDO = menu_farmacia()
    print(imprimir_turno(COMANDO))
    acierto = False

    while not acierto:
        try:
            COMANDO = input("Quieres sacar otro turno? [S] [N]: ")
            COMANDO = COMANDO.lower()
            ["s","n"].index(COMANDO)
        except ValueError:
            print("Error opcion no valida")
        else:
            acierto = True


print("Gracias por su visita")

