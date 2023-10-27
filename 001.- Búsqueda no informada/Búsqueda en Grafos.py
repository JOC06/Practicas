from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para mantener un registro de nodos visitados
    queue = deque()  # Cola para el recorrido en amplitud

    visited.add(start)  # Marcar el nodo de inicio como visitado
    queue.append(start)  # Agregar el nodo de inicio a la cola

    while queue:
        node = queue.popleft()  # Tomar el primer nodo de la cola
        print(node, end=' ')  # Imprimir el nodo visitado

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Marcar el nodo vecino como visitado
                queue.append(neighbor)  # Agregar el nodo vecino a la cola

# Ejemplo de un grafo representado como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido en Amplitud (BFS):")
bfs(graph, 'A')

#La búsqueda en grafos es una técnica fundamental en ciencia de la computación y se utiliza para resolver una variedad de problemas, desde encontrar rutas en un mapa hasta recorrer estructuras de datos como árboles y grafos. 
#Este código realiza un recorrido en amplitud en un grafo representado como un diccionario de adyacencia. Comienza desde un nodo de inicio (en este caso, 'A') y explora todos los nodos a su alcance antes de moverse a los nodos vecinos. La cola asegura que los nodos se visiten en el orden correcto.
