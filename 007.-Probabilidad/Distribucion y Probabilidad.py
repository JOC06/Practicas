# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:50:25 2023

@author: JOCELYNE
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
media = 5  # Media de la distribución
desviacion_estandar = 2  # Desviación estándar de la distribución

# Generar datos aleatorios siguiendo una distribución normal
num_muestras = 1000
datos = np.random.normal(media, desviacion_estandar, num_muestras)

# Calcular estadísticas básicas
media_datos = np.mean(datos)
desviacion_estandar_datos = np.std(datos)
varianza_datos = np.var(datos)

# Visualización del histograma de los datos generados
plt.hist(datos, bins=30, density=True, alpha=0.6, color='g')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Normal')
plt.grid(True)

# Mostrar estadísticas
print(f"Media de los datos: {media_datos}")
print(f"Desviación estándar de los datos: {desviacion_estandar_datos}")
print(f"Varianza de los datos: {varianza_datos}")

# Mostrar el gráfico
plt.show()
