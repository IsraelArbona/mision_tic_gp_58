import json

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.json'

with open(ruta) as file:
    datos = json.load(file)

    for client in datos['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')