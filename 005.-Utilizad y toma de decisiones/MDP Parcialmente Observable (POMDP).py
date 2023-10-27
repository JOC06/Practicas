# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:36:20 2023

@author: User
"""

import numpy as np

# Definir el número de estados, acciones y observaciones
num_states = 5
num_actions = 2
num_observations = 3

# Definir las probabilidades de transición (T), observación (O) y recompensa (R)
T = np.array([[[0.7, 0.3, 0.0, 0.0, 0.0],
              [0.3, 0.7, 0.0, 0.0, 0.0]],
             [[0.0, 0.0, 0.4, 0.6, 0.0],
              [0.0, 0.0, 0.3, 0.7, 0.0]],
             [[0.0, 0.0, 0.0, 0.0, 1.0]]])

O = np.array([[[0.8, 0.1, 0.1],
              [0.1, 0.7, 0.2]],
             [[0.2, 0.2, 0.6],
              [0.1, 0.1, 0.8]],
             [[0.0, 0.0, 1.0]]])

R = np.array([[1.0, 0.0],
             [0.0, 0.0],
             [0.0]])

# Definir la función de política
def policy(state):
    return 0 if state < num_states - 1 else 1

# Algoritmo de resolución de POMDP (Programación Dinámica)
def solve_pomdp(T, O, R, policy, num_states, num_actions, num_observations):
    value_function = np.zeros(num_states)
    num_iterations = 100

    for iteration in range(num_iterations):
        new_value_function = np.zeros(num_states)
        for state in range(num_states):
            action = policy(state)
            expected_return = 0
            for next_state in range(num_states):
                for observation in range(num_observations):
                    expected_return += T[action, state, next_state] * O[action, next_state, observation] * (
                            R[next_state] + value_function[next_state])
            new_value_function[state] = expected_return
        value_function = new_value_function

    return value_function

# Calcular la función de valor óptimo
optimal_value_function = solve_pomdp(T, O, R, policy, num_states, num_actions, num_observations)

# Imprimir la función de valor óptimo
print("Función de Valor Óptimo:")
print(optimal_value_function)
#Crear un código completo de un POMDP (Problema de Toma de Decisiones Parcialmente Observable) es un proceso complejo y dependerá de la plataforma y lenguaje de programación que desees utilizar. 
#Este es un ejemplo simple de un POMDP en Python que utiliza programación dinámica para calcular la función de valor óptimo. Ten en cuenta que en aplicaciones prácticas, los POMDPs suelen ser mucho más complejos y requieren algoritmos de solución más avanzados, como la programación lineal estocástica o técnicas de aprendizaje profundo.
