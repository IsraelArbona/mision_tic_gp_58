# creamos la función
def genero(letraGenero):
    pass # no se realiza ninguna secuencia de la función
    #return letraGenero

#print(genero("M"))


# Crear una función que me permita obtener el promedio de cuatro notas
# y que el resultado del promedio sea un decimal con un digito.

nota1 = 4.3
nota2 = 3.2
nota3 = 2
nota4 = 4.7

def calPromedio():
    promedio = round( (nota1 + nota2 + nota3 + nota4)/4,1 )
    return promedio

print(calPromedio())

def cPromedio(nota1,nota2,nota3,nota4):
    promedio = (nota1 + nota2 + nota3 + nota4)/4
    return round(promedio,1)

print(cPromedio(nota1, nota2, nota3, nota4))

def promedioNotas():
    nota1 = 4.3
    nota2 = 3.2
    nota3 = 2
    nota4 = 4.7

    promedio = (nota1 + nota2 + nota3 + nota4)/4
    return round(promedio,1)

print(promedioNotas())