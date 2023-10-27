# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:51:41 2023

@author: User
"""

import numpy as np

# Definir el entorno (laberinto) como una matriz de recompensas
# -1 representa obstáculos, 0 representa espacios transitables, y 100 es el objetivo
environment = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, -1, -1, -1, 100]
])

# Tasa de aprendizaje
learning_rate = 0.1

# Factor de descuento
discount_factor = 0.9

# Número de episodios de entrenamiento
num_episodes = 1000

# Inicializar la tabla Q con ceros
q_table = np.zeros((5, 5))

# Función para seleccionar la acción óptima basada en la tabla Q
def choose_action(state):
    return np.argmax(q_table[state])

# Entrenamiento
for episode in range(num_episodes):
    state = (0, 1)  # Estado inicial (fila, columna)
    while state != (4, 4):  # No hemos llegado al objetivo
        action = choose_action(state)
        next_state = (state[0] + 1, state[1])  # Simulación de movimiento hacia abajo
        reward = environment[next_state[0]][next_state[1]]
        q_table[state] = q_table[state] + learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[state])
        state = next_state

# Imprimir la tabla Q resultante
print("Tabla Q:")
print(q_table)

# Prueba del agente entrenado
state = (0, 1)
path = [state]
while state != (4, 4):
    action = choose_action(state)
    next_state = (state[0] + 1, state[1])  # Simulación de movimiento hacia abajo
    path.append(next_state)
    state = next_state

print("Camino óptimo:")
for step in path:
    print(step)
    #El Aprendizaje por Refuerzo Pasivo es una rama del aprendizaje automático que implica que un agente aprenda a realizar acciones óptimas en un entorno a través de la observación de ejemplos en lugar de interactuar activamente con el entorno.
    #En este ejemplo, se entrena al agente para encontrar el camino óptimo desde la posición inicial (0, 1) hasta el objetivo (4, 4) en un laberinto simple. El agente aprende de los ejemplos de estados y recompensas óptimas observadas en el entorno.

#Ten en cuenta que este es un ejemplo muy básico del aprendizaje por refuerzo pasivo. En aplicaciones más complejas, se pueden utilizar algoritmos más avanzados y entornos más complicados.