# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:27:46 2023

@author: Dell
"""

from sympy import symbols, And, Not, Or, Implies

# Definimos las variables simbólicas
p, q, r = symbols('p q r')

# Reglas lógicas
reglas = [
    Implies(p, q),           # Regla 1: Si p, entonces q
    Implies(And(q, r), p),   # Regla 2: Si q y r, entonces p
    Implies(Or(p, q), r)     # Regla 3: Si p o q, entonces r
]

# Hechos iniciales
hechos = [Or(p, q), Not(r)]  # Hechos iniciales (p o q) y no r

# Función para aplicar inferencia lógica
def inferencia_logica(reglas, hechos):
    cambios = True

    while cambios:
        cambios = False
        nuevas_reglas = []

        for regla in reglas:
            antecedente, consecuente = regla.args

            if antecedente in hechos and consecuente not in hechos:
                hechos.append(consecuente)
                cambios = True
            else:
                nuevas_reglas.append(regla)

        reglas = nuevas_reglas

    return hechos

# Realizamos la inferencia lógica
resultados = inferencia_logica(reglas, hechos)

# Imprimimos los hechos deducidos
print("Hechos deducidos:")
for hecho in resultados:
    print(hecho)
