"""
Devuelve un valor distinto dependiendo de la suma de los numeros ingresados
-si la suma es mayor que 15 devuelve el maximo de los numeros
-si la suma es menor de 10 devuelve el minimo de los numeros
-si esta entre 10 y 15 devuelve el numero intermedio
"""
def devolver_distintos(numero1,numero2,numero3):
    lista = [numero1,numero2,numero3]
    print(lista)
    suma = sum(lista)
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        print(lista)
        return lista[1]
"""
Descompone las letras de la palabra y borra las letras repetidas ordenandolas despues en orden alfabetico
"""
def ejercicio_dos(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)

    lista = list(set(lista))
    lista.sort()

    return lista

"""
Nos indica si hay un numero repetido y consecutivo en una secuncia de numeros introducida
"""
def ejercicio_tres(*args):
    anterior = ""
    for n in args:
        if n == anterior:
            return True
        anterior = n
    return False

"""
Nos indica una lista de numeros primos desde el 2 al numero introducido
"""
def ejercicio_cuatro(numero):
    lista = []
    for n in range(2,numero):
        cont = 0
        for num in range(2,n):
            if n%num == 0:
                cont += 1

        if cont < 1:
            lista.append(n)

    return lista



print(devolver_distintos(0,1,17))
print("----------\n" , ejercicio_dos("entretenido"))
print("----------")
print(ejercicio_tres(5,6,1,0,0,9,3,5))
print(ejercicio_tres(6,0,5,1,0,3,0,1))
print(ejercicio_cuatro(150))