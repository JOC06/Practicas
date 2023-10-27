# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:50:08 2023

@author: JOCELYNE
"""

from sympy import symbols, Not, Or, simplify

# Definición de variables
x, y = symbols('x y')

# Expresión con cuantificador existencial
existencial_expr = Or(x > 0, Or(Not(y < 0), Not(y > 5)))

# Skolemización (aproximación)
skolem_expr = simplify(existencial_expr)

print("Expresión original con cuantificador existencial:")
print(existencial_expr)
print("Expresión skolemizada (aproximada):")
print(skolem_expr)