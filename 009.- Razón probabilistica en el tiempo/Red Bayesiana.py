# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:26:38 2023

@author: JOCELYNE
"""

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Crear un objeto BayesianNetwork
model = BayesianNetwork([('D', 'G'), ('I', 'G'), ('G', 'L')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, 
                   values=[[0.8, 0.6, 0.4, 0.2],
                           [0.1, 0.3, 0.5, 0.3],
                           [0.1, 0.1, 0.1, 0.5]],
                   evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])

# Asignar las CPDs al modelo
model.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l)

# Comprobar si el modelo es válido
assert model.check_model()

# Realizar inferencia utilizando VariableElimination
inference = VariableElimination(model)

# Calcular la probabilidad de L dado D=True
result = inference.query(variables=['L'], evidence={'D': 1})
print(result)

# Calcular la probabilidad de G dado D=True, I=True
result = inference.query(variables=['G'], evidence={'D': 1, 'I': 1})
print(result)