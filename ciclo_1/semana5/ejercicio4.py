# libreria pandas - leer archivos excel
import pandas as pd

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.xlsx'

datosDataframe = pd.read_excel(ruta,sheet_name='personas')
print(datosDataframe)
print()

datosDataframe = pd.read_excel(ruta,sheet_name='personas', header=None, skiprows=1)
print(datosDataframe)
print()

datosDataframe = pd.read_excel(ruta,sheet_name='personas', header=None, skiprows=1,
                                names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'])
print(datosDataframe)
print()


