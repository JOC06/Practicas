# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:19:04 2023

@author: JOCELYNE
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
n = 100  # Número de pasos
mean = 0.0  # Media de los pasos
std = 1.0  # Desviación estándar de los pasos

# Generar una secuencia de pasos aleatorios
steps = np.random.normal(mean, std, n)

# Calcular la caminata aleatoria acumulativa
walk = np.cumsum(steps)

# Crear una gráfica de la caminata aleatoria
plt.plot(walk)
plt.title('Caminata Aleatoria Estacionaria')
plt.xlabel('Pasos')
plt.ylabel('Valor')
plt.show()