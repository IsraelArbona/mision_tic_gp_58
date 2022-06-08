# creación de archivos txt

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_58\ciclo_1\semana5\archivo.txt'

# Crear o Escritura el archivo txt
fichero = open(ruta,'w')

# Agregar información al final del archivo txt
fichero = open(ruta,'a')

# Solo lectura de un archivo txt
fichero = open(ruta,'r')

fichero.close()
