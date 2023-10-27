# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:50:52 2023

@author: Javier
"""

import numpy as np

# Definición del MDP
num_estados = 3
num_acciones = 2
transiciones = np.zeros((num_estados, num_acciones, num_estados))  # Matriz de transiciones
recompensas = np.zeros((num_estados, num_acciones))  # Matriz de recompensas
descuento = 0.9

# Configuración de las probabilidades de transición y recompensas (Ejemplo simple)
transiciones[0, 0, 0] = 0.7
transiciones[0, 0, 1] = 0.3
transiciones[0, 1, 1] = 1.0
transiciones[1, 0, 0] = 0.2
transiciones[1, 0, 2] = 0.8
transiciones[1, 1, 2] = 0.9
recompensas[0, 0] = 5
recompensas[0, 1] = 1
recompensas[1, 0] = 2
recompensas[1, 1] = 0
recompensas[2, 0] = 0
recompensas[2, 1] = 0

# Algoritmo de iteración de valores
valores = np.zeros(num_estados)
tolerancia = 1e-6

while True:
    delta = 0
    for estado in range(num_estados):
        v = valores[estado]
        nuevos_valores = []
        for accion in range(num_acciones):
            suma = 0
            for nuevo_estado in range(num_estados):
                suma += transiciones[estado, accion, nuevo_estado] * (recompensas[estado, accion] + descuento * valores[nuevo_estado])
            nuevos_valores.append(suma)
        valores[estado] = max(nuevos_valores)
        delta = max(delta, abs(v - valores[estado]))
    if delta < tolerancia:
        break

# Imprimir los valores óptimos
print("Valores óptimos de los estados:")
for estado, valor in enumerate(valores):
    print(f"Estado {estado}: {valor:.2f}")