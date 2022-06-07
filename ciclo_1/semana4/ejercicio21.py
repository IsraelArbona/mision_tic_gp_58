# libreria pandas

import pandas as pd

'''
ventas = pd.Series([12,43,25])
print(ventas)
'''

ventas = pd.Series([12,43,25], index=['Ene','Feb','Mar'])

'''
print(ventas)
print(ventas[0])
print(ventas['Ene'])
print(ventas.dtype)
print()
print(ventas.index)
print(ventas.values)
'''

ventas.name = 'Ventas 2022'
ventas.index.name = 'Meses'

print(ventas,'\n')
print(ventas.axes)
print(ventas.shape)