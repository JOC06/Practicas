# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:25:57 2023

@author: JOCELYNE
"""

class BaseConocimiento:
    def __init__(self):
        self.hechos = {}
        self.reglas = []

    def agregar_hecho(self, hecho, certeza):
        self.hechos[hecho] = certeza

    def agregar_regla(self, antecedente, consecuente, certeza):
        self.reglas.append((antecedente, consecuente, certeza))

    def razonar(self, conclusion):
        certeza_total = 0
        for regla in self.reglas:
            antecedente, consecuente, certeza_regla = regla
            if all(h in self.hechos and self.hechos[h] >= certeza_regla for h in antecedente):
                if consecuente == conclusion:
                    certeza_total += certeza_regla
        return certeza_total

# Crear una base de conocimiento con incertidumbre
base_conocimiento = BaseConocimiento()

# Agregar hechos con certeza
base_conocimiento.agregar_hecho("Cielo nublado", 0.6)
base_conocimiento.agregar_hecho("Viento fuerte", 0.4)

# Agregar reglas con factores de certeza
base_conocimiento.agregar_regla(["Cielo nublado", "Viento fuerte"], "Lluvia", 0.8)
base_conocimiento.agregar_regla(["Cielo nublado"], "Lluvia", 0.5)

# Realizar razonamiento con incertidumbre
certeza_lluvia = base_conocimiento.razonar("Lluvia")

# Mostrar el factor de certeza de lluvia
print(f"Factor de certeza de 'Lluvia': {certeza_lluvia}")