# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:12:42 2023

@author: Dell
"""

# Definición de reglas
reglas = {
    "Regla 1": {"if": ["A"], "then": "B"},
    "Regla 2": {"if": ["B"], "then": "C"},
    "Regla 3": {"if": ["C"], "then": "D"},
    "Regla 4": {"if": ["D"], "then": "E"}
}

# Hechos iniciales
hechos = ["A"]

def encadenamiento_hacia_adelante(reglas, hechos):
    cambio = True

    while cambio:
        cambio = False

        for regla, contenido in reglas.items():
            condiciones = contenido.get("if")
            resultado = contenido.get("then")

            if resultado not in hechos and all(condicion in hechos for condicion in condiciones):
                hechos.append(resultado)
                print(f"Se aplicó la {regla}: {condiciones} => {resultado}")
                cambio = True

if __name__ == "__main__":
    print("Ejemplo de Encadenamiento hacia Adelante:")
    print("Hechos iniciales:", hechos)
    encadenamiento_hacia_adelante(reglas, hechos)
    print("Hechos finales:", hechos)
