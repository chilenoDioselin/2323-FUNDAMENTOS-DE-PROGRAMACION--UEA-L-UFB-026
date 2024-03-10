# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 14},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 46},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 45},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 38},
            {"dia": "Domingo", "temp": 34}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 77},
            {"dia": "Martes", "temp": 55},
            {"dia": "Miércoles", "temp": 85},
            {"dia": "Jueves", "temp": 82},
            {"dia": "Viernes", "temp": 50},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 60}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 25}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"dia": "Lunes", "temp": 62},
            {"dia": "Martes", "temp": 64},
            {"dia": "Miércoles", "temp": 68},
            {"dia": "Jueves", "temp": 60},
            {"dia": "Viernes", "temp": 45},
            {"dia": "Sábado", "temp": 50},
            {"dia": "Domingo", "temp": 55}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 63},
            {"dia": "Martes", "temp": 66},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 70},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 70}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 61},
            {"dia": "Martes", "temp": 65},
            {"dia": "Miércoles", "temp": 55},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 72},
            {"dia": "Sábado", "temp": 76},
            {"dia": "Domingo", "temp": 71}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 64},
            {"dia": "Martes", "temp": 67},
            {"dia": "Miércoles", "temp": 69},
            {"dia": "Jueves", "temp": 71},
            {"dia": "Viernes", "temp": 62},
            {"dia": "Sábado", "temp": 65},
            {"dia": "Domingo", "temp": 70}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 38},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 35},
            {"dia": "Viernes", "temp": 45},
            {"dia": "Sábado", "temp": 46},
            {"dia": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 42},
            {"dia": "Martes", "temp": 40},
            {"dia": "Miércoles", "temp": 35},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 84},
            {"dia": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 56},
            {"dia": "Martes", "temp": 50},
            {"dia": "Miércoles", "temp": 40},
            {"dia": "Jueves", "temp": 50},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 86},
            {"dia": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 75},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 89},
            {"dia": "Viernes", "temp": 86},
            {"dia": "Sábado", "temp": 83},
            {"dia": "Domingo", "temp": 80}
        ]
    ]
]
def calcular_promedio(suma_acumulada, total_acumulado):
  """
  Calcula el promedio de dos valores.

  Parámetros:
    suma_acumulada: La suma acumulada de los valores.
    total_acumulado: El número total de valores.

  Retorno:
    El promedio de los valores.
  """
  return round(suma_acumulada / total_acumulado, 2)

# Calcular el promedio de temperaturas para cada ciudad y semana
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad = no_ciudad + 1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 1
        suma = 0
        for dia in semana:
            suma = suma + dia['temp']
        promedio = round(suma / len(semana), 1)
        suma_promedio += promedio
        print(f'El promedio semana No. {no_semana} es: {promedio}')
    promedio_ciudad = round(suma_promedio / len(ciudad), 1)
    print(f'El promedio mensual es: {promedio_ciudad}')
