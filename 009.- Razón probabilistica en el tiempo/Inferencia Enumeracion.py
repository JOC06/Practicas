# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:22:59 2023

@author: JOCELYNE
"""

# Definir la matriz de transición de la cadena de Markov
transition_matrix = {
    "A": {"A": 0.7, "B": 0.3},
    "B": {"A": 0.4, "B": 0.6}
}

# Función para realizar inferencia por enumeración
def enumeration_inference(sequence, target_state):
    total_probability = 1.0
    current_state = sequence[0]

    for i in range(1, len(sequence)):
        next_state = sequence[i]
        transition_probability = transition_matrix[current_state][next_state]
        total_probability *= transition_probability
        current_state = next_state

    return total_probability

# Secuencia de observaciones
observed_sequence = ["A", "A", "B", "B"]

# Estado objetivo para calcular su probabilidad
target_state = "A"

# Calcular la probabilidad del estado objetivo dada la secuencia de observaciones
probability = enumeration_inference(observed_sequence, target_state)

print(f"La probabilidad de estar en el estado '{target_state}' después de la secuencia es: {probability:.4f}")