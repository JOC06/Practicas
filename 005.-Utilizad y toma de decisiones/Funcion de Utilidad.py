# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:49:34 2023

@author: Javier
"""

# Definir la función de utilidad
def funcion_utilidad(opcion):
    if opcion == "opcion_A":
        return 10
    elif opcion == "opcion_B":
        return 8
    else:
        return 0  # Valor por defecto si la opción no es reconocida

# Calcular la utilidad de cada opción
opcion_A = "opcion_A"
opcion_B = "opcion_B"

utilidad_A = funcion_utilidad(opcion_A)
utilidad_B = funcion_utilidad(opcion_B)

# Comparar las utilidades
if utilidad_A > utilidad_B:
    print("El agente prefiere la opción A.")
elif utilidad_B > utilidad_A:
    print("El agente prefiere la opción B.")
else:
    print("El agente es indiferente entre las dos opciones.")