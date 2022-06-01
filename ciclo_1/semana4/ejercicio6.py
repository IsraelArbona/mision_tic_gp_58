# Convertir de grados celsius a fahrenheit

'''
c = [34.5,32.7,38,39.5,28.9]
f = list( map( lambda x: (float(9)/5)* x + 32, c ) )
print('Grados celsius: ', c)
print('Conversión a grados fahrenheit: ',f)
'''

# Convertir de grados fahrenheit a celsius

'''
f = [94.1, 90.86000000000001, 100.4, 103.10000000000001, 84.02]
c = list( map( lambda x: (float(5)/9)*(x-32),f ) )

print('Grados fahrenheit: ', f)
print('Conversión a grados celsius: ', c)
'''

lista1 = [1,2,3,4,3,4,5]
lista2 = [2,4,3,5]
lista3 = [-1,-4,-5,3,2,3,4]

resultado = list(  map( lambda a,b,c: a+b+c, lista1,lista2,lista3 ) )
print('El resultado de la sumas de las tres listas es: ', resultado)

resultado2 = list( map( lambda a,b: a+b,lista1,lista2 ) ) 
print(resultado2)

resultado3 = list( map( lambda a,b,c: ((3.5*a) + (2.7*b) + c), lista1,lista2,lista3 ) )
print(resultado3)

