# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:49:46 2023

@author: Javier
"""

import random

# Definición del modelo de decisión (laberinto)
estados = [(0, 0), (0, 1), (1, 0), (1, 1)]
acciones = ["adelante", "derecha"]

# Recompensas asociadas a cada casilla
recompensas = {
    (0, 0): -1,
    (0, 1): 10,
    (1, 0): -1,
    (1, 1): 1,
}

# Probabilidades de transición determinísticas
transiciones = {
    (0, 0): {"adelante": (0, 1), "derecha": (1, 0)},
    (0, 1): {"adelante": (1, 1), "derecha": (0, 0)},
    (1, 0): {"adelante": (1, 1), "derecha": (0, 0)},
    (1, 1): {"adelante": (1, 0), "derecha": (0, 1)},
}

# Inicialización de los valores de los estados
valores = {estado: 0 for estado in estados}

# Inicialización de la política (acciones aleatorias)
politica = {estado: random.choice(acciones) for estado in estados}

# Hiperparámetro de descuento (factor de descuento)
descuento = 0.9

# Algoritmo de iteración de políticas
for _ in range(100):
    nuevos_valores = {}
    for estado in estados:
        accion = politica[estado]
        nuevo_estado = transiciones[estado][accion]
        suma = recompensas[estado] + descuento * valores[nuevo_estado]
        nuevos_valores[estado] = suma
    valores = nuevos_valores

    # Actualizar la política
    for estado in estados:
        mejor_accion = None
        max_valor = float("-inf")
        for accion in acciones:
            nuevo_estado = transiciones[estado][accion]
            valor = recompensas[estado] + descuento * valores[nuevo_estado]
            if valor > max_valor:
                max_valor = valor
                mejor_accion = accion
        politica[estado] = mejor_accion

# Imprimir la política óptima
print("Política óptima:")
for estado, accion in politica.items():
    print(f"En el estado {estado}, tomar la acción: {accion}")