# exportar diccionarios ha archivo json

import json

datos = dict()

datos['clients'] = []

datos['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

datos['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

datos['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.json'

with open(ruta,'w') as file:
    json.dump(datos,file, indent=4)
    
