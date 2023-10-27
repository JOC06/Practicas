# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:45:20 2023

@author: User
"""

from pgmpy.models import DynamicBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Crear el modelo de la Red Bayesiana Dinámica
model = DynamicBayesianNetwork()

# Definir las variables aleatorias y sus relaciones temporales
# En este ejemplo, tenemos dos variables: A y B en dos instantes de tiempo (t1 y t2).
model.add_edge('A_t1', 'A_t2')
model.add_edge('B_t1', 'B_t2')

# Definir las distribuciones condicionales de probabilidad (CPD) para las variables en t1
cpd_a_t1 = TabularCPD(variable='A_t1', variable_card=2, values=[[0.7], [0.3]])
cpd_b_t1 = TabularCPD(variable='B_t1', variable_card=2, values=[[0.6], [0.4]])

# Definir las CPD para las variables en t2
cpd_a_t2 = TabularCPD(variable='A_t2', variable_card=2, values=[[0.8, 0.2], [0.1, 0.9]], evidence=['A_t1'], evidence_card=[2])
cpd_b_t2 = TabularCPD(variable='B_t2', variable_card=2, values=[[0.7, 0.3], [0.5, 0.5]], evidence=['B_t1'], evidence_card=[2])

# Asociar las CPD con las variables en el modelo
model.add_cpds(cpd_a_t1, cpd_b_t1, cpd_a_t2, cpd_b_t2)

# Verificar si el modelo es válido
assert model.check_model()

# Realizar inferencia en la DBN
inference = DBNInference(model)
result = inference.query(variables=['A_t2'], evidence={'B_t1': 0}, show_progress=False)
print(result)
#Crear un código completo de una Red Bayesiana Dinámica (DBN) es un proyecto complejo que requeriría un lenguaje de programación específico y un contexto detallado.
#Este código crea un modelo simple de una DBN con dos variables, A y B, en dos instantes de tiempo, t1 y t2. Define las CPD para las variables en cada instante de tiempo y luego realiza una consulta de inferencia para estimar la probabilidad de la variable A en t2 dado que B en t1 es 0.

#Recuerda que este es un ejemplo básico y las DBN pueden ser mucho más complejas en aplicaciones del mundo real. Puedes personalizar y expandir este código según tus necesidades específicas.