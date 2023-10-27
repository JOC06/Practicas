# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:20:32 2023

@author: JOCELYNE
"""

from collections import deque

def bfs(graph, start, goal):
    if start not in graph or goal not in graph:
        return "Nodo de inicio o nodo objetivo no están en el grafo."

    explored = set()
    queue = deque([[start]])

    if start == goal:
        return "Nodo de inicio es igual al nodo objetivo."

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in explored:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            explored.add(node)

    return "No se encontró un camino desde el nodo de inicio al nodo objetivo."

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

start_node = 'A'
goal_node = 'F'

result = bfs(graph, start_node, goal_node)
if isinstance(result, list):
    print(f"Camino desde {start_node} hasta {goal_node}: {result}")
else:
    print(result)