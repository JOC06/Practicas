# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:27:58 2023

@author: JOCELYNE
"""

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, antecedente, consecuente):
        self.reglas.append((antecedente, consecuente))

    def razonar(self):
        conclusiones = set()
        for regla in self.reglas:
            antecedente, consecuente = regla
            if all(hecho in self.hechos for hecho in antecedente):
                conclusiones.add(consecuente)
        return conclusiones

# Crear una base de conocimiento para recomendaciones de películas
base_conocimiento = BaseConocimiento()

# Agregar hechos y reglas
base_conocimiento.agregar_hecho("Usuario ha visto 'Matrix'")
base_conocimiento.agregar_hecho("Usuario ha visto 'El Señor de los Anillos'")
base_conocimiento.agregar_hecho("Usuario ha visto 'Star Wars'")

base_conocimiento.agregar_regla({"Usuario ha visto 'Matrix'", "Usuario ha visto 'El Señor de los Anillos'"}, "Recomendar 'Star Wars'")
base_conocimiento.agregar_regla({"Usuario ha visto 'Matrix'", "Usuario ha visto 'Star Wars'"}, "Recomendar 'El Señor de los Anillos'")

# Razonar y obtener recomendaciones
recomendaciones = base_conocimiento.razonar()

# Mostrar las recomendaciones
print("Recomendaciones:")
for recomendacion in recomendaciones:
    print(recomendacion)