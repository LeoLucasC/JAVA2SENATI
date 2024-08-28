import pandas as xd
import numpy as cv
df_numeros_random=cv.random.randint(1,11,size=5)
df_numeros = xd.DataFrame(df_numeros_random,columns=['Numeros'])
df_numeros['Dobles'] = df_numeros['Numeros']*2
print(df_numeros)