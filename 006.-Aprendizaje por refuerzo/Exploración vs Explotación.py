# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:03:21 2023

@author: User
"""

import numpy as np

# Número de brazos en el bandit multi-armed
num_brazos = 5

# Verdadera recompensa media para cada brazo (puede ser desconocida en la práctica)
recompensas_verdaderas = np.random.normal(0, 1, num_brazos)

# Inicialización del promedio estimado de recompensas y recuento de selección de brazos
promedio_estimado = np.zeros(num_brazos)
contador_seleccion = np.zeros(num_brazos)

# Número total de iteraciones (tiradas de brazo)
num_iteraciones = 1000

# Parámetro epsilon para equilibrar exploración y explotación
epsilon = 0.1

# Historial de recompensas obtenidas
recompensas_historial = []

for i in range(num_iteraciones):
    if np.random.random() < epsilon:
        # Exploración: elige un brazo al azar
        brazo_elegido = np.random.choice(num_brazos)
    else:
        # Explotación: elige el brazo con el promedio estimado más alto
        brazo_elegido = np.argmax(promedio_estimado)

    # Simular la recompensa para el brazo elegido
    recompensa = np.random.normal(recompensas_verdaderas[brazo_elegido], 1)
    
    # Actualizar el promedio estimado y el contador de selección del brazo
    contador_seleccion[brazo_elegido] += 1
    promedio_estimado[brazo_elegido] += (recompensa - promedio_estimado[brazo_elegido]) / contador_seleccion[brazo_elegido]

    # Registrar la recompensa obtenida en el historial
    recompensas_historial.append(recompensa)

# Calcular la recompensa total acumulada
recompensa_total = sum(recompensas_historial)

print(f"Recompensa total acumulada: {recompensa_total}")

# Puedes analizar el historial de recompensas obtenidas para evaluar el rendimiento
#Este código implementa un algoritmo epsilon-greedy para equilibrar la exploración (con probabilidad epsilon) y la explotación (con probabilidad 1 - epsilon) en un problema de bandit multi-armed. Puedes ajustar el valor de epsilon para controlar el equilibrio entre exploración y explotación. Cuanto menor sea epsilon, más énfasis se pondrá en la explotación.

#Ten en cuenta que en un entorno real, las recompensas verdaderas no serían conocidas, pero este ejemplo las simula para ilustrar el concepto. En la práctica, tendrías que adaptar el algoritmo para aprender de las recompensas observadas.






Re