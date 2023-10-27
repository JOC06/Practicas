# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:46:03 2023

@author: Javier
"""

import networkx as nx

# Crear un grafo para representar la DBN
dbn = nx.DiGraph()

# Definir los nodos de tiempo t y t+1
t0_nodes = ['Clima_t0']
t1_nodes = ['Clima_t1']

# Definir las probabilidades iniciales en t0
prob_clima_t0 = {'Soleado': 0.7, 'Lluvioso': 0.3}

# Definir las transiciones en t+1 dadas las condiciones en t0
prob_clima_t1_given_t0 = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Agregar los nodos y las probabilidades al grafo
dbn.add_node('Clima_t0', values=['Soleado', 'Lluvioso'], prob=prob_clima_t0)
dbn.add_node('Clima_t1', values=['Soleado', 'Lluvioso'], prob=prob_clima_t1_given_t0)

# Agregar arcos que representan la dependencia temporal
dbn.add_edge('Clima_t0', 'Clima_t1')

# Visualizar el grafo
import matplotlib.pyplot as plt

pos = nx.spring_layout(dbn, seed=42)
nx.draw(dbn, pos, with_labels=True, node_size=1000, node_color='lightblue')
labels = nx.get_edge_attributes(dbn, 'prob')
nx.draw_networkx_edge_labels(dbn, pos, edge_labels=labels, font_size=10)
plt.title("Dynamic Bayesian Network (DBN) - Clima")
plt.show()
