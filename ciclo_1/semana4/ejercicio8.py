# Funcion reduce (importarla)
from functools import reduce

'''
lista = [1,2,3,4,5,6,7,8,9]

acumulador = 0
for elemento in lista:
    acumulador = acumulador + elemento

#print(acumulador)

# resultado = sum(lista)
# print(resultado)

def funcion_acumular(acumulador=0, elemento=0):
    return acumulador + elemento

resultado = reduce(funcion_acumular,lista)
print(type(resultado))
print(resultado) 


resultado = reduce( lambda acumulador=0,elemento=0: acumulador + elemento, lista)
print(resultado)
'''

lista = ['Python','Java','Ruby','Elixir']
resultado = reduce(lambda acumulador='',elemento='': acumulador + ' - ' + elemento, lista)
print(resultado)

nuevaLista = list( map( lambda ele: ele[1:], lista ) )
nuevoResultado = reduce(lambda acu='',ele='': acu + ' - ' + ele, nuevaLista)

print(nuevaLista)
print(nuevoResultado)