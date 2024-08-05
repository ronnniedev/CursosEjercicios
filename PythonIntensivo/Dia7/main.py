class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print ("Que tal")
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()
