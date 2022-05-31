# Envoltura de funciones en python

'''
def suma(val1 = 0, val2 = 0):
    return val1 + val2

print(suma())

# Asignar una función a una variable
funcion_suma = suma

# Enviar como parametro una función.
def operacion(funcion,val1 = 0, val2 = 0):
    return funcion(val1,val2)

resultado = operacion(funcion_suma,45,15)
print(resultado)
'''

def crear_funcion(operador):
    if operador == '+':
        def suma(val1 = 0, val2 = 0):
            return val1 + val2
        return suma
    elif operador == '-':
        def resta(val1 = 0, val2 = 0):
            return val1 - val2
        return resta
    elif operador == '*':
        def multiplicacion(val1 = 0, val2 = 0):
            return val1 * val2
        return multiplicacion
    elif operador == '/':
        def division(val1 = 0, val2 = 0):
            return val1 / val2
        return division()


def operacion(funcion,val1 = 0, val2 = 0):
    return funcion(val1,val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,15,5)
print(resultado)

funcion_resta = crear_funcion('-')
resultado2 = operacion(funcion_resta,5,13)
print(resultado2)

funcion_multi = crear_funcion('*')
resultado3 = operacion(funcion_multi,2,8)
print(resultado3)