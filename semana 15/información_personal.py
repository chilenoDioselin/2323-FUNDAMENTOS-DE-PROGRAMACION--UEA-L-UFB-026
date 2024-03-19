# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Chileno Mendoza Dioselin Gabriela",
    "Edad": 21,
    "Ciudad": "Tarapoa-Cuyabeno",
    "Profesion": "estudio de tercer nivel en proceso-Tecnologias de la información"
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "0994857254"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")