# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:59:30 2023

@author: JOCELYNE
"""

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Supongamos que tienes un conjunto de datos X (características) y y (etiquetas)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([3, 5, 7, 9])

# Crea un modelo de regresión lineal
modelo = LinearRegression()

# Realiza validación cruzada con 3 divisiones (puedes ajustar el número de divisiones según tus necesidades)
puntuaciones = cross_val_score(modelo, X, y, cv=3, scoring='r2')

# La variable "puntuaciones" contendrá las puntuaciones R cuadrado para cada división
# Puedes cambiar 'r2' a otras métricas de evaluación, como 'mean_squared_error' o 'accuracy' según tu problema.

print("Puntuaciones de validación cruzada:", puntuaciones)
print("Puntuación media:", np.mean(puntuaciones))
