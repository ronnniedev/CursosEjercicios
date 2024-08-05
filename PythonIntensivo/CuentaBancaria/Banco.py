class Persona:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class Cliente(Persona):

    def __init__(self, nombre, apellidos, numero_cuenta, balance):
        super().__init__(nombre, apellidos)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"-------------Cliente--------------- \n Nombre: {self.nombre} \n Apellidos: {self.apellidos} \n "
                f"Numero de cuenta: {self.numero_cuenta} \n Saldo: {self.balance}")

    def depositar(self, dinero):

        if dinero <= 0:
            print("Error: Introduzca un deposito mayor a 0 para que este sea ejecutado")
        else:
            self.balance += dinero

    def retirar(self, dinero):

        if dinero > self.balance:
            print("Error: No puede quedarse en numeros rojos")
        else:
            self.balance -= dinero


"""
    Despliege de la lista de opciones que tenemos para el banco, nos pedira escribir una de las siguientes opciones
    @:return string
"""


def mostrar_menu_inicial():

    print("Bienvenido al sistema bancario, por favor identifiquese: \n"
          "1- Mostrar Clientes \n"
          "2- Crear Cliente \n"
          "3- Logearse como cliente \n"
          "0- Salir \n")

    return input("Escribe la opcion: ")


"""
    Dependiendo de la opcion proporcionada ejecuta una opcion concreta
    @:param opcion
"""


def ejecutar_funcionalidad(opcion):

    match opcion:
        case '1':
            mostrar_clientes()
        case '2':
            crear_cliente()
        case '3':
            login_cliente()
        case'0':
            pass
        case _:
            print("ERROR: valor introducido no valido, vuelva a ingresarlo")
            input("Por favor escriba una letra o caracter y pulse enter para continuar...")
            return

    return


"""
    Imprime la lista de clientes
"""


def mostrar_clientes():
    for cliente in lista_clientes:
        print(str(cliente))


"""
    Crea un cliente pidiendo los datos pertinenetes y los ingresa en la lista de clientes
"""

def crear_cliente():
    nombre = input("Escribeme el nombre del cliente: ")
    apellidos = input("Los apellidos del cliente: ")
    numero_cliente = input("El numero de cuenta del cliente: ")
    saldo_inicial = int(input("El saldo inicial del cliente: "))

    carrito = Cliente(nombre,apellidos,numero_cliente,saldo_inicial)
    lista_clientes.append(carrito)
    print("Cliente añadido con exito")
    mostrar_clientes()


"""
    Escoge el cliente que queremos a traves de un numero de cuenta solicitado
    @:return cliente : Cliente
"""


def login_cliente():
    print("Estos son los clientes alojados en el sistema actualmente: ")
    mostrar_clientes()
    numero = input("Escribeme el numero de cuenta del cliente con el que te quieres logear")

    encontrado = False
    mi_cliente = None

    for cliente in lista_clientes:
        if cliente.numero_cuenta == numero:
            encontrado = True
            mi_cliente = cliente
            break

    if encontrado:
        menu_cliente(mi_cliente)
    else:
        print("Cliente no encontrado")


"""
    Ejecuta una funcion depediendo de la opcion recibida, carga la clase Cliente tambien a partir de su objeto
    @:param opcion : string
    @:param cliente : Cliente
"""

def ejecutar_funcionalidades_cliente(opcion,cliente):
    match opcion:
        case '1':
            print(str(cliente))
        case '2':
            deposito = int(input("Intropduzca el dinero a ingresar: "))
            cliente.depositar(deposito)
        case '3':
            retiro = int(input("Introduzca el dinero a retirar: "))
            cliente.retirar(retiro)
        case '0':
            pass
        case _:
            print("ERROR: valor introducido no valido, vuelva a ingresarlo")
            input("Por favor escriba una letra o caracter y pulse enter para continuar...")
            return

    input("Por favor escriba una letra o caracter y pulse enter para continuar...")
    return

"""
    Despliege de la lista de opciones que tenemos para el banco en la seccion del cliente, nos pedira escribir una de las siguientes opciones
    @:return string
"""

def mostrar_menu_cliente():

    print("Bienvenido al sistema bancario, por favor identifiquese: \n"
          "1- Mostrar datos \n"
          "2- Depositar dinero \n"
          "3- Retirar dinero \n"
          "0- Salir de la sesion \n")

    return input("Escribe la opcion: ")

"""
    Establece un loop para cargar las funcionaliddes relacionadas a un cliente
    @:param cliente : Cliente
    @:return string
"""

def menu_cliente(cliente):
    print(f"Bienvenido al menu del cliente {cliente.nombre}")
    print(str(cliente))
    opcion = -1

    while opcion != "0":

        opcion = mostrar_menu_cliente()
        ejecutar_funcionalidades_cliente(opcion,cliente)

    input("Cerrando sesion, ingrese cualquier letra para continuar...")


lista_clientes = []
opcion = -1

while opcion != "0":
    opcion = mostrar_menu_inicial()
    if opcion == 0:
        pass
    else:
        ejecutar_funcionalidad(opcion)


