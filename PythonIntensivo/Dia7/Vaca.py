class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice mooooooooooo")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca("Ronnie")
oveja1 = Oveja('Nube')

animales = [vaca1,oveja1]

def animal_habla(animal):
    animal.hablar()


animal_habla(oveja1)

