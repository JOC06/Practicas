# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:51:38 2023

@author: Javier
"""

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Crear la red bayesiana
bn = BayesianNetwork([('A', 'B'), ('A', 'C')])

# Crear tablas de probabilidad condicional para los nodos A, B y C
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.3], [0.2, 0.8]], evidence=['A'], evidence_card=[2])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.5, 0.5], [0.4, 0.6]], evidence=['A'], evidence_card=[2])

bn.add_cpds(cpd_a, cpd_b, cpd_c)

# Agregar un nodo de decisión
bn.add_node('D')

# Crear la tabla de probabilidad condicional para el nodo de decisión D
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.4], [0.6]])

bn.add_cpds(cpd_d)

# Imprimir información sobre la red bayesiana
print("Red Bayesiana:")
print(bn.get_cpds())