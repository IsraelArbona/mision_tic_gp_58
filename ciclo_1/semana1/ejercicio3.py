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

def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1 : "))
    num2 = float(input("Ingrese el numero 2 : "))
    print("La suma de", int(num1),"+",int(num2), "es", int(num1 + num2))

sumarDosnumeros()

def sumarDosnumerosInt():
    num1 = int(input("Ingrese el numero 1 : "))
    num2 = int(input("Ingrese el numero 2 : "))
    print("La suma de", num1,"+",num2, "es", num1 + num2)

sumarDosnumerosInt()