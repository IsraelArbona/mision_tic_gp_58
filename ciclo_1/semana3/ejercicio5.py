# Creación de un conjunto

# se crea un conjunto de elementos numericos.

'''
s = {1,2,3,4,5}
print(type(s))
print(s)
'''

# Al igual que otras colecciones, puede contener diferente tipos de datos.

'''
s = {True, 3.14, None, False, 'Hola grupo 58',(4,5)}
print(s)
'''

# Un conjunto no puede incluir objetos mutables como listas

'''
s = {[1,2,3]}
'''

# Python distingue este tipo de operación como creación de un diccionario.
s = {}

# Creación de un conjunto vacio utilizando la clase Set.

'''
s = set()
print(s)
'''

# Podemos obtener un conjunto  a partir de cualquier objeto iterable.

'''
s1 = set([1,2,3,4])
s2 = set(range(20))

print(s1)
print(s2)
'''

# En los conjuntos los elementos repetidos son eliminados,
# si el conjunto es solo numeros entero se ordena.

'''
lista = list({1,2,3,4,5})
conjunto = set([1,2,4,5,1,3,2,7])

print(lista)
print(conjunto)

a = set('Hola grupo 58')
print(a)

print(dir(a))
'''

# Recorrer todo los elementos de un conjunto

'''
conjunto = {1,3,2,9,3,1}
print(conjunto)
for i,numero in enumerate(conjunto):
    print('Posición : ', i)
    print(numero)
'''

# Métodos de objeto conjunto

# add() -> agregar un elemento a un conjunto.

'''
setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.add(22.5555555)
setMutable.add(9)
setMutable.add(9)
print(setMutable)
'''

# clear() -> Eliminar todos los elementos de un conjunto.

'''
setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.clear()
print(setMutable)
'''

# copy() -> devuelve una copia del conjunto.

'''
setMutable = set([4.0,'Carro',True,(3,4),1,2,'Grupo 58'])
setMutableCopy = setMutable.copy()

print(setMutable)
print(setMutableCopy)
print(setMutable == setMutableCopy)
'''

# difference() -> devuelve la diferencia entre dos conjuntos.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print(setMutable1)
print(setMutable2)
print(setMutable1.difference(setMutable2))
print(setMutable2.difference(setMutable1))
'''

# difference_update() -> actuliza un conjunto, con la diferecia de los conjuntos

'''
conj1 = {'python','Zope2','ZODB3','pytz'}
conj2 = {'python','Plone','diazo'}

print(conj1)
print(conj2)
conj1.difference_update(conj2)
print(conj1)
'''

# discard() -> eliminar o remover un elemento de un conjunto.

'''
conj1 = {'python','Zope2','ZODB3','pytz'}
print(conj1)
conj1.discard('Zope2')
print(conj1)
'''

# pop() -> elimina o remueve y devuelve un elemento de un conjunto.

'''
paquetes = {'python','zope','plone','django'}
print(paquetes)
print('Valor aleatorio devuelto es : ', paquetes.pop())
print(paquetes)
print('Valor aleatorio devuelto es : ', paquetes.pop())
print(paquetes)
print('Valor aleatorio devuelto es : ', paquetes.pop())
print(paquetes)
'''

# remove() -> busca y remueve un elemento de un conjunto.

paquetes = {'python','zope','plone','django'}
print(paquetes)
paquetes.remove('django')
print(paquetes)















