# condicionales

'''
var1 = 5
var2 = 5

print(var1 > var2)
print(var1 < var2)
print(var1 >= var2)
print(var1 <= var2)
print(var1 != var2)
print(var1 == var2)
print(type(True))
print(type(False))


n = 4
print((n % 2 == 0) != (n % 3 == 0))
'''

'''
x = 10

if x > 0:
    print('x es un número positivo')
'''

# determinar si un numero es par o impar

'''
x = 39

if x % 2 == 0:
    print('x es un número par')
else:
    print('x es un número impar')
'''


'''
x = 10
y = 20

if x < y:
    print("'x' es menor que 'y'")
elif x > y:
    print("'x' es mayor que 'y'")
else:
    print('"x" y "y" son iguales')
'''

'''
letra = 'a'

if letra == 'a':
    print('Mal resultado')
elif letra == 'b':
    print('Buen resultado')
elif letra == 'c':
    print('Cerca, pero no es correcto')
'''

'''
x = 9 
y = 32

if x == y:
    print("x e y son iguales")
else:
    if x < y:
        print("x es menor a y")
    else:
        print("x es mayor a y")
'''

'''
# determinar si un número es positivo y tiene un solo digito

x = 3

if 0 < x:
    if x < 10:
        print('x es un número positivo de un solo digito')


if x >= 0 and x < 10:
    print('x es un número positivo de un solo dígito')
'''


temperatura_fahr = input('Ingrese la tempuratura en grados Fahrenheit ')

try:
    fahr = float(temperatura_fahr)
    cel = ( ( (fahr - 32.0) * 5.0) / 9.0 )
    print(cel)
except:
    print("No ingreso ningún número, gracias")