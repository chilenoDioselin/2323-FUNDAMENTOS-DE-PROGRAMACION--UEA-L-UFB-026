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

#Iterando sobre las ciudades, semanas y días para calcular el promedio de temperaturas
for ciudad_index, ciudad in enumerate(temperaturas, start=1):
    print(f'CIUDAD No. {ciudad_index}')
    for semana_index, semana in enumerate(ciudad, start=1):
        # Calculando el promedio de temperaturas para la semana actual
        temperatura_semana = [dia["temp"] for dia in semana]  # Lista de temperaturas de la semana
        promedio_semana = sum(temperatura_semana) / len(temperatura_semana)  # Calculando el promedio
        print(f'El promedio de la semana No. {semana_index} es: {promedio_semana:.2f}')