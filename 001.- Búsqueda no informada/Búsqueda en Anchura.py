from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para llevar un seguimiento de los nodos visitados
    queue = deque()  # Cola para realizar la búsqueda en anchura

    queue.append(start)  # Inicializamos la cola con el nodo de inicio

    while queue:
        node = queue.popleft()  # Sacamos el primer nodo de la cola
        if node not in visited:
            print(node)  # Realiza alguna acción con el nodo, en este caso lo imprimimos
            visited.add(node)  # Marcamos el nodo como visitado

            # Agregamos los nodos vecinos no visitados a la cola
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo representado como un diccionario de listas de adyacencia
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Recorrido BFS a partir del nodo 'A':")
    bfs(graph, 'A')
    