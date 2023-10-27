# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:30:10 2023

@author: JOCELYNE
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables lingüísticas (antecedentes y consecuente)
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_comida')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad_servicio')
calidad = ctrl.Consequent(np.arange(0, 11, 1), 'calidad_general')

# Definir funciones de membresía para las variables lingüísticas
comida.automf(3)
servicio.automf(3)
calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

# Definir reglas difusas
regla1 = ctrl.Rule(comida['pobre'] | servicio['pobre'], calidad['baja'])
regla2 = ctrl.Rule(servicio['aceptable'], calidad['media'])
regla3 = ctrl.Rule(servicio['buena'] | comida['buena'], calidad['alta'])

# Crear un sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear un simulador de sistema de control
sistema_simulacion = ctrl.ControlSystemSimulation(sistema_control)

# Asignar valores a las entradas
sistema_simulacion.input['calidad_comida'] = 6.5
sistema_simulacion.input['calidad_servicio'] = 9.8

# Realizar la evaluación difusa
sistema_simulacion.compute()

# Obtener el resultado
resultado = sistema_simulacion.output['calidad_general']
print("Calidad general del restaurante:", resultado)

# Graficar las funciones de membresía
comida.view()
servicio.view()
calidad.view()

# Graficar la salida
calidad.view(sim=sistema_simulacion)