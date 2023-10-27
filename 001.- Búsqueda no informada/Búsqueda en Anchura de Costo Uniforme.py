import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]  # Cola de prioridad para explorar nodos por costo ascendente

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)  # Sacamos el nodo con el menor costo
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost  # Devolvemos el costo mínimo para llegar al objetivo

        for neighbor, edge_cost in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + edge_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return float('inf')  # Devolvemos infinito si no se encuentra una ruta

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo ponderado representado como un diccionario de diccionarios
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 5},
        'C': {'A': 2, 'D': 0},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    goal_node = 'D'

    cost = uniform_cost_search(graph, start_node, goal_node)

    if cost != float('inf'):
        print(f"El costo mínimo de {start_node} a {goal_node} es {cost}.")
    else:
        print(f"No se encontró una ruta de {start_node} a {goal_node}.")