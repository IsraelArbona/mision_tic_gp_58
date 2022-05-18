# Manejo de Bucle for.
# range(start, stop,step)
# range(inicio, final, contador)

'''
for x in range(0,4):
    print('Estamos en la iteración : ' + str(x))
'''

'''
for x in range(0, 10, 2):
    print('Estamos en la iteración: ', x)
'''

'''
for j in range(10, 0, -2):
    print('Estamos en la iteración : ', j)
'''


'''
for j in range(10, 0, -2):
    if j == 4:
        break
    print(j)
'''

# ejercicio 2
# Método split()

'''
oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # Convierte la cadena de caracteres a una lista palabras.

print(type(frases))
print(frases)
print(len(frases))
print('La oración analizada es: ', oracion, '\n')

for palabra in range(len(frases)):
    print('Palabra {}, en la frase su posición es {}'.format(frases[palabra], palabra))
'''

# ejercicio 3
# Bucle for con Diccionario.

'''
datosBasicos = {
    'nombres': 'Leonardo Jose',
    'apellidos': 'Caballero Garcia',
    'cedula': '11002343454',
    'fecha_nacimiento': '03/11/1980',
    'lugar_nacimiento': 'Bucaramanga, Santader, Colombia',
    'nacionalidad': 'Colombiano',
    'estado_civil': 'Soltero'
}

clave = datosBasicos.keys()
valor = datosBasicos.values()

print(type(clave))

for cla in clave:
    print(cla, '=>', datosBasicos[cla])
print()
cantidad_datos = datosBasicos.items()

for clave, valor in cantidad_datos:
    print(clave +' = ' + valor) 
print()
for k in datosBasicos.keys():
    print(k, '->', datosBasicos[k])
print()
for k2 in datosBasicos:
    print(k2, ' --> ', datosBasicos[k2])
'''

# ejercicio 4 
# Bucle for con else

'''
db_connection = '127.0.0.1','5432','root','nomina'
print(type(db_connection))
print(db_connection)

for parametro in db_connection:
    print(parametro)

print('El comando de postgreSQL es: $ psql -h {} -p {} -u {} -d {}'.
format(db_connection[0],db_connection[1],db_connection[2],db_connection[3]))
'''





