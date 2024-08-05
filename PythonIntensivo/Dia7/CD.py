class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Almbum: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD('Pink Floyd', 'The Wall',24)

print(str(mi_cd))
print(len(mi_cd))
del mi_cd

