from collections import Counter,namedtuple,defaultdict

numeros = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4]
Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
ariel = Persona("Ariel", 1.76, 79)

print(Counter(numeros))
print(ariel.peso)
