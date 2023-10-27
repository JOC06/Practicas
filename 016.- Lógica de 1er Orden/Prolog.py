# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:49:50 2023

@author: JOCELYNE
"""

from pyswip import Prolog

# Crear una instancia de Prolog
prolog = Prolog()

# Definir hechos
prolog.assertz("padre(juan, pedro)")
prolog.assertz("padre(pedro, ana)")

# Definir una regla
prolog.assertz("abuelo(X, Y) :- padre(X, Z), padre(Z, Y)")

# Consulta
for solucion in prolog.query("abuelo(X, Y)"):
    print(solucion["X"], "es abuelo de", solucion["Y"])