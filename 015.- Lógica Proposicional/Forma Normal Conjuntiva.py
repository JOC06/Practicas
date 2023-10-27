# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:21:26 2023

@author: Dell
"""

from sympy import symbols, Or, And, Not, to_cnf, simplify

# Definimos las variables simbólicas
p, q, r = symbols('p q r')

# Definimos la fórmula original
formula_original = And(Or(p, q), Or(Not(p), r))

# Convertimos la fórmula a Forma Normal Conjuntiva (FNC)
formula_fnc = to_cnf(formula_original, True)

# Aplicamos simplificaciones adicionales para obtener una FNC más simple
formula_fnc_simplificada = simplify(formula_fnc)

print("Fórmula Original:")
print(formula_original)
print("\nFórmula en Forma Normal Conjuntiva (FNC):")
print(formula_fnc)
print("\nFórmula FNC Simplificada:")
print(formula_fnc_simplificada)
