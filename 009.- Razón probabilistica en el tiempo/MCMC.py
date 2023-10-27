# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:23:29 2023

@author: JOCELYNE
"""

import random
#Monte Carlo para Cadenas de Markov (MCMC) es una técnica utilizada para muestrear valores de una distribución de probabilidad 
# utilizando cadenas de Markov. Uno de los algoritmos MCMC más conocidos es el Método de Metropolis-Hastings. 


# Distribución de probabilidad objetivo (ejemplo)
target_distribution = {
    'A': 0.3,
    'B': 0.4,
    'C': 0.2,
    'D': 0.1
}

# Función para calcular la probabilidad de una muestra según la distribución objetivo
def calculate_target_probability(sample, target_distribution):
    return target_distribution.get(sample, 0)

# Función para realizar MCMC con el Método de Metropolis-Hastings
def metropolis_hastings(target_distribution, num_samples):
    samples = []
    current_sample = random.choice(list(target_distribution.keys()))

    for _ in range(num_samples):
        samples.append(current_sample)

        # Elegir una nueva muestra propuesta de manera aleatoria
        proposed_sample = random.choice(list(target_distribution.keys()))

        # Calcular la razón de aceptación
        acceptance_ratio = (calculate_target_probability(proposed_sample, target_distribution) /
                            calculate_target_probability(current_sample, target_distribution))

        # Aceptar o rechazar la muestra propuesta según la razón de aceptación
        if random.uniform(0, 1) < acceptance_ratio:
            current_sample = proposed_sample

    return samples

# Realizar MCMC con Metropolis-Hastings
num_samples = 1000
samples = metropolis_hastings(target_distribution, num_samples)

# Contar la frecuencia de cada valor muestreado
sample_counts = {value: samples.count(value) / num_samples for value in set(samples)}

# Imprimir los resultados
print("Resultados del MCMC con Metropolis-Hastings:")
for value, frequency in sample_counts.items():
    print(f"{value}: Frecuencia estimada: {frequency:.4f}, Probabilidad objetivo: {target_distribution[value]}")