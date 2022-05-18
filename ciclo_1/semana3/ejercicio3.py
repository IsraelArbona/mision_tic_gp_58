# Listas 

'''
lista = [1, 2.5, 'DevCode', [5,6], 4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5,'DevCode']
print(lista[1:7]) # [2.5, 'DevCode',[5,6], 4]
print(lista[1:6:2]) # [2.5, [5,6]]
'''

# ejercicio 2
# list vacia

'''
lista2 = []
print(lista2)
'''

# ejercicio 3

'''
nombre = 'Luis'
edad = 25
lista3 = [nombre,edad]

print(lista3)
'''

# ejercicio 4

'''
nombres = ['Luis', 'maria']
edades = [24,22]
lista4 = [nombres, edades]

print(lista4)

nombres += ['Cristian']
print(lista4)
'''

# ejercicio 5

'''
factura = ['pan','huevos', 1000,700]
print(factura)
'''

# Modificar un elemento de la lista

'''
factura[1] = 'carne'
print(factura)
'''

# ejercicio 6
# Método append()
# Este método agrega una elemento al final de una lista.

'''
versiones_plone = [2.5, 3.6, 4, 5]
print(versiones_plone)

versiones_plone.append(6)
print(versiones_plone)
'''

# ejercicio 7
# Mètodo count()
# Este método recibe un elemento o valor como argumento 
# y cuenta la cantidad de veces que aparece en la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6,4,3,6,7, 4]
print(versiones_plone)
print('6 -> ', versiones_plone.count(6))
print('4 -> ', versiones_plone.count(4))
print('2.5 -> ', versiones_plone.count(2.5))
'''

# ejercicio 8
# Método extend()
# Este método extiende una lista agregando un iterable al final.

'''
versiones_plone = [2.1, 2.5, 3.6]
print(versiones_plone)
versiones_plone.extend([4])
print(versiones_plone)
versiones_plone.extend(range(3,18))
print(versiones_plone)
versiones_plone.extend([5,2,'Letras',[1,2]])
print(versiones_plone)
'''

# ejercicio 9
# Método index()
# Este método recibe un elemento como argumento y devuelve el índice de su primera aparición en la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4 ,5 ,6 ,4]
print(versiones_plone)
print(versiones_plone.index(4))
'''

# El método admite como argumento adicional un índice inicial 
# a partir de donde empieza la búsqueda, 
# opcionalmente también el índice final.

'''
print(versiones_plone.index(4,2))
print(versiones_plone.index(4,5))
'''

# El método devuelve una excepción ValueError 
# si el elemento no se encuentra en la lista, o en el entorno definido.

'''
print(versiones_plone.index(9))
'''

# ejercicio 10
# Método insert()
# Nos permite insertar el elemento x en la lista, en el índice i.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.insert(2, 4.5)
print(versiones_plone)
'''

# ejercicio 11
# Método pop()
# Este método devuelve el ultimo elemento de la lista y lo borra de la misma.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

print(versiones_plone.pop())
print(versiones_plone)
'''

# Opcionalmente puede recibir un argumento numerico entero, 
# que funciona con índice del elemento (por defecto -1)

'''
print(versiones_plone.pop(2))
print(versiones_plone)
'''

# ejercicio 12
# Método remove()
# Este método recibe como argumento un elemento o valor 
# y borra su primera aparición en la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 3.6]
print(versiones_plone)

versiones_plone.remove(3.6)
print(versiones_plone)
'''

# El método devuelve una excepción ValueError si el elemento no se encuentra en la lista

'''
versiones_plone.remove(7)
'''

# ejercicio 13
# Método reverse()
# Este método invierte el orden de los elementos de una lista.

'''
versiones_plone = [2.1, 2.6, 6, 1.4, 5, 6, 7]
print(versiones_plone)

versiones_plone.reverse()
print(versiones_plone)
'''

# ejercicio 14
# Método sort()
# Este método ordena los elemento de la lista.

versiones_plone = [6, 1.3, 3.5, 2, 4, 5, 1.5, 7]
print(versiones_plone)

versiones_plone.sort()
print(versiones_plone)

# El método sort() admite la opción reverse, por defecto el valor es False.
# de tener el valor True, el ordenamiento se hace en sentido contrario o inverso.

versiones_plone.sort(reverse= True)
print(versiones_plone)

lista_letra = ['a', 'o','A','u','i']

lista_letra.sort()
print(lista_letra)