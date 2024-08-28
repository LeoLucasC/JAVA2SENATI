import pandas as pd


datos = [
    ["juan", 15, 8.5, "madrid"],
    ["ana", 14, 9.0, "Barcelona"],
    ["Luis", 16, 7.5, "Valencia"],
    ["marta", 15, 8.0, "Sevilla"]
]


columnas = ['Nombre', 'Edad', 'Nota', 'Ciudad']


df = pd.DataFrame(datos, columns=columnas)


print(df)
