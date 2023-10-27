
import heapq

def a_star(graph, start, goal):
    open_set = []  # Cola de prioridad (heap) para nodos abiertos
    heapq.heappush(open_set, (0, start))  # Tupla (f, nodo)
    
    came_from = {}  # Diccionario para almacenar los padres de los nodos
    g_score = {node: float('inf') for node in graph}  # Costo desde el inicio al nodo
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # Costo total estimado
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

def heuristic(node, goal):
    # Implementa tu función heurística aquí
    pass

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path



def ao_star(graph, start, goal):
    open_set = [(0, start)]  # Cola de prioridad (heap) para nodos abiertos
    came_from = {}  # Diccionario para almacenar los padres de los nodos
    g_score = {node: float('inf') for node in graph}  # Costo desde el inicio al nodo
    g_score[start] = 0

    while open_set:
        _, current = open_set.pop(0)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, goal)
                open_set.append((f_score, neighbor))
                open_set.sort(key=lambda x: x[0])
    
    return None

def heuristic(node, goal):
    # Implementa tu función heurística aquí
    pass

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
