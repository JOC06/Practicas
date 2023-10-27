# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:45:08 2023

@author: JOCELYNE
"""

reglas_diagnosticas = {
    "Regla 1": {"Síntoma A": "Causa X"},
    "Regla 2": {"Síntoma B": "Causa Y"},
    "Regla 3": {"Síntoma A": "Causa Z", "Síntoma B": "Causa Y"},
    "Regla 4": {"Síntoma C": "Causa X"}
}

# Función para realizar el diagnóstico
def diagnosticar_sintomas(sintomas, reglas):
    causas_posibles = set()

    for regla, causas in reglas.items():
        sintomas_coincidentes = set(sintomas) & set(causas.keys())
        if sintomas_coincidentes == set(causas.keys()):
            causas_posibles.update(set(causas.values()))

    return causas_posibles

# Síntomas observados
sintomas_observados = ["Síntoma A", "Síntoma C"]

# Realizar el diagnóstico
causas_posibles = diagnosticar_sintomas(sintomas_observados, reglas_diagnosticas)

if causas_posibles:
    print("Posibles causas identificadas:", causas_posibles)
else:
    print("No se pudo identificar una causa con los síntomas observados.")