# Lista paralelas

nombres1 = ['Juan','Maria','Josue','Marcos','Luz']
edades2 =  [15    ,32     ,25     ,17      ,18]

nombres = list() # nombres = []
edades = list()  # edades  = []

for xpersona in range(5):
    nombre = input('Digite el nombre de la persona: ')
    nombres.append(nombre)
    edad = int(input('Digite la edad de la persona: '))
    edades.append(edad)

print('Nombre de las personas que son mayores o iguales a 18 años')

for xedad in range(5):
    if edades[xedad] >= 18:
        print('Nombre -', nombres[xedad], ' edad : ', edades[xedad])









'''
    print(type(nombres)) # tipo de dato
    print(dir(nombres))  # método del objeto
'''