def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():

    for x in range(1, 5):
        yield x * 10


def mi_generador():
    numero = 0
    while True:
        numero = numero + 1
        yield numero



numero = 1
generador = mi_generador()


while True:
    input("Presiona enter: ")
    print(next(generador))
