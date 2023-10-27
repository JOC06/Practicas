# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:58:58 2023

@author: User
"""

import networkx as nx

# Crear un gráfico de red de decisión
G = nx.DiGraph()

# Agregar nodos (eventos y decisiones)
G.add_node("Iniciar", type="decision")
G.add_node("Llueve", type="event")
G.add_node("Tráfico", type="event")
G.add_node("Llegar tarde", type="event")
G.add_node("Tomar sombrilla", type="decision")

# Agregar bordes entre los nodos
G.add_edge("Iniciar", "Llueve")
G.add_edge("Iniciar", "Tráfico")
G.add_edge("Llueve", "Tomar sombrilla")
G.add_edge("Tráfico", "Llegar tarde")
G.add_edge("Llegar tarde", "Tomar sombrilla")

# Asignar probabilidades a los eventos
G.nodes["Llueve"]["prob"] = 0.3
G.nodes["Tráfico"]["prob"] = 0.4
G.nodes["Llegar tarde"]["prob"] = 0.2

# Asignar valores a las decisiones
G.nodes["Iniciar"]["value"] = 0
G.nodes["Tomar sombrilla"]["value"] = 5

# Calcular el valor esperado
def calcular_valor_esperado(G):
    valor_esperado = 0
    for nodo in nx.topological_sort(G):
        if G.nodes[nodo]["type"] == "event":
            padre = list(G.predecessors(nodo))[0]
            valor_esperado += G.nodes[nodo]["prob"] * G.nodes[padre]["value"]
    return valor_esperado

valor_esperado = calcular_valor_esperado(G)
print(f"El valor esperado de la red de decisión es: {valor_esperado}")
#hemos creado una red de decisión simple que modela la decisión de si llevar una sombrilla en función de si llueve, si hay tráfico y si llegas tarde. Luego, calculamos el valor esperado de tomar la decisión de llevar una sombrilla. Puedes personalizar este código para adaptarlo a tu problema específico y añadir más nodos y aristas según sea necesario.