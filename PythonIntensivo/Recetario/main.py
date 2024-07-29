from pathlib import Path
from os.path import exists
import os

"""
    Cuenta el numero de recetas que hay en la base de datos
    @:return contador : int
"""


def contar_recetas():

    cont = 0
    for txt in Path(RUTA).glob("**/*.txt"):
        cont += 1

    return cont


"""
    Despliege de la lista de opciones que tenemos para el recetario, nos pedira escribir una de las siguientes opciones
    @:return string
"""


def seleccionar():
    print("Las opciones para el recetario son las siguientes: \n"
          "1- Leer receta \n"
          "1- Crear receta \n"
          "3- Crear categoria \n"
          "4- Eliminar receta \n"
          "5- Eliminar categoria \n"
          "6- Finalizar programa")

    return input("Escribe la opcion: ")


"""
    Recibe un numero en formato de string y selecciona una funcion de las siguientes presentadas
    @:param numero : string
"""


def llamar_opcion(numero):

    match numero:
        case '1':
            leer_receta(seleccionar_categoria())
        case '2':
            crear_receta(seleccionar_categoria())
        case '3':
            crear_categoria(input("Dime el nombre de la nueva categoria: "))
        case '4':
            eliminar_receta(seleccionar_categoria())
        case '5':
            eliminar_categoria(seleccionar_categoria())
        case '6':
            input("Finalizando programa, pulse enter para continuar...")
            return
        case _:
            print("ERROR: valor introducido no valido, vuelva a ingresarlo")
            input("Por favor escriba una letra o caracter y pulse enter para continuar...")
            return

    input("Por favor escriba una letra o caracter y pulse enter para continuar...")
    return


"""
    Lista las categorias que existen actualmente en la ruta principal de archivos
    @:return string
"""


def listar_categorias():

    lista = "-----Categorias actuales-----"
    print("Seleccione una categoria de las siguientes: ")
    for item in os.listdir(RUTA):
       lista = lista + "\n- " + item

    return lista


"""
    Nos permite seleccionar una categoria determinada dentro de la carpeta, mostrandonos las categorias disponibles
    @:return categoria : string
"""


def seleccionar_categoria():

    lista = listar_categorias()
    print(lista)
    categoria = input("Escriba la categoria con mayusuculas incluidas:")
    # ruta donde se aloja la receta
    localizacion = Path(RUTA, categoria)
    while not exists(localizacion):
        os.system('cls')
        print(lista)
        print("Error: Esta categoria no existe, por favor escriba la categoria basandose en esta lista"
              ", recuerde las mayusuculas\n ")
        categoria = input("Escriba la categoria con mayusuculas incluidas:")
        localizacion = Path(RUTA, categoria)
        print(localizacion)

    return categoria


"""
    Selecciona la receta a traves de la categoria proprocionada, ademas lista el numero de recetas que hay
    @:param categoria : string
"""


def seleccionar_receta(categoria):

    lista = listar_recetas(categoria)
    print(lista)
    receta = input("Escriba la receta con mayusculas incluidas:")
    localizacion = Path(RUTA, categoria, receta)

    while not exists(localizacion):
        os.system('cls')
        print(lista)
        print("Error: Esta receta no existe, por favor escriba la categoria basandose en esta lista"
              ", recuerde las mayusuculas\n ")
        receta = input("Escriba la receta con mayusuculas incluidas:")
        localizacion = Path(RUTA, categoria)
        print(localizacion)

    return receta


"""
    Lista las recetas dentro de la categoria proporcionada
    @:param categoria : string
    @:return lista : string
"""


def listar_recetas(categoria):
    lista = "-----Recetas creadas-----"
    for item in Path(RUTA, categoria).glob("*.txt"):
        lista += "\n- " + item.name

    return lista


"""
    Lee una receta seleccionada a traves de la categoria proporcionada
    @:param categoria : string
"""


def leer_receta(categoria):
    localizacion = Path(RUTA, categoria, seleccionar_receta(categoria))

    if exists(localizacion):
        print("--------Receta seleccionada-----\n")
        receta = open(localizacion, 'r')
        receta = receta.read()
        print(receta)
        print("\n\n-----------------------------")
    else:
        print("El archivo especificado no existe")

    return


"""
    Crea una receta en la carpeta seleccionada
    @:param categoria : string
"""


def crear_receta(categoria):

    nombre_receta = input("Dime el nombre de la receta a añadir: ")

    if not nombre_receta.endswith(".txt"):
        nombre_receta = nombre_receta + ".txt"

    if not nombre_receta.count('.') >= 2:
        localizacion = Path(RUTA, categoria, nombre_receta)
        archivo = open(localizacion, 'a')
        texto = input("Escribe aqui la receta: ")
        archivo.write(texto)
        archivo.close()
        archivo = open(localizacion, 'r')
        print("--------Receta creada-----\n")
        contenido = archivo.read()
        print(contenido)
        print("\n\n-----------------------------")
        archivo.close()
        lista = listar_recetas(categoria)
        print(lista)

    return


"""
    Crea una categoria nueva a traves del nombre proporcionado
    @:param categoria : string
"""


def crear_categoria(categoria):
    if exists(Path(RUTA, categoria)):
        print("Esa categoria ya existe")
    else:
        os.mkdir(Path(RUTA, categoria))
        print("---Categoria creada---\n")
        print(listar_categorias())
    return


"""
    Elimina una receta por input tomando como parametro origen la categoria proporcionada
    @:param categoria : string
"""


def eliminar_receta(categoria):
    localizacion = Path(RUTA, categoria, seleccionar_receta(categoria))

    if exists(localizacion):
        os.remove(localizacion)
        print("-----Receta borrada-----")
        print(listar_recetas(categoria))
    else:
        print("El archivo especificado no existe")

    return


"""
    Elmina una categoria introducida como parametro
    @:param categoria : string
"""


def eliminar_categoria(categoria):
    print(listar_categorias())

    if not exists(Path(RUTA, categoria)):
        print("Esa categoria no existe")
    else:
        os.rmdir(Path(RUTA, categoria))
        print("---Categoria borrada---\n")
        print(listar_categorias())

    return


global RUTA
RUTA = Path(Path.home(), "OneDrive", "Desktop", "proyectos", "pruebas", "Recetario", "Recetas")
opcion = 0


while opcion != '6':

    os.system('cls')
    print("Numero de recetas: ", contar_recetas())
    opcion = seleccionar()
    llamar_opcion(opcion)

os.system('cls')
print("Programa finalizado")
