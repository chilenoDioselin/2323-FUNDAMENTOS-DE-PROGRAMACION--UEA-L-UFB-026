# Definición de la matriz bidimensional
matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para ordenar una fila específica de la matriz en orden ascendente
def ordenar_fila(matrix, fila):
    matrix[fila] = sorted(matrix[fila])

# Fila a ordenar
fila_a_ordenar = 1

# Mostrar matriz original
print("Matriz original:")
for fila in matrix:
    print(fila)

# Llamada a la función de ordenación
ordenar_fila(matrix, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matrix:
    print(fila)
