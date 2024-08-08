import re

def verificar_saludo(frase):

    patron = r"^Hola"

    verificacion = re.search(patron , frase)

    if verificacion:
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("Adios imbecil")