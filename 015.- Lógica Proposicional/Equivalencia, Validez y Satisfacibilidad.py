# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:26:17 2023

@author: Dell
"""

from sympy import symbols, Implies, Equivalent, And, Or, Not, satisfiable, ask

# Definimos las variables simbólicas
p, q, r = symbols('p q r')

# Definimos dos expresiones lógicas
expresion1 = Equivalent(Implies(p, q), Or(Not(p), q))  # Ley de implicación
expresion2 = And(Or(p, q), Or(Not(p), r))  # Expresión conjuntiva

# Verificamos la equivalencia de las expresiones
if expresion1.equals(expresion2):
    print("Las expresiones son equivalentes.")
else:
    print("Las expresiones no son equivalentes.")

# Verificamos la validez de una expresión (si es verdadera para todas las asignaciones)
expresion3 = Or(p, Not(p))
if ask(expresion3, True):
    print("La expresión es válida (siempre verdadera).")
else:
    print("La expresión no es válida.")

# Verificamos la satisfacibilidad de una expresión (si es verdadera para al menos una asignación)
expresion4 = And(p, Not(q))
if satisfiable(expresion4):
    print("La expresión es satisfacible (al menos una asignación la hace verdadera).")
else:
    print("La expresión no es satisfacible (siempre falsa).")
