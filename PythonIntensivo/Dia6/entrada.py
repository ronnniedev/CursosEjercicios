from pathlib import Path,PureWindowsPath

registro_ultima_sesion = ["\tFederico", "\t20/12/2021", "\t08:17:32 hs", "\tSin errores de carga"]
registro = open('registro.txt','w')

registro.writelines(registro_ultima_sesion)

registro.close()

registro = open('registro.txt','r')

print(registro.read())

registro.close()


print("-----------------------")
base = Path.home()
guia = Path(base, "Comida","fabada","marisa")
ejemplo = guia.parents[2]

print(ejemplo)


ruta = Path(Path.home(),"Curso Python","Día 6","practicas_path.py")

print(ruta)

# en_europa = (guia.relative_to(Path("fabada")))

#for txt in Path(guia).glob("**/*.txt"):
   # print(txt)