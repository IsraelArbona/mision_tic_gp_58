# Acceder a los caracteres de uno en uno de la cadena de texto (String)

fruta = 'fresa'
letra = fruta[1]
print(letra)

fruta = 'banana'
letra = fruta[0]
print(letra)

numero = 2
print(fruta[1+2+numero])


# Conseguir la longitud de una cadena
fruta = 'banana'
#        012345

longitud = len(fruta)
print(longitud)
print(fruta[longitud-1])

print(fruta[-1])
print(fruta[-6])

# Rebanadas de una cadena
s = 'Monty_Python'

print(s[0:6])
print(s[6:12])

print(s[:3])
print(s[3:])

print(s[5:5])
print(s[:])

# Inmutabilidad de una cadena -- Solo es posible crear una nueva cadena

saludo = 'Hola mundo'
#saludo[0] = 'j'
nuevo_saludo = 'j' + saludo[1:]
print(nuevo_saludo)


# Operador in, devuelve respuesta booleana 
# si una cadena se encuentra dentro de otra cadena

var1 = 'a'
var2 = 'banana'
print(var1 in var2)

var1 = 'ola'
var2 = 'banana'
print(var1 in var2)

# Comparación de cadenas

palabra = 'banana'
if palabra == 'banana':
    print('Esta bien, bananas')

palabra2 = '@pera'

if palabra2 < 'banana':
    print('Tu palabra ' + palabra2 + ', viene antes de banana')
elif palabra2 > 'banana':
    print('Tu palabra ' + palabra2 + ', viene despues de banana')
else:
    print('las palabra son iguales')


# Conseguir el tipo de dato de una variable 
# y los métodos asociados a ese tipo de variable

cadena = "Grupo 58"
print(type(cadena))
#print(dir(cadena))

# Convertir una cadena en mayúsculas

palabra = 'banana'
palabra_nueva = palabra.upper()
print(palabra_nueva)

# Retorna la posición de una subcadena dentro de una cadena

palabra = 'banana'
posicion = palabra.find('a')
print(posicion)
print(palabra.find('na'))
print(palabra.find('na',3))

# Retirar espacios en blanco a los extremos de una cadena

linea = '                    Aquí vamos                 '
print(linea)
print(linea.strip())


# Conseguir una subcadena dentro de otra al 
# inicio retornando Vardadero o Falso

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))

print(linea.startswith('q'))
print(linea.lower().startswith('q'))
print(linea.lower())


# Pieza de código que permite cortar el host del correo electronico 
# y luego imprimirlo

# conseguir la posición del @ 
cadena = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
posicion = cadena.find('@')
print(posicion)

espacio = cadena.find(' ',posicion)
print(espacio)

host = cadena[posicion + 1:espacio]
print(host)

# Operador de Formato

# %s cadena
# %d número

nombre = 'Luis'
numero = 30

print('%s %d' % (nombre, numero))

saludo = 'Hola'
print('%s, Luis' % (saludo))

camellos = 42

print('He visto %d camellos' % camellos)

# Omitir caracteres especiales

cadena = 'Hola\nmundo'
print(cadena)

cadena = r'Hola\nmundo'
print(cadena)


# Método de count en cadena de texto (String)

frase = 'un uno, un dos, un tres'

print(frase.count('un')) # sacar 4 hay "un" en la cadena
print(frase.count('un',10)) # sacar 1 teniendo en cuenta la posición inicial
print(frase.count('un',0,10)) # sacar 3 "un" teniendo en cuenta el rango

# Método replace

print(frase.replace('un', 'XXX'))
print(frase.replace('un', 'XXXX', 2))


var1 = 10
var2 = 20

print('El valor es: {}'.format(12))
print('El valor es: {}'.format(11.2343))

print('Los valores son: {}, {} y {}'.format(1,2,3))
print('Los valores son: {1}, {0} y {2}'.format(1,2,3))

print('Los valores son: {num1} y {num2}'.format(num1 = 2,num2 = 3))
print('Los valores son: {1} y {0}'.format(var1,var2))


# Multiplicacion de una cadena

mensaje = 'Hola' * 3
mensaje2 = 'mundo'
print(mensaje + mensaje2)


# Añadir en una cadena

msg = 'Hola'
msg += ' '
msg += 'mundo'
print(msg)
