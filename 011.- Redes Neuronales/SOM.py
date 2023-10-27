# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:10:45 2023

@author: JOCELYNE
"""

import numpy as np
from sklearn.datasets import load_iris
from minisom import MiniSom
import matplotlib.pyplot as plt

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Normalizar los datos
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

# Definir el tamaño del SOM
map_size = (10, 10)  # Tamaño del SOM

# Crear el SOM
som = MiniSom(map_size[0], map_size[1], X.shape[1], sigma=1.0, learning_rate=0.5)

# Inicializar los pesos aleatoriamente
som.random_weights_init(X)

# Entrenar el SOM
som.train_batch(X, 1000, verbose=True)

# Visualizar el SOM y los grupos resultantes
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Mapa de distancias
plt.colorbar()

# Mapear cada instancia de datos al nodo ganador del SOM
winners = np.array([som.winner(x) for x in X])  # Para cada instancia, encuentra el nodo ganador

for i, (x, y) in enumerate(winners):
    plt.text(x+0.5, y+0.5, str(y), ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5))

plt.xticks(np.arange(0, map_size[0], 1))
plt.yticks(np.arange(0, map_size[1], 1))
plt.grid()
plt.show()