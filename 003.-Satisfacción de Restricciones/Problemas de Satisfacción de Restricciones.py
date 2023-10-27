# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:23:28 2023

@author: User
"""

from constraint import Problem

# Define el problema
problem = Problem()

# Define las variables (países) y sus dominios (colores)
countries = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

for country in countries:
    problem.addVariable(country, colors)

# Define las restricciones (países adyacentes no pueden tener el mismo color)
problem.addConstraint(lambda a, b: a != b, ("A", "B"))
problem.addConstraint(lambda a, b: a != b, ("A", "C"))
problem.addConstraint(lambda a, b: a != b, ("A", "D"))
problem.addConstraint(lambda b, c: b != c, ("B", "C"))
problem.addConstraint(lambda c, d: c != d, ("C", "D"))

# Encuentra la solución
solutions = problem.getSolutions()

# Imprime las soluciones encontradas
for solution in solutions:
    print(solution)