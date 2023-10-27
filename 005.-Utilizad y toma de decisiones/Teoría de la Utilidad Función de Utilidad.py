# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:39:48 2023

@author: User
"""

def funcion_de_utilidad(cantidad_bienes, precio, elasticidad=1.0):
    """
    Calcula la función de utilidad para un consumidor dado un conjunto de bienes y precios.

    Args:
    cantidad_bienes (list): Lista de cantidades de bienes consumidas.
    precio (list): Lista de precios de los bienes.
    elasticidad (float): Parámetro de elasticidad.

    Returns:
    float: Valor de la función de utilidad.
    """
    if len(cantidad_bienes) != len(precio):
        raise ValueError("Las listas de cantidades y precios deben tener la misma longitud.")

    utilidad = 0.0
    for i in range(len(cantidad_bienes)):
        utilidad += cantidad_bienes[i] ** elasticidad / precio[i]

    return utilidad

# Ejemplo de uso
cantidades = [2, 3]  # Cantidad de dos bienes
precios = [1, 2]     # Precios de los dos bienes
elasticidad = 1.5   # Elasticidad de la función de utilidad

utilidad_total = funcion_de_utilidad(cantidades, precios, elasticidad)
print("La utilidad total es:", utilidad_total)
# La teoría de la utilidad se utiliza comúnmente en economía para modelar las preferencias de los individuos. 
#Este código define una función llamada funcion_de_utilidad que calcula la utilidad total de un consumidor dadas las cantidades de bienes consumidas y los precios de esos bienes. Puedes ajustar la elasticidad para cambiar la forma de la función de utilidad. En este ejemplo, se utiliza una función de utilidad Cobb-Douglas con elasticidad de 1.5.

#Puedes modificar las listas cantidades y precios, así como la elasticidad según tus necesidades para calcular diferentes valores de utilidad.
