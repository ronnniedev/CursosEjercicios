import shutil
from pathlib import Path
import re
import os
import datetime
import time
import math

def buscador_codigos(texto):
    patron = r"^N\D{3}-\d{5}$"
    texto = texto.split(" ")
    for palabra in texto:
        verificacion = re.search(patron, palabra)
        if verificacion:
            return True

    return False
def extractor_texto(carpeta,file):
    localizacion = Path(carpeta,file)
    archivo = open(localizacion, 'r')
    texto = archivo.readline()
    archivo.close()
    return texto

def file_walker():
    ruta = Path(os.getcwd(),"Mi_Gran_Directorio")
    cont = 0
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for file in archivo:
            texto = extractor_texto(carpeta, file)
            if buscador_codigos(texto):
                imprimir_en_pantalla(file,texto)
                cont += 1
    print("\nArchivos Encontrados: ", cont, "\n")

def imprimir_en_pantalla(file,texto):
    patron = r"^N\D{3}-\d{5}$"
    codigo = "0"
    verificacion = re.search(patron, texto)
    texto = texto.split(" ")
    for palabra in texto:
        verificacion = re.search(patron, palabra)
        if verificacion:
            codigo = palabra
            break
    print(f"{file}\t\t{codigo}")


day = str(datetime.date.today())
day = day.split("-")
fecha = day[2] + "-" + day[1] + "-" + day[0]
print(f"Fecha de búsqueda: {fecha}")
print("---------------------------------")
print("Archivo\t\t\t\tCodigo")
print("---------\t\t\t---------")
inicio = time.time()
file_walker()
final = time.time()
duracion = final-inicio
print("Duracion de la busqueda:", math.ceil(duracion), "segundos")

print("---------------------------------")
