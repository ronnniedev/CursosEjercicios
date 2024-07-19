frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1] #primer espacio es el comienzo del split, el del medio el final, y el final cada cuantos caracteres
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)
print("........................")
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil","fácil")
resultado = resultado.replace("mala","buena")
print(resultado)

print("........................")
# dic = {'c1':['a','b','c'],'c2':['d','e','f']}
# print(dic['c2'][1].upper())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia" #añadimos datos a diccionarios
print(mi_dic)

print("........................")
mi_tuple = (1,2,(10,20),4)
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla) #convierte la tupla en lista
print(mi_tuple)

print("........................")
mi_set = set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)




