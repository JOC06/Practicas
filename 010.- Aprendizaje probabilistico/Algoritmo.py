# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:13:08 2023

@author: JOCELYNE
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Genera datos de ejemplo
np.random.seed(0)
n_samples = 300
X = np.concatenate((np.random.normal(0, 1, int(0.7 * n_samples)),
                    np.random.normal(5, 1, int(0.3 * n_samples))))[:, np.newaxis]

# Ajusta un modelo GMM con EM
n_components = 2  # Número de componentes (clústeres)
gmm = GaussianMixture(n_components=n_components)

# Ajusta el modelo a los datos
gmm.fit(X)

# Predice las etiquetas de los puntos de datos
labels = gmm.predict(X)

# Imprime los parámetros del modelo
print("Medias estimadas:", gmm.means_)
print("Covarianzas estimadas:", gmm.covariances_)

# Grafica los resultados
plt.scatter(X, np.zeros_like(X), c=labels, s=40, cmap='viridis')
plt.show()