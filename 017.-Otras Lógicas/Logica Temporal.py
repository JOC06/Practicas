# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:32:28 2023

@author: JOCELYNE
"""

from datetime import datetime

class Alimento:
    def __init__(self, nombre, fecha_vencimiento, es_vegetariano):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.es_vegetariano = es_vegetariano

    def se_puede_comer(self):
        ahora = datetime.now()
        if ahora < self.fecha_vencimiento and self.es_vegetariano:
            return f"Se puede comer el alimento {self.nombre}."
        elif ahora >= self.fecha_vencimiento:
            return f"No se puede comer el alimento {self.nombre} porque ha vencido."
        else:
            return f"No se puede comer el alimento {self.nombre}."

# Crear un alimento con fecha de vencimiento
fecha_vencimiento_ensalada = datetime(2023, 12, 31)
ensalada = Alimento("ensalada", fecha_vencimiento_ensalada, es_vegetariano=True)

# Realizar una consulta para saber si se puede comer
decision = ensalada.se_puede_comer()
print(decision)