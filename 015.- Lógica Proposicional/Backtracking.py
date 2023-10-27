# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:09:27 2023

@author: Dell
"""

def es_seguro(tablero, fila, columna, N):
    # Verifica si es seguro colocar una reina en la fila y columna dadas
    # Verifica la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verifica la diagonal izquierda superior
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verifica la diagonal derecha superior
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, fila, N):
    if fila == N:
        # Todas las reinas se han colocado con éxito
        return True

    for columna in range(N):
        if es_seguro(tablero, fila, columna, N):
            tablero[fila][columna] = 1
            if resolver_n_reinas(tablero, fila + 1, N):
                return True
            tablero[fila][columna] = 0

    return False

def imprimir_tablero(tablero):
    N = len(tablero)
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()

def n_reinas(N):
    tablero = [[0] * N for _ in range(N)]
    if resolver_n_reinas(tablero, 0, N):
        print(f"Solución para {N} reinas:")
        imprimir_tablero(tablero)
    else:
        print(f"No hay solución para {N} reinas.")

if __name__ == "__main__":
    N = 8  # Número de reinas
    n_reinas(N)
