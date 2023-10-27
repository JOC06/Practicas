# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:58:43 2023

@author: User
"""

import gym
import numpy as np

# Crear el entorno CartPole
env = gym.make('CartPole-v1')

# Parámetros
num_episodes = 1000
learning_rate = 0.1
discount_factor = 0.99
exploration_prob = 0.5
exploration_decay = 0.99

# Inicializar la tabla Q con ceros
state_space_size = env.observation_space.shape[0]
action_space_size = env.action_space.n
Q_table = np.zeros((state_space_size, action_space_size))

# Función para seleccionar una acción epsilon-greedy
def select_action(state):
    if np.random.rand() < exploration_prob:
        return env.action_space.sample()  # Acción aleatoria
    else:
        return np.argmax(Q_table[state, :])  # Acción basada en la tabla Q

# Entrenamiento
for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = select_action(state)
        next_state, reward, done, _ = env.step(action)
        
        # Actualizar la tabla Q
        Q_table[state, action] = Q_table[state, action] + learning_rate * (reward + discount_factor * np.max(Q_table[next_state, :]) - Q_table[state, action])
        
        state = next_state
        total_reward += reward

    # Decrecer la probabilidad de exploración
    exploration_prob *= exploration_decay

    if episode % 10 == 0:
        print(f"Episodio {episode}: Recompensa total = {total_reward}")

# Juego final con el agente entrenado
state = env.reset()
total_reward = 0
done = False

while not done:
    action = np.argmax(Q_table[state, :])
    state, reward, done, _ = env.step(action)
    total_reward += reward

print(f"Juego finalizado con recompensa total de {total_reward}")

# Cerrar el entorno
env.close()
#El aprendizaje por refuerzo activo es una rama de la inteligencia artificial que implica que un agente (como un programa informático) aprenda a tomar decisiones óptimas para maximizar una recompensa a lo largo del tiempo. 
#Este código implementa el algoritmo Q-learning para el entorno CartPole de OpenAI Gym. El agente aprende a equilibrar un poste en un carrito, y el objetivo es maximizar la recompensa. Ten en cuenta que este es un ejemplo simple, y el aprendizaje por refuerzo activo puede ser mucho más complejo en aplicaciones del mundo real. Ajusta los parámetros y el entorno según tus necesidades específicas.
