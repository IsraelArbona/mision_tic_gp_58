# Ciclos while

'''
n = 5
while n > 0: # -> contiene una condición para determinar la iteración que va tener el bucle
    print(n)
    n = n - 1
print('Despegue!')
'''


# break -> nos permite terminar o finalizar las iteraciones de un bucle o ciclo.

'''
while True:
    numero = int(input('Ingrese un número: '))
    if numero % 2 == 0:
        print('El número es par')
        break
    else:
        print('El número es impar')
        break
'''

'''
n = int(input('Por favor, ingrese un número mayor que cero: '))
while n>0:
    print(n)
    print('Correcto!')
    break
'''

'''
n = int(input('Por favor, Digite un número mayor a cero. '))
while n > 0:
    print(n)
    n = n-1
print('Finalizar')
'''

# ejercicio 2
# Alejarse de la terminación

'''
i = 1
while i > 0:
    print(i)
    i += 1
print('finalizar')
'''

# ejercicio 3
# Brincarse la meta

'''
i = -1
while i != 10:
    print(i)
    i = i + 2
print('Finalizar')
'''


# ejercicio 4
# problemas de indetación

'''
n = 1
while n < 10:
    print(n)
i = i + 1
print('Finalizar')
'''

# ejercicio 5
# Olvidar el avance

'''
n = 1
while n < 10:
    print(n)
print('Finalizar')
'''

# ejercicio 6
# Mostrar los primero 40 número de 100

'''
n = 0
while n < 100:
    print(n)
    n = n + 1
    if n == 41:
        break
print('Listo')
'''

'''
n = 0
while n < 100:
    print(n)
    if n == 40:
        break
    n = n + 1
print('Listo')
'''

# ejercicio 7
# continue -> nos permite finalizar el recorrido mas no terminar el ciclo.

'''
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)
'''

# Mostrar los primero 5 número impares, saltando el cuarto valor. partiendo desde 1
'''
    1
    3
    5

    9
    11
'''

'''
n = 0
while n < 50:
    print(n)
    n = n+2
    if n == 13:
        break
print('listo') 
'''

'''
i = 0
while i < 11:
    i += 1
    if i % 2 == 0:
        continue
    if i == 7:
        continue
    print(i)
'''

'''
n = -1
while n != 11:
    n += 2
    if n == 7:
        continue
    print(n)
'''

'''
i = 0
impar = -1
while i <= 5:
    impar += 2
    i += 1
    if i == 4:
        continue
    print(impar)
'''

'''
var = -1
while var < 11:
    var += 2
    if var == 7:
        continue
    print('Valor de variable: ', var)
'''

'''
i = 0
y = 0
while i < 15:
    if i % 2 == 0:
        continue
    else:
        y = y + 1
        print(i)
        i = i + 1
        if y == 4:
            break
'''

# Bucle while controlado por Evento.

'''
acuNotas, proNotas, conNotas = 0, 0.0, 0

print('Introduzca la nota de un estudiante ( -1 para salir): ')
calif = int(input())

while calif != -1:
    acuNotas = acuNotas + calif
    conNotas = conNotas + 1
    print('Introduzca la nota de un estudiante ( -1 para salir): ')
    calif = int(input())

proNotas = round(acuNotas/conNotas,1)
print('El promedio de notas de los estudiantes es: ', proNotas)
'''

'''
acuNotas, proNotas, conNotas = 0, 0.0, 0
mensaje = 'Introduzca la nota de un estudiante ( -1 para salir): '
calif = int(input(mensaje))

while calif != -1:
    acuNotas = acuNotas + calif
    conNotas = conNotas + 1
    calif = int(input(mensaje))
else:
    if acuNotas != 0:
        proNotas = round(acuNotas/conNotas,1)
        print('El promedio de notas de los estudiantes es: ', proNotas)
    else:
        print('No existen notas de los estudiantes')
'''

a , b = 0, 1

while b < 100:
    print(b)
    a, b = b , a + b

