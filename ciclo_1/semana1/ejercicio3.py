'''
# Creación de funciones
def imprime_Cosas():
    print("La clase esta genial")
    print("python es lo máximo")

def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()

# Llamar la función
repetir_funciones()
# Llamar la función
imprime_Cosas()

# Llamar la función
repetir_funciones()

# Llamar la función
imprime_Cosas()
# Llamar la función
imprime_Cosas()
'''


'''
def operacionSuma():
    a = 17
    b = 3
    suma = a + b
    return "La suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma)

resultado = operacionSuma()
#print(resultado)
#print(operacionSuma())

def operacionSumaP():
    a = 13
    b = 27
    suma = a + b
    print("la suma de",a,"+",b,"es igual a:", suma)

operacionSumaP()
'''

'''
def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1 : "))
    num2 = float(input("Ingrese el numero 2 : "))
    print("La suma de", int(num1),"+",int(num2), "es", int(num1 + num2))

#sumarDosnumeros()

def sumarDosnumerosInt():
    num1 = int(input("Ingrese el numero 1 : "))
    num2 = int(input("Ingrese el numero 2 : "))
    print("La suma de", num1,"+",num2, "es", num1 + num2)

#sumarDosnumerosInt()

def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcular su raiz cuadrada "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada de : ", valor, "es", raiz)

#raizCuadrada()
'''



'''
b = 5
def suma(a,b):
    return a + b

B = 30
A = 10
a = 15

print(suma(a,b))
'''

def otra_suma(numero1,numero2):
    print(numero1 + numero2)
    print("\n")
    return numero1 + numero2

#resultado = otra_suma(5, 6)
# print(resultado)


#creación de la función
def mi_funcion(nombre,apellido):
    miNombre = nombre + apellido
    return miNombre

#Llamar la función
#print(mi_funcion("Luis", "Morelo"))

def saludar(nombre, mensaje='Hola'):
    print(mensaje,nombre)

#saludar('Pepe Grillo')

def mensaje():
    print("Ingrese por favor el valor")

def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())

    return print("la suma de",num1,"+",num2,"es igual a: ",num1 + num2)

#llamar la función
#sumarDosnumeros()

'''
def primeraFuncion(): # función externa
    print("\n \"Hola desde la función externa\" \n")
    def segundaFuncion(): # función interna
        print("\n \"Hola desde la función interna\" \n")
    
    #llamar la función
    segundaFuncion()

#llamar la función
#primeraFuncion()
'''



'''
#crear la función primerNumero
def primerNumero(x):
    def segundoNumero(y):
        return x * y
    return segundoNumero

resultado = primerNumero(2)

print(type(resultado))
print(type(resultado(5)))
print(resultado(5))
'''



def primeraFuncion():
    x = 2
    def segundaFuncion(a):
        x = 10
        print(a + x)
        return x
    
    # llamar la función segundaFuncion
    x = segundaFuncion(3)
    print(x)

# llamar la función primeraFuncion
primeraFuncion()









