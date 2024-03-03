# Definición de la matriz bidimensional
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matrix, valor):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == valor:
                return True, (i, j)
    return False, None

# Valor a buscar
valor_buscar = 5

# Llamada a la función de búsqueda
encontrado, posicion = buscar_valor(matrix, valor_buscar)

# Mostrar resultados
if encontrado:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
