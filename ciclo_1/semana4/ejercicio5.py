# importar pow
from math import pow

#la función pow toma dos argumentos, el numero y potecia
# print(pow(2,3))

numeros  = [2,3,4,5,6,7,8,9]
potencias = [3,2,4,3,2,4,3,2]

print(numeros)
print(potencias)

resultado = list(map(pow,numeros,potencias))
print(resultado)