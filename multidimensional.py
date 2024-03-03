# Matriz 3D para almacenar datos de temperaturas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada semana en cada ciudad
for ciudad_idx, ciudad in enumerate(temperaturas, start=1):
    print(f"Promedio de temperaturas para Ciudad {ciudad_idx}:")
    for semana_idx, semana in enumerate(ciudad, start=1):
        suma_temperaturas = sum(dia['temp'] for dia in semana)
        promedio_temperaturas = suma_temperaturas / len(semana)
        print(f"  Semana {semana_idx}: {promedio_temperaturas:.2f}°C")
    print()
