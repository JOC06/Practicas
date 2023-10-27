# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:00:00 2023

@author: JOCELYNE
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Supongamos que tienes características (X) y etiquetas (y)
X, y = # Aquí debes cargar tus datos de entrenamiento

# Divide los datos en conjuntos de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un modelo de regresión logística
modelo = LogisticRegression()

# Entrena el modelo en el conjunto de entrenamiento
modelo.fit(X_train, y_train)

# Evalúa el modelo en el conjunto de validación
puntuacion = modelo.score(X_val, y_val)

print("Precisión en el conjunto de validación:", puntuacion)
