# Conversión entre contenedores

# Conversión de cadenas

# cadena -> lista (str - list)

'''
cadena = 'Grupo_58'
lista = list(cadena)
print(lista)
'''

# cadena -> tupla (str - tuple)

'''
cadena1 = 'hola'
cadena2 = 'adios'
numero = 18
tupla = tuple(cadena1)
tuplaGeneral = (tupla,numero,tuple(cadena2))
print(tupla)
print(tuplaGeneral)
'''

# cadena -> conjunto (str - set)

'''
cadena = 'hhola'
conjunto = set(cadena)
print(conjunto)
'''

# lista -> cadena (list - str)

'''
lista = ['h','o','l','a',(1,2,3)]

try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('No se puede concatenar tipo de datos diferentes ha string.')

convertirCadena = ''
for elemento in lista:
    convertirCadena = convertirCadena + str(elemento)

print(convertirCadena)    
'''

# lista -> tupla (list - tuple)

'''
lista = ['h','o','l','a',123]
tupla = tuple(lista)

print(tupla)
'''

# lista -> conjunto (list - set)

'''
lista = ['h','o','o','l','a',1,1,2,2,3]
conjunto = set(lista)

print(conjunto)
'''

# tupla -> cadena (tuple - str)

'''
tupla = ('h','o','l','a')
cadena = ''.join(tupla)

print(cadena)
'''

# tupla -> lista (tuple - list)

'''
tupla = ('hola',125,'mundo')
lista = list(tupla)

print(lista)
'''

# tupla -> conjunto (tuple - set)

'''
tupla = ('hola',111,'mundo','hola')
conjunto = set(tupla)

print(conjunto)
'''

# conjunto -> cadena (set - str)

'''
conjunto = {'h','o','l','a'}
cadena = ''.join(conjunto)

print(cadena)
'''

# conjunto -> tupla (set - tuple)

'''
conjunto = set(range(20))
tupla = tuple(conjunto)

print(tupla)
'''

# conjunto -> lista (set - list)

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)

print(lista)
'''

# Conversión a diccionario

# cadena -> diccionario (str - dict)

cadena = 'Grupo_58'

diccionarioCadena = dict()
for posicion in range(len(cadena)):
    diccionarioCadena[posicion] = cadena[posicion]

print(diccionarioCadena)

diccionario = dict( zip( range( len(cadena) ), cadena ) )
print(diccionario)