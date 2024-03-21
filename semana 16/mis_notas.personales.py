# Escritura de Archivo de Texto
# Abrir el archivo en modo de escritura
with open('mis_notas.txt', 'w') as archivo:
    # Escribir notas personales en el archivo
    archivo.write("Estas son mis notas personales:\n")
    archivo.write("- Recordar hacer los pedidos de la comida.\n")
    archivo.write("- presentar los deberes de manera puntual.\n")
    archivo.write("- Preparar los deberes hasta el fin de semana.\n")

# Lectura de Archivo de Texto
# Abrir el archivo en modo de lectura
with open('mis_notas.txt', 'r') as archivo:
    # Leer el contenido del archivo línea por línea
    for linea in archivo.readlines():
        # Mostrar cada línea leída en la consola
        print(linea.strip())  # Eliminar espacios en blanco y saltos de línea

# Cierre de Archivo
# El archivo se cierra automáticamente gracias al uso del bloque with
