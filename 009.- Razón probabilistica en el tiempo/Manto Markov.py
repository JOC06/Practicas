# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:24:54 2023

@author: JOCELYNE
"""

import random

# Definir la matriz de transición de la cadena de Markov
# En este ejemplo, asumimos que tenemos dos estados: "A" y "B"
# Las probabilidades de transición se definen como P(A|A), P(B|A), P(A|B), P(B|B)
# Puedes ajustar estas probabilidades según tu necesidad.

transition_matrix = {
    "A": {"A": 0.7, "B": 0.3},
    "B": {"A": 0.4, "B": 0.6}
}

# Función para predecir el siguiente estado
def predict_next_state(current_state):
    probabilities = transition_matrix[current_state]
    next_state = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
    return next_state

# Inicializamos el estado inicial
current_state = "A"

# Generar una secuencia de estados
num_steps = 10  # Número de pasos en la secuencia
sequence = [current_state]

for _ in range(num_steps):
    next_state = predict_next_state(current_state)
    sequence.append(next_state)
    current_state = next_state

# Imprimir la secuencia generada
print("Secuencia generada:", " -> ".join(sequence))