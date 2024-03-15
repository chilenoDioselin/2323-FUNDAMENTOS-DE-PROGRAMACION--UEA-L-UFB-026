# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Adrian Zambrano",
    "edad": 27,
    "ciudad": "Quito",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "ingeniero civil"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0994567893"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
