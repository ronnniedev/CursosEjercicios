from random import randint

intentos = 8
acertado = False
numero = randint(0,100)
nombre = input("Escribeme tu nombre: ")
print(numero)

while intentos > 0 and not acertado:
    print("Intento",8-intentos+1)
    num_introducido = int(input(f"{nombre} Escribeme un numero del 1 al 100: "))
    while num_introducido < 0 or num_introducido > 100:
        num_introducido = int(input(f"Error: Numero introducido fuera de rango, porfavor {nombre} Escribeme un numero del 1 al 100: "))

    if num_introducido == numero:
        acertado = True
        print("Has ganado enhorabuena! te ha tomado", 8 - intentos +1, "intentos")
        break
    elif num_introducido < numero:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")

    intentos -= 1

if not acertado:
    print(f"Has perdido, vuelve a intentarlo la proxima vez el numero secreto era {numero}")