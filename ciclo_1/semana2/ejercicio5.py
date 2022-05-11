# Ejercicio 1

# Diccionario vacio

diccionario = {}
print(diccionario)
print(type(diccionario))

# Diccionario vacio usando el constructor dict()
diccionario1 = dict()

print(diccionario1)

# ejercicio 2
# si necesitamos almacenar nuevos valores basta con separarlos mediante una coma.

diccionario1 = {
#   clave       : valor    
    "total"     : 40,
    "descuento" : True,
    "subtotal"  : 12.59434,
    "cliente"   : "Marcos"
}

print(diccionario1)

# ejercicio 3

# Argumentos con nombre
diccionario3 = dict(uno = 1, dos = 2, tres = 3)
print(diccionario3)

# Pares claves: valor encerrados entre llaves
diccionario3 = dict({'uno':1,'dos':2,'tres':3})
print(diccionario3)

# ejercicio 4

diccionario4 = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo":"cheval"
}

numeroTelefono = {
    'jefe' : '+57 23214324',
    'secretaria' : '+57 3211212'
}

print(diccionario4)
print(numeroTelefono)

print(diccionario4['gato'])
print(numeroTelefono['jefe'])

#print(dir(diccionario4))

# Ejemplo 5 

usuario = {
    'nombre': 'Maria',
    'edad': 25,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': False
    },
    'no_medallas': 10
}

print(usuario)

# Podemos agregar, obtener y modificar 
# algún valor del diccionario con el usu de corchetes

usuario['activo'] = True
print(usuario)
print(usuario['activo'])

usuario['nombre'] = 'Carlos'
print(usuario)


# ejercicio 6

''' 
    Podemos obtener todas las llaves de nuestro diccionario 
    utilizando el método keys, ademas podemos obtener todos los valores
    del diccionario con el método values
'''

diccionario6 = {'Eduar': 1, 'Francisco': 2, 'Juan': 3, 'Jose': 4}

print(diccionario6.keys())
print(diccionario6.values())

diccionario7 = {
    "Nombre"   : "Sixto Manuel",
    "Apellido" : "García Romero",
    "Cedula"   : 80223023,
    "Direccion": "Cll 3 # 45-09",
    "Telefono" : 4534354,
    "Titulo"   : "Ingeniero",
    "Ciudad"   : "Cali",
    "Trabajo"  : "Independiente"
}

print()
print("Cantidad de datos: ", len(diccionario7), "\n")
print(diccionario7, "\n")
print(diccionario7.keys(), "\n")
print(diccionario7.values(), "\n")

# ejercicio 8

datos = {
    'id'            : '3223423m234',
    'nombre'        : 'Andres',
    'apellido'      : 'Lopez',
    'email'         : 'andres.lopez@miscorreo.com',
    'telefono'      : 310232343,
    'direccion'     : 'calle 20 sur 34 23',
    'ciudad'        : 'Armenia',
    'departamento'  : 'Risaralda',
    'pais'          : 'Colombia'
}

print(f'Número de datos: {len(datos)} \n')

for clave in datos.keys():
    print(f'{clave} = {datos[clave]}')



datos2 = dict(
    id = '3479234f823',
    nombre = 'Mauricio',
    apellido = 'Posada',
    email = 'm.posada@micorreo.com',
    telefono = 310324322,
    github = '@mposada',
    instagram = '@mposadasites',
    direccion='cra 20 # 10 10',
    ciudad = 'cali',
    departamento = 'valle',
    pais = 'Colombia'
)


print()
print("Cantidad de datos: ", len(datos2))
print(datos2)
print()
print(datos2.keys())
print()
print(datos2.values())
print()

diccionario = {
    'clave1' : 345,
    'clave2' : True,
    'clave3' : 'Juan Carlos'
}

print(diccionario)
print(type(diccionario))
print(diccionario['clave1'])
print(type(diccionario['clave1']))
print(diccionario['clave2'])
print(type(diccionario['clave2']))
print(diccionario['clave3'])
print(type(diccionario['clave3']))



# Encapsulamiento con Diccionario

def promedioNotas2(dicNotas: dict):
    sumatoria  = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']
    promedio = round(sumatoria / 4, 2)
    return promedio

# diccionario vacio
dicNotas = {}

# agregar valores al diccionario
dicNotas['Nota1'] = 4.2
dicNotas['Nota2'] = 3.3
dicNotas['Nota3'] = 2.3
dicNotas['Nota4'] = 4.0
print('El promedio es de: ', promedioNotas2(dicNotas))