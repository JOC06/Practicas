

import random

# Función de ejemplo para la optimización. Reemplázala con tu propia función.
def objective_function(x):
    return -x**2 + 4*x - 4

def hill_climbing(max_iterations):
    # Generar un punto inicial aleatorio
    current_solution = random.uniform(-10, 10)
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generar un vecino cercano
        neighbor = current_solution + random.uniform(-0.1, 0.1)
        neighbor_value = objective_function(neighbor)

        # Si el vecino es mejor, muévete a él
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

if __name__ == "__main__":
    max_iterations = 1000
    best_solution, best_value = hill_climbing(max_iterations)

    print("Mejor solución encontrada:", best_solution)
    print("Valor de la función en la mejor solución:", best_value)

    #La búsqueda de ascenso de colinas, o Hill Climbing en inglés, es un algoritmo de optimización que se utiliza para encontrar un máximo local en una función. 
    #El algoritmo comienza con una solución aleatoria y realiza iteraciones para buscar vecinos cercanos que tengan un valor de función superior. Si encuentra un vecino mejor, se mueve hacia él.