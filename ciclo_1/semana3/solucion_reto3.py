def AutoPartes(ventas: list):
    # declarar diccionario vacio.
    venta = dict() # venta = {}

    # ciclo para agregar los elementos.
    for idProducto, dProducto, pnProducto, cvProducto, \
        sProducto, nComprador, cComprador, fVenta in ventas:
        # forzar la entrada
        if venta.get(idProducto) == None:
            # Creación de nueva clave
            venta[idProducto] = []

        # Registro de una nueva lista de tuplas en el diccionario.
        venta[idProducto].append( (dProducto, pnProducto, cvProducto, sProducto, \
                                    nComprador, cComprador, fVenta) )

    return venta


# Definir la función a consultar.
def consultaRegistro(ventas, idProducto):
    # Ubicar los idProducto dentro de la diccionario.
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, \
            nComprador, cComprador,fVenta in ventas[idProducto]:

            # Mostrar los registros encontrados.
            print('Producto consultado :', idProducto, ' Descripción ', dProducto, \
                    ' #Parte ', pnProducto, ' Cantidad vendida ', cvProducto, ' Stock ', sProducto, \
                    ' Comprador', nComprador, ' Documento ', cComprador, ' Fecha Venta ', fVenta)
    else:
        # Si no se ubica el producto
        print("No hay registro de venta de ese producto") 



print(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()




'''

(
    [
        (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
        (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
        (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
        (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
        (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
    ]
), 
2010



{
    2001: [('rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020')], 
    2010: [('bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020')], 
    3578: [('tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020')], 
    9251: [('piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]
} 2010


{
    2001: [('rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020')], 
    2010: [('bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'), ('bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020')], 
    3578: [('tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020')], 
    9251: [('piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]} 2010


'''