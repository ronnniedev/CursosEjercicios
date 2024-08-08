import re
texto = "llama al 564-525-6588 ya mismo"

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

busqueda = re.search(patron, texto)

print(busqueda.group(2))