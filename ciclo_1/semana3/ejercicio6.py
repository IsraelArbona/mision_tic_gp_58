# Inicializar las tareas pendiente  -- diccionario.

tareas = {
    '01': {
        'descripcion': 'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02': {
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180
    },
    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}

# Crear una nueva tarea.
def create(tareas,identificador,tareaNueva):
    tareas[identificador] = tareaNueva
    return tareas

# Listado de tareas pendientes.
def read(tareas):
    for identificador,tarea in tareas.items():
        print(identificador, ' - ',end='')
        for nomAtributo,atributo in tarea.items():
            print(atributo, ' ,', end='')
        print()
    print()

# validar si una tarea existe.
def validarTarea(identificador,tareas):
    if identificador in tareas:
        return True
    else:
        return False

opcion = 0

while opcion != 5:

    print('\n --- Aplicación del CRUD tareas pendientes --- \n')
    print(' 1: Adicionar Tarea')
    print(' 2: Consultar Tarea')
    print(' 3: Actulizar Tarea')
    print(' 4: Eliminar Tarea')
    print(' 5: Salir')

    opcion = int(input('Ingrese una opción : '))

    if opcion == 1:
        print()
        print('-> Adicionar tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea : '))

        if not validarTarea(identificador, tareas):
            descripcion = str(input('Ingrese la descripción de la tarea : '))
            estado = str(input('Ingrese el estado de la tarea : '))
            tiempo = int(input('Ingresar el tiempo de realización de la tarea : '))

            tareaNueva = {
                'descripcion': descripcion,
                'estado': estado,
                'tiempo' : tiempo
            }

            # llamar a la función para crear la tarea. 
            tareas = create(tareas,identificador,tareaNueva)
        else:
            print('La tarea ya existe!')

    elif opcion == 2:
        print()
        print('-> Listado de tareas')
        print()

        # llamar a la funcion para listar todas las tareas pendiente.
        read(tareas)
    
    elif opcion == 3:
        print()
        print('-> Actulizar tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea a modificar : '))

        if validarTarea(identificador,tareas):
            nuevaDescripcion = str(input('Nueva descripción : '))
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado : '))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = int(input('Nuevo tiempo : '))
            if nuevoTiempo:
                tareas[identificador]['tiempo'] = nuevoTiempo
        else:
            print('No ha sido encontrada la tarea.')

    elif opcion == 4:
        print()
        print('-> Eliminar tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea a eliminar : '))

        if validarTarea(identificador, tareas):
            tareas.pop(identificador)
        else:
            print('La tarea pendiente no fue encontrada.')