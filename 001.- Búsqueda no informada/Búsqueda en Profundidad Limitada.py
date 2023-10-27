

def ldfs(graph, start, limit, depth=0):
    if depth > limit:
        return
    
    print(start, end=' ')

    for neighbor in graph[start]:
        ldfs(graph, neighbor, limit, depth + 1)

# Ejemplo de un grafo representado como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Búsqueda en Profundidad Limitada (LDFS):")
ldfs(graph, 'A', 2)  # Limitar la profundidad a 2

#La búsqueda en profundidad limitada (Limited Depth-First Search, LDFS) es una variante de la búsqueda en profundidad (DFS) en la que se establece un límite máximo en la profundidad hasta la cual se explorarán los nodos. 
#Si la profundidad actual supera el límite establecido, la función retorna sin explorar más allá de ese punto. De lo contrario, sigue explorando los nodos vecinos hasta el límite de profundidad establecido.