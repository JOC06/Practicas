

import random

# Función objetivo (puedes cambiarla según tu problema)
def objective_function(x):
    return x**2

# Parámetros del algoritmo
num_candidates = 10  # Número de candidatos en cada iteración
num_iterations = 100  # Número de iteraciones
search_range = (-10, 10)  # Rango de búsqueda

# Función para generar candidatos iniciales
def generate_initial_candidates(num_candidates, search_range):
    return [random.uniform(search_range[0], search_range[1]) for _ in range(num_candidates)]

# Función para evaluar la función objetivo en una lista de candidatos
def evaluate_candidates(candidates):
    return [objective_function(x) for x in candidates]

# Función de búsqueda de haz local
def local_beam_search(num_candidates, num_iterations, search_range):
    current_candidates = generate_initial_candidates(num_candidates, search_range)
    
    for iteration in range(num_iterations):
        candidate_values = evaluate_candidates(current_candidates)
        best_candidate_index = candidate_values.index(min(candidate_values))
        best_candidate = current_candidates[best_candidate_index]
        
        new_candidates = [best_candidate + random.uniform(-0.1, 0.1) for _ in range(num_candidates)]
        current_candidates = new_candidates
    
    best_solution = min(evaluate_candidates(current_candidates))
    return best_solution

# Ejecutar la búsqueda de haz local
best_solution = local_beam_search(num_candidates, num_iterations, search_range)
print("Mejor solución encontrada:", best_solution)