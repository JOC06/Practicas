# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:32:53 2023

@author: JOCELYNE
"""

# Función que utiliza lógica superior para tomar una decisión basada en múltiples condiciones
def tomar_decision(condicion1, condicion2, condicion3):
    if condicion1 and condicion2:
        decision = "Tomar acción A"
    elif condicion2 or condicion3:
        decision = "Tomar acción B"
    else:
        decision = "Tomar acción predeterminada"
    return decision

# Simulación de condiciones
condicion1 = True
condicion2 = False
condicion3 = True

# Llamada a la función para tomar una decisión
decision = tomar_decision(condicion1, condicion2, condicion3)

# Imprimir la decisión
print("La decisión es:", decision)