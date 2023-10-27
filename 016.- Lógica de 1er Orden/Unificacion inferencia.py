# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:48:47 2023

@author: JOCELYNE
"""


def unificar(termino1, termino2, sustitucion={}):
    if sustitucion is None:
        return None
    elif termino1 == termino2:
        return sustitucion  # Si los términos son iguales, no se requiere ninguna sustitución adicional
    elif isinstance(termino1, str) and not es_variable(termino1):
        return None  # Si termino1 es una constante y no una variable, no se puede unificar con nada
    elif isinstance(termino2, str) and not es_variable(termino2):
        return None  # Si termino2 es una constante y no una variable, no se puede unificar con nada
    elif es_variable(termino1):
        return unificar_variable(termino1, termino2, sustitucion)
    elif es_variable(termino2):
        return unificar_variable(termino2, termino1, sustitucion)
    elif isinstance(termino1, list) and isinstance(termino2, list):
        if len(termino1) != len(termino2):
            return None  # Las listas deben tener la misma longitud para unificarse
        else:
            for i in range(len(termino1)):
                sustitucion = unificar(termino1[i], termino2[i], sustitucion)
            return sustitucion
    else:
        return None  # En otros casos, no se pueden unificar

def es_variable(termino):
    return isinstance(termino, str) and termino.islower()  # Verifica si un término es una variable

def unificar_variable(variable, termino, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], termino, sustitucion)  # Si la variable ya tiene una sustitución, unifica con esa sustitución
    elif termino in sustitucion:
        return unificar(variable, sustitucion[termino], sustitucion)  # Si el término ya tiene una sustitución, unifica con esa sustitución
    else:
        sustitucion[variable] = termino  # Establece una nueva sustitución
        return sustitucion

# Ejemplo de unificación exitosa
expresion1 = ["padre", "X", "Y"]
expresion2 = ["padre", "Juan", "Maria"]

sustitucion = unificar(expresion1, expresion2)

if sustitucion is not None:
    print("Unificación exitosa. Sustitución:")
    for key, value in sustitucion.items():
        print(f"{key} = {value}")
else:
    print("No se puede unificar las expresiones.")