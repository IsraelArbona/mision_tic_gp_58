def cliente(informacion: dict)-> dict:
    
    # uso de variables
    cli_id = informacion['id_cliente']
    cli_nombre = informacion['nombre']
    cli_edad = informacion['edad']
    cli_primerIngreso = informacion['primer_ingreso']

    if cli_edad > 18:
        atraccion = 'X-Treme'
        apto = True
        if cli_primerIngreso == True:
            total_boleta = ( 20000 - (20000 * 0.05) )
        else:
            total_boleta = 20000
    elif cli_edad >= 15 and cli_edad <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if cli_primerIngreso == True:
            total_boleta = 5000 - (5000 * 0.07)
        else:
            total_boleta = 5000
    elif cli_edad >= 7 and cli_edad < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if cli_primerIngreso == True:
            total_boleta = 10000 - (10000 * (5/100))
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    diccionario_respuesta = {
        'nombre': cli_nombre,
        'edad' : cli_edad,
        'atraccion' : atraccion,
        'apto' : apto,
        'primer_ingreso' : cli_primerIngreso,
        'total_boleta' : total_boleta
    }

    return diccionario_respuesta


# Diccionario para realizar las pruebas de la función

'''
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}
'''
# el llamado de la función es para validar las respuestas.
#print(cliente(informacion))