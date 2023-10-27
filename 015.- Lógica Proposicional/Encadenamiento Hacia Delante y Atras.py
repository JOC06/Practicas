# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:19:46 2023

@author: Dell
"""

# Definición de reglas
reglas = {
    "Regla 1": {"if": ["A"], "then": "B"},
    "Regla 2": {"if": ["B"], "then": "C"},
    "Regla 3": {"if": ["C"], "then": "D"},
    "Regla 4": {"if": ["D"], "then": "E"},
    "Regla 5": {"if": ["E"], "then": "F"},
    "Regla 6": {"if": ["F"], "then": "G"}
}

# Hechos iniciales y objetivo
hechos_iniciales = ["A"]
hecho_objetivo = "G"

def encadenamiento_hacia_adelante(reglas, hechos_iniciales, hecho_objetivo):
    hechos = set(hechos_iniciales)
    cambio = True

    while cambio:
        cambio = False

        for regla, contenido in reglas.items():
            condiciones = contenido.get("if")
            resultado = contenido.get("then")

            if resultado not in hechos and all(condicion in hechos for condicion in condiciones):
                hechos.add(resultado)
                print(f"Se aplicó la {regla}: {condiciones} => {resultado}")
                cambio = True

        if hecho_objetivo in hechos:
            print(f"Se ha alcanzado el hecho objetivo: {hecho_objetivo}")
            return True

    print(f"No se pudo alcanzar el hecho objetivo: {hecho_objetivo}")
    return False

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
    print("Ejemplo de Encadenamiento hacia Adelante y hacia Atrás:")
    
    print("\nUsando Encadenamiento hacia Adelante:")
    encadenamiento_hacia_adelante(reglas, hechos_iniciales, hecho_objetivo)
    
    print("\nUsando Encadenamiento hacia Atrás:")
    encadenamiento_hacia_atras(reglas, hecho_objetivo)
