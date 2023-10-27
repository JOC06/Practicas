# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:18:11 2023

@author: Dell
"""


import pandas as pd
from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent
from itertools import product

# Función para generar una tabla de verdad
def tabla_de_verdad(expresion):
    # Obtenemos las variables en la expresión
    variables = list(expresion.free_symbols)
    
    # Generamos todas las combinaciones de valores para las variables
    combinaciones = list(product([True, False], repeat=len(variables)))
    
    # Evaluar la expresión para cada combinación de valores
    resultados = []
    for combo in combinaciones:
        valores = dict(zip(variables, combo))
        resultado = expresion.subs(valores)
        resultados.append(list(valores.values()) + [resultado])
    
    # Crear un DataFrame de Pandas para la tabla de verdad
    column_names = [str(var) for var in variables] + ["Resultado"]
    tabla = pd.DataFrame(resultados, columns=column_names)
    
    return tabla

# Función para analizar una expresión lógica
def analizar_expresion(expresion_str):
    expresion = eval(expresion_str)  # Evalúa la expresión lógica
    return expresion

def main():
    print("Generador de Tablas de Verdad para Lógica Proposicional")
    expresion_str = input("Ingrese una expresión lógica (usando variables como p, q y operadores como ~, &, |, =>, <=>): ")
    
    try:
        expresion = analizar_expresion(expresion_str)
        tabla = tabla_de_verdad(expresion)
        print("\nTabla de Verdad:")
        print(tabla)
    except Exception as e:
        print("Error al analizar la expresión:", e)

if __name__ == "__main__":
    main()
