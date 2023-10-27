# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:27:01 2023

@author: JOCELYNE
"""

import random

# Probabilidad de lluvia
probabilidad_lluvia = 0.3  # Puedes ajustar esta probabilidad

# Función para tomar una decisión racional
def decision_racional(probabilidad):
    if probabilidad < 0.2:
        return "No llevo paraguas."
    elif probabilidad < 0.6:
        return "Llevo un paraguas por si acaso."
    else:
        return "Definitivamente llevo un paraguas."

# Simular la probabilidad de lluvia
simulacion_probabilidad = random.random()  # Genera un número aleatorio entre 0 y 1

# Tomar una decisión racional basada en la probabilidad simulada
decision = decision_racional(simulacion_probabilidad)

# Mostrar la decisión tomada
print(f"Probabilidad de lluvia: {simulacion_probabilidad}")
print("Decisión:", decision)