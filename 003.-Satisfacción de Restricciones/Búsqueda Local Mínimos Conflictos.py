# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:47:08 2023

@author: User
"""

import random

def initial_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def num_conflicts(state, queen_index):
    conflicts = 0
    for i in range(len(state)):
        if i == queen_index:
            continue
        if state[i] == state[queen_index] or abs(state[i] - state[queen_index]) == abs(i - queen_index):
            conflicts += 1
    return conflicts

def min_conflicts(csp, max_steps=1000):
    state = initial_state(len(csp))
    for _ in range(max_steps):
        conflict_queens = [i for i in range(len(csp)) if num_conflicts(state, i) > 0]
        if not conflict_queens:
            return state
        queen_to_move = random.choice(conflict_queens)
        min_conflict_value = float('inf')
        min_conflict_pos = state[queen_to_move]
        for pos in range(len(csp)):
            if pos != state[queen_to_move]:
                state[queen_to_move] = pos
                conflict_count = num_conflicts(state, queen_to_move)
                if conflict_count < min_conflict_value:
                    min_conflict_value = conflict_count
                    min_conflict_pos = pos
        state[queen_to_move] = min_conflict_pos
    return None

def print_board(state):
    for row in state:
        for col in range(len(state)):
            if col == state[row]:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    n = 8  # Cambia el valor de 'n' para ajustar el tamaño del tablero.
    solution = min_conflicts(range(n))
    if solution:
        print("Solución encontrada:")
        print_board(solution)
    else:
        print("No se encontró una solución después de un número máximo de iteraciones.")
#El algoritmo de búsqueda local para resolver problemas de "Mínimos Conflictos" es una técnica utilizada para encontrar soluciones en problemas de satisfacción de restricciones (CSP, por sus siglas en inglés). 
#Este código resuelve el problema de las N-Queens utilizando el algoritmo de Mínimos Conflictos. Ajusta el valor de n en la parte superior del script para cambiar el tamaño del tablero y encontrar soluciones para diferentes valores de N.
