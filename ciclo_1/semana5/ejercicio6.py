# leer o escribir en archivo txt

datos = ['linea 1','linea 2','linea 3','linea 4','linea 5']

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.txt'
fichero = open(ruta,'w')

'''
for lie in datos:
    fichero.write(lie)
    fichero.write('\n')
fichero.close()


for i in range(1001):
    for lie in datos:
        variable = str(i) + ', ' + lie
        fichero.write(variable)
    fichero.write('\n')

fichero.close()
'''


ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo_p.txt'
fichero = open(ruta,'w')

'''
for lie in datos:
    print(lie,file=fichero)
fichero.close()
'''

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo_list_comp.txt'
fichero = open(ruta,'w')

fichero.writelines('%s\n' % s for s in datos)
fichero.close()
