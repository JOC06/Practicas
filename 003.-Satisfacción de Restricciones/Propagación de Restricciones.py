# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:42:42 2023

@author: User
"""

from constraint import Problem

# Definimos una función para verificar si dos regiones son adyacentes
def regiones_adyacentes(region1, region2):
    # Define aquí tus restricciones para la adyacencia de regiones
    # Puedes usar una matriz de adyacencia o cualquier otra lógica específica para tu problema
    return True

# Creamos una instancia del problema
problem = Problem()

# Definimos las variables (en este caso, regiones) y su dominio (en este caso, colores)
regiones = ["A", "B", "C", "D"]
colores = ["Rojo", "Verde", "Azul"]

problem.addVariables(regiones, colores)

# Agregamos restricciones para asegurarnos de que regiones adyacentes no tengan el mismo color
for region1 in regiones:
    for region2 in regiones:
        if region1 != region2 and regiones_adyacentes(region1, region2):
            problem.addConstraint(lambda color1, color2: color1 != color2, (region1, region2))

# Encontramos una solución
soluciones = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solucion in soluciones:
    print(solucion)
    #Claro, puedo proporcionarte un ejemplo básico de un código para la propagación de restricciones en Python utilizando la biblioteca constraint. La propagación de restricciones es útil para resolver problemas de programación con restricciones (CSP).
    #Asegúrate de personalizar la función regiones_adyacentes para reflejar las restricciones específicas de tu problema. Este es solo un ejemplo simple para mostrarte cómo se usa la biblioteca constraint en Python para resolver problemas de propagación de restricciones.
    