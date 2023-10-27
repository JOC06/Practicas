

import math
import random

def funcion_objetivo(x):
    # Esta es la función que quieres optimizar.
    # Debes modificarla según tu problema específico.
    return -x**2 + 4*x

def temple_simulado(funcion_objetivo, temperatura_inicial, tasa_enfriamiento, iteraciones):
    mejor_solucion = random.uniform(-10, 10)  # Genera una solución inicial aleatoria
    mejor_valor = funcion_objetivo(mejor_solucion)
    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones):
        nueva_solucion = mejor_solucion + random.uniform(-0.1, 0.1)  # Genera una solución vecina aleatoria
        valor_nueva_solucion = funcion_objetivo(nueva_solucion)

        # Comprueba si la nueva solución es mejor o si se acepta con una cierta probabilidad
        if valor_nueva_solucion > mejor_valor or random.random() < math.exp((valor_nueva_solucion - mejor_valor) / temperatura_actual):
            mejor_solucion = nueva_solucion
            mejor_valor = valor_nueva_solucion

        # Enfría la temperatura
        temperatura_actual *= tasa_enfriamiento

    return mejor_solucion, mejor_valor

if __name__ == "__main__":
    temperatura_inicial = 100.0
    tasa_enfriamiento = 0.95
    iteraciones = 1000

    mejor_solucion, mejor_valor = temple_simulado(funcion_objetivo, temperatura_inicial, tasa_enfriamiento, iteraciones)

    print(f"Mejor solución encontrada: x = {mejor_solucion}, Valor = {mejor_valor}")