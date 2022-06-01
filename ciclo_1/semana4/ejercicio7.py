# Función filter

'''
def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,45,55,2,1,30,7,6,8,9,3,1,3,2)
print('Número de elemento de la tupla original: ', len(tupla))
print(tupla)

resultado = tuple( filter(mayor_a_cinco, tupla) )
print('Número de elemento de la tupla filtrada: ', len(resultado))
print(resultado)

resultado = tuple( filter( lambda elemento: elemento >= 5,tupla) )
print('Número de elemento de la tupla filtrada: ', len(resultado))
print(resultado)
'''

pares = list() # []

for i in range(100):
    if i % 2 == 0:
        pares.append(i)

#print(pares)

tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
resultado = list( filter(lambda elemento: elemento % 2 == 0, tupla) )
print('Números pares : ',resultado)

resultado = list( filter(lambda elemento: elemento % 2 == 1, tupla) )
print('Número impares: ', resultado)
