# Lista paralelas

'''
nombres1 = ['Juan','Maria','Josue','Marcos','Luz']
edades2 =  [15    ,32     ,25     ,17      ,18]

nombres = list() # nombres = []
edades = list()  # edades  = []

for xpersona in range(5):
    nombre = input('Digite el nombre de la persona: ')
    nombres.append(nombre)
    edad = int(input('Digite la edad de la persona: '))
    edades.append(edad)

print('Nombre de las personas que son mayores o iguales a 18 años')

for xedad in range(5):
    if edades[xedad] >= 18:
        print('Nombre -', nombres[xedad], ' edad : ', edades[xedad])
'''


'''
    print(type(nombres)) # tipo de dato
    print(dir(nombres))  # método del objeto
'''


# listas compuestas.

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

'''
print(lista)
print(lista[0])
print(lista[0][0])
'''

'''
for x in range(len(lista[0])):
    print(lista[0][x])
'''

'''
for x in range(len(lista)):
    for k in range(len(lista[x])):
        print(lista[x][k])
'''

# Ejercicio 2

'''
lista = [[1,3,5,7,9],[2,4,6,8,10]]

for x in range(len(lista)):
    resultado = 0
    for k in range(len(lista[x])):
        resultado = resultado + lista[x][k]
    
    print(resultado)
'''

# Ejercicio 3

'''
lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

resultado = 0
for x in range(len(lista)):
    for k in range(len(lista[x])):
        resultado = resultado + lista[x][k]

print(resultado)
'''

# Ejercicio 4

padres = list()
hijos = list()

for k in range(3):
    pa = input('Ingrese el nombre del padre: ')
    ma = input('Ingrese el nombre de la madre: ')

    padres.append([pa,ma])
    cantidad = int(input('Cantidad de hijos en la familia: '))
    hijos.append([])

    for x in range(cantidad):
        hi = input('Ingrese el nombre del hij@ ')
        hijos[k].append(hi)


print('Listado de padre, madre e hijos \n')

for x in range(len(padres)):
    print('Padre : ', padres[x][0])
    print('Madre : ', padres[x][1])
    for k in range(len(hijos[x])):
        print('Hij@s : ', hijos[x][k])
    
print('\nListado de padres con la cantidad de hij@s \n')

for x in range(len(padres)):
    print('Padre : ', padres[x][0])
    print('Hij@s : ', len(hijos[x]))









