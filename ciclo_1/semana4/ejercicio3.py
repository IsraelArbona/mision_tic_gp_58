# Funciones anónimas (lambda)

#def sumar1(val1=0,val2=0):
#    return val1 + val2

'''
sumar = lambda val1 = 0, val2 = 0 : val1 + val2
print(sumar(10))

operacion = lambda operacion, val1 = 0, val2 = 0 : operacion(val1,val2) 
resultado = operacion(sumar,10)
print(resultado)
'''

# crear función anónima sin parametros

#def mifunc():
#    return True

'''
sin_parametros = lambda : True
print(sin_parametros() == True)
'''

# crear función anónima varios argumentos.

'''
con_valores = lambda val, val1 = 0, val2 = 0 : val+val1 -val2
resultado = con_valores(3,5,7)
print(resultado)
'''

# *args -> significa cero o mas argumentos que se almacenan en una tupla

'''
con_asterico = lambda *args : args[0]

lista = [1,2,3,4,5,6,7,8,9]

resultado = con_asterico(*lista)
print(resultado)

resultado2 = con_asterico(2)
print(resultado)

resultado3 = con_asterico(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print(resultado3)
'''

# **kwargs -> crean diccionarios

'''
diccionario = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

con_doble_asterisco = lambda **kwargs : sum(kwargs.values())
resultado = con_doble_asterisco(**diccionario)
print(resultado)
'''

lista = [1,2,3]
dicc = {
    'a': 1,
    'b': 2,
    'c': 3
}

con_asteriscos = lambda *a , **b : sum(a) + sum(b.values())
resultado = con_asteriscos(*lista, **dicc)
print(resultado)