# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:28:23 2023

@author: JOCELYNE
"""

class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {
            "Cielo nublado": {"Actividad al aire libre": 0.6},
            "Viento fuerte": {"Actividad al aire libre": 0.4},
        }

    def razonar(self, condiciones):
        recomendaciones = {}
        for condicion, valor in condiciones.items():
            if condicion in self.base_conocimiento:
                for actividad, factor in self.base_conocimiento[condicion].items():
                    if actividad not in recomendaciones:
                        recomendaciones[actividad] = 1.0
                    recomendaciones[actividad] *= factor if valor else 1 - factor
        return recomendaciones

# Crear un sistema experto
sistema = SistemaExperto()

# Definir las condiciones meteorológicas
condiciones = {
    "Cielo nublado": True,
    "Viento fuerte": False
}

# Realizar el razonamiento
recomendaciones = sistema.razonar(condiciones)

# Mostrar las recomendaciones
print("Recomendaciones de actividades:")
for actividad, certeza in recomendaciones.items():
    if certeza >= 0.5:
        print(f"{actividad} (Certidumbre: {certeza})")