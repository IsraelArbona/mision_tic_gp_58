# realice una función para determinar si un número es positivo y tiene dos digitos 
# o si es negativo y tiene tres digitos
# validar que cero sea invalido.

def testNumero():
    entero = int(input('Digite el número: '))

    if entero == 0:
        return 'Número Invalido!'
    elif entero > 0:
        if len(str(entero)) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo y no tiene dos dígitos'
    else:
        if len(str(entero)) -1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y no tiene tres dígitos'

#print(testNumero())

def testNumero2():
    numCadena = input('Digite un número: ')

    if numCadena == '0':
        return 'Número Invalido!'
    elif numCadena.startswith('-'):
        if len(numCadena) -1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y no tiene tres dígitos'
    else:
        if len(numCadena) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo y no tiene dos dígitos'

#print(testNumero2())

def testNumero3():
    numCadena = input('Digite un número: ')

    if numCadena == '0':
        return 'Número Invalido!'
    elif numCadena.find('-') == 0:
        if len(numCadena) -1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y no tiene tres dígitos'
    else:
        if len(numCadena) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo y no tiene dos dígitos'

#print(testNumero3())

def testNumero4():
    numCadena = input('Digite un número: ')

    if numCadena == '0':
        return 'Número Invalido!'
    elif numCadena.count('-') == 1:
        if len(numCadena) -1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo y no tiene tres dígitos'
    else:
        if len(numCadena) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo y no tiene dos dígitos'

print(testNumero4())