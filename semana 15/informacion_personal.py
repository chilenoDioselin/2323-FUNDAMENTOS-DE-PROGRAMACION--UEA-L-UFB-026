# Diccionario
informacion_personal = {
'nombre':'Dioselin Chileno',
'edad':21,
'ciudad':'Tarapoa',
'provincia':'Sucumbios',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Tarapoa'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Estudiante Universitaria'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0994857254'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)