# libreria pandas

import pandas as pd

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.csv'

datosDataframe = pd.read_csv(ruta, sep=';')
print(datosDataframe)
print()

datosDataframe = pd.read_csv(ruta, sep=';', header=None)
print(datosDataframe)
print()

datosDataframe = pd.read_csv(ruta, sep=';', skiprows=1,
                            names=['Id','Pr Nombre','Sg Nombre','Edad',' Salario 1','Salario 2'])
print(datosDataframe)
print()

datosDataframe = pd.read_csv(ruta, sep=';', skiprows=1,
                            names=['Id','Pr Nombre','Sg Nombre','Edad',' Salario 1','Salario 2'],
                            na_values='?')
print(datosDataframe)
print()

datosDataframe = pd.read_csv(ruta, sep=';', skiprows=1,
                            names=['Id','Pr Nombre','Sg Nombre','Edad',' Salario 1','Salario 2'],
                            na_values='?',
                            index_col='Id')
print(datosDataframe)
print()

datosDataframe = pd.read_csv(ruta, sep=';', skiprows=1,
                            names=['Id','Pr Nombre','Sg Nombre','Edad',' Salario 1','Salario 2'],
                            na_values='?',
                            index_col=['Pr Nombre','Sg Nombre'])
print(datosDataframe)
print()
print(datosDataframe['Edad'][4])
print(type(datosDataframe['Edad'][4]))

