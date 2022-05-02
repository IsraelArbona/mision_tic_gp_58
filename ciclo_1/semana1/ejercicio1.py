# declaramos una variable de tipo entero
var_int = 50

# declaramos una variable de tipo float, double
var_pi = 3.1416

# declaramos una variable de tipo cadena de texto (string)
var_str = "Grupo_58"

# declaramos una variable de tipo boolean
var_bol = False

# declaramos una variable de tipo diccionario
var_dict = {
    "nombre": "Juliana",
    "apellido": "Correa",
    "edad": 37
}

# modificar el valor de un campo del diccionario
var_dict["nombre"] = "Maria"
# agregar un campo al diccionario
var_dict["peso"] = 57.5

# eliminar un campo del diccionario
var_dict.pop("apellido")

'''
    Comentar un bloque de código -- con tres comillas sencillas
print("El nombre de la persona es " + var_dict["nombre"] + " y tiene " + str(var_dict["edad"]))
print("El nombre de la persona es " + var_dict["nombre"] + " y tiene", var_dict["edad"])
print(f"El nombre de la persona es {var_dict['nombre']} y tiene {var_dict['edad']}")

print("el nombre de la persona es",var_dict["nombre"],"y tiene",var_dict["edad"])

print("El nombre de la persona es {} y tiene {}".format(var_dict["nombre"],var_dict["edad"]))

print(f"El valor de la variable pi es {var_pi}")
'''


var = "3.7.1"
print(var)
print(type(var))

var = 1.2
print(var)
print(type(var))

var = var + 1
print(var)
print(type(var))

var = 100
print(var)
print(type(var))

var = 200 + 300
print(var)
print(type(var))




