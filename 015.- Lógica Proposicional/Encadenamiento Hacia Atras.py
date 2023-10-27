# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:16:04 2023

@author: Dell
"""

# Definición de reglas
reglas = {
    "Regla 1": {"if": "A", "then": "B"},
    "Regla 2": {"if": "B", "then": "C"},
    "Regla 3": {"if": "C", "then": "D"},
    "Regla 4": {"if": "D", "then": "E"}
}

# Hecho objetivo
hecho_objetivo = "E"

def encadenamiento_hacia_atras(reglas, hecho_objetivo):
    if hecho_objetivo in reglas:
        print(f"Se ha alcanzado el hecho objetivo: {hecho_objetivo}")
        return True

    for regla, contenido in reglas.items():
        if contenido["then"] == hecho_objetivo:
            condiciones = contenido["if"]
            print(f"Intentando aplicar la {regla}: {condiciones} => {hecho_objetivo}")
            for condicion in condiciones:
                if not encadenamiento_hacia_atras(reglas, condicion):
                    print(f"No se pudo aplicar la {regla} debido a la condición: {condicion}")
                    return False
            print(f"Se aplicó la {regla}: {condiciones} => {hecho_objetivo}")
            return True

    print(f"No se encontró una regla que conduzca al hecho objetivo: {hecho_objetivo}")
    return False

if __name__ == "__main__":
    print("Ejemplo de Encadenamiento hacia Atrás:")
    if encadenamiento_hacia_atras(reglas, hecho_objetivo):
        print(f"Se ha alcanzado el hecho objetivo: {hecho_objetivo}")
    else:
        print(f"No se pudo alcanzar el hecho objetivo: {hecho_objetivo}")
