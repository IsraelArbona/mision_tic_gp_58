# libreria pandas - dataframes

import pandas as pd

'''
datos = { 
    'manzanas': [3,2,0,1],
    'naranjas': [0,3,7,2]
}

compras = pd.DataFrame(datos)
print(compras)
'''

datos = { 
    'manzanas': [3,2,0,1],
    'naranjas': [0,3,7,2]
}

compras = pd.DataFrame(datos,index=['Juni','Roberto','Lily','David'])

'''
print(compras.index)
print(compras.values)
print(compras.columns)
'''

compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'

print(compras,'\n')
print(compras.axes)