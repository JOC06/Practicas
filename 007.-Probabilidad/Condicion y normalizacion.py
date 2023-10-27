# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:48:39 2023

@author: JOCELYNE
"""

# Datos de la urna
bolas = {'roja': 10, 'verde': 20, 'azul': 15}

# Función para calcular la probabilidad condicionada
def probabilidad_condicionada(color, condicion):
    if color in bolas and condicion in bolas:
        prob_condicionada = bolas[color] / bolas[condicion]
    else:
        prob_condicionada = 0.0
    return prob_condicionada

# Calcular la probabilidad condicionada de obtener una bola roja dado que es azul
color_deseado = 'roja'
condicion = 'azul'
prob_cond = probabilidad_condicionada(color_deseado, condicion)

# Normalización para asegurarse de que la suma de todas las probabilidades sea 1
suma_probabilidades = sum(probabilidad_condicionada(color, condicion) for color in bolas)
probabilidades_normalizadas = {color: probabilidad_condicionada(color, condicion) / suma_probabilidades for color in bolas}

print(f"Probabilidad condicionada de obtener una bola {color_deseado} dado que es {condicion}: {prob_cond}")
print("Probabilidades normalizadas:")
for color, prob in probabilidades_normalizadas.items():
    print(f"Probabilidad de obtener una bola {color}: {prob}")
