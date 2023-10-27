import random
import math

# Función objetivo que queremos maximizar (puedes cambiarla según tus necesidades)
def funcion_objetivo(x):
    return -x**2 + 5*x + 10

# Algoritmo Hill Climbing
def hill_climbing(iteraciones, paso, x_inicial):
    x_actual = x_inicial

    for _ in range(iteraciones):
        valor_actual = funcion_objetivo(x_actual)

        # Genera un nuevo candidato dentro del vecindario
        x_candidato = x_actual + random.uniform(-paso, paso)
        valor_candidato = funcion_objetivo(x_candidato)

        # Compara los valores de la función objetivo
        if valor_candidato > valor_actual:
            x_actual = x_candidato

    return x_actual, funcion_objetivo(x_actual)

if __name__ == "__main__":
    # Parámetros del algoritmo
    iteraciones = 1000
    paso = 0.1
    x_inicial = 0

    mejor_x, mejor_valor = hill_climbing(iteraciones, paso, x_inicial)

    print(f"Mejor solución encontrada: x = {mejor_x}, valor = {mejor_valor}")
