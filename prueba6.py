
datos = [
    ["leolucas", 26, "casado"],
    ["cristian", 25, "soltero"]
]


columnas = ['nombre', 'edad', 'estado civil']

# Imprimir las etiquetas de las columnas
print(f"{columnas[0]:<10} {columnas[1]:<5} {columnas[2]:<12}")

# Imprimir los datos
for fila in datos:
    print(f"{fila[0]:<10} {fila[1]:<5} {fila[2]:<12}")
