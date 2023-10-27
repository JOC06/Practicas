# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:50:27 2023

@author: Javier
"""

# Definición del modelo de decisión
# Supongamos que tienes un agente que toma decisiones sobre llevar un paraguas o no,
# y los estados representan las condiciones del clima (lluvia o no lluvia).

# Definición de los estados
estados = ["lluvia", "no_lluvia"]

# Definición de las acciones
acciones = ["llevar_paraguas", "no_llevar_paraguas"]

# Probabilidades de transición (matriz de probabilidades de transición)
transiciones = {
    ("lluvia", "llevar_paraguas"): {"lluvia": 0.9, "no_lluvia": 0.1},
    ("lluvia", "no_llevar_paraguas"): {"lluvia": 0.2, "no_lluvia": 0.8},
    ("no_lluvia", "llevar_paraguas"): {"lluvia": 0.1, "no_lluvia": 0.9},
    ("no_lluvia", "no_llevar_paraguas"): {"lluvia": 0.0, "no_lluvia": 1.0},
}

# Recompensas para cada estado (ganancia si la acción es exitosa)
recompensas = {"lluvia": -10, "no_lluvia": 5}

# Hiperparámetro de descuento (factor de descuento)
descuento = 0.9

# Inicialización de los valores de los estados
valores = {estado: 0 for estado in estados}

# Algoritmo de iteración de valores (Bellman)
for _ in range(100):
    nuevos_valores = {}
    for estado in estados:
        max_valor = float("-inf")
        for accion in acciones:
            suma = 0
            for nuevo_estado, prob_transicion in transiciones[(estado, accion)].items():
                suma += prob_transicion * (recompensas[nuevo_estado] + descuento * valores[nuevo_estado])
            max_valor = max(max_valor, suma)
        nuevos_valores[estado] = max_valor
    valores = nuevos_valores

# Imprimir los valores finales
print("Valores óptimos de los estados:")
for estado, valor in valores.items():
    print(f"{estado}: {valor:.2f}")

# Tomar la decisión óptima
decision_optima = {}
for estado in estados:
    max_valor = float("-inf")
    mejor_accion = None
    for accion in acciones:
        suma = 0
        for nuevo_estado, prob_transicion in transiciones[(estado, accion)].items():
            suma += prob_transicion * (recompensas[nuevo_estado] + descuento * valores[nuevo_estado])
        if suma > max_valor:
            max_valor = suma
            mejor_accion = accion
    decision_optima[estado] = mejor_accion

print("\nDecisión óptima en cada estado:")
for estado, accion in decision_optima.items():
    print(f"En el estado {estado}, tomar la acción: {accion}")