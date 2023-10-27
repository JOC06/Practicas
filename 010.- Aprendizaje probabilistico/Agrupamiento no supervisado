
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Genera datos de ejemplo
n_samples = 300
n_features = 2
n_clusters = 3
X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# Crea un objeto KMeans y ajusta el modelo
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Obtiene las etiquetas de los clústeres y los centros de los clústeres
labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Grafica los resultados
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1,], c='red', marker='x', s=200, label='Centros de Clúster')
plt.legend(loc='best')
plt.show()
