# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 00:07:40 2023

@author: User
"""

# Función para calcular el Valor de la Información
def calcular_voi(valor_actual, costo_informacion, valor_con_informacion, probabilidad_exito):
    beneficio_con_informacion = probabilidad_exito * valor_con_informacion
    beneficio_sin_informacion = probabilidad_exito * valor_actual
    beneficio_adicional = beneficio_con_informacion - beneficio_sin_informacion
    voi = beneficio_adicional - costo_informacion
    return voi

# Valores de ejemplo
valor_actual = 10000  # Valor actual de la decisión
costo_informacion = 2000  # Costo de obtener información adicional
valor_con_informacion = 12000  # Valor esperado con información adicional
probabilidad_exito = 0.7  # Probabilidad de éxito con información adicional

# Calcular el Valor de la Información
voi = calcular_voi(valor_actual, costo_informacion, valor_con_informacion, probabilidad_exito)

# Imprimir el resultado
print(f"El Valor de la Información es: {voi}")
#El Valor de la Información (VOI, por sus siglas en inglés) es un concepto utilizado en la toma de decisiones para determinar si la obtención de información adicional justifica el costo asociado. Calcular el VOI implica comparar el beneficio esperado de obtener información adicional con el costo de adquirirla. 
#En este código, la función calcular_voi toma el valor actual de la decisión, el costo de obtener información adicional, el valor esperado con información adicional y la probabilidad de éxito con información adicional. Luego, calcula el beneficio adicional que se obtendría con la información, resta el costo de obtener la información y devuelve el Valor de la Información. El valor de ejemplo para el VOI se imprime al final del código
#Puedes personalizar los valores de ejemplo y utilizar este código como punto de partida para calcular el Valor de la Información en tus propias decisiones.

