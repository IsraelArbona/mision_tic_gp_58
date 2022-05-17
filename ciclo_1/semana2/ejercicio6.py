'''
    Método clear()
    Este método remueve o elimina todo los elemento (items) del diccionario.
'''

diccionario = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print('\n', diccionario)
diccionario.clear()
print('\n', diccionario)



'''
    Métodos copy()
    Este método devuelve una copia del diccionario.
'''

diccionario2 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print('diccionario2: ',diccionario2)
nuevoDiccionario2 = diccionario2.copy()
print('nuevodiccionario2: ', nuevoDiccionario2)


'''
    fromkeys
    Este método crear un nuevo diccionario con claves a partir de un tipo de dato secuencial.
    El valor por defecto es el tipo None.
'''

lista_tupla = ('python','zope','plone')
versiones = dict.fromkeys(lista_tupla)

print('\nNuevo diccionario: %s' % str(versiones))

diccionario3 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

nuevoDiccionario3 = dict.fromkeys(diccionario3)
print('\nnuevoDiccionario3: %s' % nuevoDiccionario3)

nuevoDiccionario3 = dict.fromkeys(diccionario3,'0')
print('\nnuevoDiccionario3 : %s' % nuevoDiccionario3)

'''
    Método get()
    Devuelve el valor de una clave solicitada, sino la encuentra devuelve None.
'''

diccionario4 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print(diccionario4.get('Cedula'))
print(diccionario4.get('correo'))
#print(diccionario4['correo'])

'''
    Método items()
    Devuelve una lista de pares de diccionario (clave-valor), como una tupla.

    [                                           -> lista
        ('Cedula', 1100232342),                 -> tupla
        ('Nombre', 'Maria'),                    -> tupla
        ('Apellido', 'Florez'),                 -> tupla
        ('Correo', 'mflorez@gmail.com')         -> tupla
    ]
'''

diccionario5 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print(diccionario5.items())


'''
    Método pop()
    Remover específicamente una clave del diccionario y devuelve valor correspondiente.
    Lanza una excepción KeyError si la clave no existe.
'''

diccionario6 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print('diccionario original: ', diccionario6)

valorEliminado = diccionario6.pop('Apellido')
print('Valor eliminado: ', valorEliminado)

print('Nuevo diccionario: ', diccionario6)


'''
    Método update()
    Actulizar un diccionario agregando nuevos pares (clave-valor).
    Si se llama el update sin pasar parametros, el diccionaro permanece sin cambios.
'''

diccionario6 = {
    'Cedula': 1100232342,
    'Nombre': 'Maria',
    'Apellido':'Florez',
    'Correo': 'mflorez@gmail.com',
}

print(diccionario6)
diccionario6.update({'activo':True, 'telefono': 3240434554})

print('\n',diccionario6)

