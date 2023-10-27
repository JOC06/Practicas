# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:53:21 2023

@author: Javier
"""

# Probabilidad a priori de tener la enfermedad
probabilidad_enfermedad = 0.01  # 1% de la población

# Probabilidad de un resultado positivo en la prueba dado que tienes la enfermedad
probabilidad_positivo_dado_enfermedad = 0.95  # Sensibilidad

# Probabilidad de un resultado positivo en la prueba dado que no tienes la enfermedad
probabilidad_positivo_dado_no_enfermedad = 0.10  # 10% de falsos positivos

# Calcular la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
def regla_de_bayes(probabilidad_enfermedad, probabilidad_positivo_dado_enfermedad, probabilidad_positivo_dado_no_enfermedad):
    probabilidad_no_enfermedad = 1 - probabilidad_enfermedad
    probabilidad_positivo = (probabilidad_enfermedad * probabilidad_positivo_dado_enfermedad) + (probabilidad_no_enfermedad * probabilidad_positivo_dado_no_enfermedad)
    probabilidad_enfermedad_dado_positivo = (probabilidad_enfermedad * probabilidad_positivo_dado_enfermedad) / probabilidad_positivo
    return probabilidad_enfermedad_dado_positivo

resultado = regla_de_bayes(probabilidad_enfermedad, probabilidad_positivo_dado_enfermedad, probabilidad_positivo_dado_no_enfermedad)

print(f"Probabilidad de tener la enfermedad dado un resultado positivo en la prueba: {resultado:.2%}")