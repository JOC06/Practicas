# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:51:13 2023

@author: Javier
"""

import numpy as np

# Definir las constantes del POMDP
num_states = 2
num_actions = 2
num_observations = 2
discount_factor = 0.9

# Definir las matrices de transición, recompensa y observación
# Esto es un ejemplo, debes proporcionar valores reales
transition_matrix = np.array([
    # Acción 0
    [
        [0.7, 0.3],
        [0.4, 0.6]
    ],
    # Acción 1
    [
        [0.2, 0.8],
        [0.9, 0.1]
    ]
])

reward_matrix = np.array([
    # Acción 0
    [1.0, 0.0],
    # Acción 1
    [0.0, 2.0]
])

observation_matrix = np.array([
    # Acción 0
    [
        [0.8, 0.2],
        [0.1, 0.9]
    ],
    # Acción 1
    [
        [0.6, 0.4],
        [0.3, 0.7]
    ]
])

# Función para actualizar la creencia del agente
def update_belief(belief, action, observation):
    new_belief = np.zeros(num_states)
    for s in range(num_states):
        for sp in range(num_states):
            new_belief[sp] += observation_matrix[action, s, sp] * belief[s]
    new_belief /= np.sum(new_belief)
    return new_belief

# Función para tomar una decisión óptima utilizando la estrategia de política óptima
def optimal_policy(belief):
    expected_rewards = []
    for a in range(num_actions):
        expected_reward = np.sum(belief * (reward_matrix[a] + discount_factor * np.dot(transition_matrix[a], belief)))
        expected_rewards.append(expected_reward)
    return np.argmax(expected_rewards)

# Inicializar la creencia
initial_belief = np.array([0.5, 0.5])

# Simular una secuencia de decisiones y observaciones
for _ in range(5):
    action = optimal_policy(initial_belief)
    observation = np.random.choice(num_observations, p=observation_matrix[action, :])
    print(f"Taking action {action}, observing {observation}")
    initial_belief = update_belief(initial_belief, action, observation)