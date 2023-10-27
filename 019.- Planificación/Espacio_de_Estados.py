
from collections import deque

class Estado:
    def __init__(self, nodo_actual, camino):
        self.nodo_actual = nodo_actual
        self.camino = camino

def bfs(grafo, inicio, objetivo):
    frontera = deque([Estado(inicio, [inicio])])
    visitados = set()

    while frontera:
        estado_actual = frontera.popleft()
        nodo_actual = estado_actual.nodo_actual

        if nodo_actual == objetivo:
            return estado_actual.camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    nuevo_camino = list(estado_actual.camino)
                    nuevo_camino.append(vecino)
                    frontera.append(Estado(vecino, nuevo_camino))

    return None

# Ejemplo de uso
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    nodo_inicio = 'A'
    nodo_objetivo = 'F'

    camino = bfs(grafo, nodo_inicio, nodo_objetivo)

    if camino:
        print(f"Camino encontrado: {camino}")
    else:
        print("No se encontró un camino.")