# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:25:56 2023

@author: JOCELYNE
"""

import random

# Función de densidad de probabilidad de una distribución (ejemplo)
def pdf(x):
    if x >= 0 and x <= 1:
        return 2 * x
    return 0

# Función para realizar muestreo por rechazo
def rejection_sampling(pdf, x_min, x_max):
    while True:
        x = random.uniform(x_min, x_max)
        y = random.uniform(0, pdf(x_max))
        
        if y <= pdf(x):
            return x

# Realizar muestreo por rechazo
x_min = 0
x_max = 1
sample = rejection_sampling(pdf, x_min, x_max)
print("Muestreo por Rechazo:", sample)