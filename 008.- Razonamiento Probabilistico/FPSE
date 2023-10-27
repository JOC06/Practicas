import numpy as np
import matplotlib.pyplot as plt

# Generar una serie temporal sintética
np.random.seed(0)
true_values = np.linspace(0, 10, 100) + np.random.normal(0, 1, 100)

# Inicialización del filtro de Kalman
def kalman_filter(initial_state, initial_covariance, process_noise, measurement_noise):
    state = initial_state
    covariance = initial_covariance

    filtered_state_means = []
    predicted_state_means = []
    smoothed_state_means = []

    for measurement in true_values:
        # Predicción del estado siguiente
        predicted_state = state
        predicted_covariance = covariance + process_noise

        # Actualización del estado basado en la medición
        kalman_gain = predicted_covariance / (predicted_covariance + measurement_noise)
        state = predicted_state + kalman_gain * (measurement - predicted_state)
        covariance = (1 - kalman_gain) * predicted_covariance

        filtered_state_means.append(state)
        predicted_state_means.append(predicted_state)

    return filtered_state_means, predicted_state_means

# Parámetros del filtro de Kalman
initial_state = 0
initial_covariance = 1
process_noise = 0.01
measurement_noise = 1

# Realizar el filtrado
filtered_state_means, predicted_state_means = kalman_filter(initial_state, initial_covariance, process_noise, measurement_noise)

# Realizar el suavizado (en orden inverso)
smoothed_state_means, _ = kalman_filter(filtered_state_means[-1], initial_covariance, process_noise, measurement_noise)
smoothed_state_means = list(reversed(smoothed_state_means))

# Graficar resultados
plt.figure(figsize=(12, 6))
plt.plot(true_values, label='Valores Verdaderos')
plt.plot(filtered_state_means, label='Filtrado de Kalman', linestyle='--')
plt.plot(predicted_state_means, label='Predicción de Kalman', linestyle=':')
plt.plot(smoothed_state_means, label='Suavizado de Kalman', linestyle='-.')
plt.legend()
plt.title('Filtrado, Predicción y Suavizado con el Filtro de Kalman')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()
