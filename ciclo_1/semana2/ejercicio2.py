# Forma de clasificar los condicionales
'''
#Condión simple
 
if:

if:
else

horaDelDia = 21

if horaDelDia >= 12:
    print("PM")
else:
    print("AM")
'''

'''
# Decisiones secuenciales

if:
if:
if:
if:

resultadoDelExamen = 91

if resultadoDelExamen > 60:
    print("Aprobado")
if resultadoDelExamen > 90:
    print("Excelente trabajo!")

'''

num = input('Por favor, digite un número entero: ')
num = int(num)

if num < 0:
    num = num * ( -1 )
if num == 0:
    print('El número es igual a cero')
else:
    if ( (num > 0) and (num <= 9) ):
        print('El número tiene 1 dígito')    
    else:
        if num >= 10 and num <= 99:
            print('El número tiene 2 dígitos')
        else:
            if (num >= 100) and (num <= 999):
                print('El número tiene 3 dígitos')
            else:
                if num >= 1000 and num <= 9999:
                    print('El número tiene 4 digitos')
                else:
                    print('El número tiene más de 4 dígitos')

print("Final")


if num < 0:
    num *= -1

if num > 0 and num < 10:
    print('El número tiene 1 dígito')
elif num > 9 and num < 100:
    print('El número tiene 2 dígitos')
elif num > 99 and num < 1000:
    print('El número tiene 3 dígitos')
elif num > 999 and num < 10000:
    print('El número tiene 4 dígitos')
elif num == 0:
    print("Número igual a cero")
else:
    print('El número tiene mas de 4 dígitos')


    