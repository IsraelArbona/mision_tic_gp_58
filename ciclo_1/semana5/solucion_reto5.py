import pandas as pd

# ruta del archivo csv
# rutaFileCsv = 'C:\\Users\\israelarbonaguerrero\\Desktop\\RUTA2_MISIONTIC_2022\\grupo_58\\ciclo_1\\semana5\\movies.csv'


rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'

def listaPeliculas(rutaFileCsv: str)->str:
    # print(rutaFileCsv.split('.')[-1])

    # validar extensión archivo
    if rutaFileCsv.split('.')[-1] == 'csv':
        
        try:
            # Leer el archivo csv
            aCsv = pd.read_csv(rutaFileCsv)
            #print(aCsv)

            # Se crea un subconjunto con las columnas 'Country', 'Language' e 'Gross Earnings'.
            subGrupoPeliculas = aCsv[['Country','Language','Gross Earnings']]
            # print(subGrupoPeliculas)

            # Se usa las columnas 'Country' y 'Language' como índice para la tabla dinámica y 
            # 'Gross Earnings' como tabla de resumen
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=['Country','Language'])
            return gananciaPaisLenguaje.head(10)

        except:
            print('Error al leer el archivo de datos.')

    else:
        print('Extensión inválida.') 

print(listaPeliculas(rutaFileCsv))
