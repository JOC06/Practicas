# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:44:38 2023

@author: Dell
"""

from sympy import symbols, Not, And, Or, Implies, Equivalent

# Definimos las variables simbólicas
p, q = symbols('p q')

# Creamos expresiones lógicas
expresion1 = And(p, q)  # p AND q
expresion2 = Or(p, q)   # p OR q
expresion3 = Implies(p, q)  # p IMPLIES q
expresion4 = Equivalent(p, q)  # p IF AND ONLY IF q

# Imprimimos las expresiones lógicas
print("Expresión 1 (p AND q):", expresion1)
print("Expresión 2 (p OR q):", expresion2)
print("Expresión 3 (p IMPLIES q):", expresion3)
print("Expresión 4 (p IF AND ONLY IF q):", expresion4)

# Evaluamos las expresiones para algunos valores de p y q
valores = [(True, True), (True, False), (False, True), (False, False)]

for p_valor, q_valor in valores:
    resultado1 = expresion1.subs({p: p_valor, q: q_valor})
    resultado2 = expresion2.subs({p: p_valor, q: q_valor})
    resultado3 = expresion3.subs({p: p_valor, q: q_valor})
    resultado4 = expresion4.subs({p: p_valor, q: q_valor})

    print(f"Para p={p_valor}, q={q_valor}:")
    print(f"Expresión 1 (p AND q) = {resultado1}")
    print(f"Expresión 2 (p OR q) = {resultado2}")
    print(f"Expresión 3 (p IMPLIES q) = {resultado3}")
    print(f"Expresión 4 (p IF AND ONLY IF q) = {resultado4}")
    print()

# También podemos aplicar negación a una expresión lógica
negacion_expresion1 = Not(expresion1)
print("Negación de la Expresión 1 (NOT p AND q):", negacion_expresion1)
