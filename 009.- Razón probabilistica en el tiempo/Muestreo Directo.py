# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:25:13 2023

@author: JOCELYNE
"""

import random

# Distribución de probabilidad discreta (ejemplo)
probabilities = {
    'A': 0.3,
    'B': 0.2,
    'C': 0.5
}

# Función para realizar muestreo directo
def direct_sampling(probabilities):
    random_value = random.uniform(0, 1)
    cumulative_probability = 0

    for item, prob in probabilities.items():
        cumulative_probability += prob
        if random_value < cumulative_probability:
            return item

# Realizar muestreo directo
sample = direct_sampling(probabilities)
print("Muestreo Directo:", sample)