def suma():
    n1 = int(input("numero 1:"))
    n2 = int(input("numero 2:"))
    print(n1+n2)
    print("Gracias por sumar")


try:
    suma()
except TypeError:
    print("Algo no ha salido bien")
except ValueError:
    print("Eso no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")
