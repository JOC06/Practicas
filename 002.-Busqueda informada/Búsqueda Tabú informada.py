

import random

# Función objetivo de ejemplo (puede ser reemplazada por tu problema específico)
def funcion_objetivo(solucion):
    return sum(solucion)

# Generación de una solución inicial de ejemplo (lista de números)
def generar_solucion_inicial(num_elementos):
    return [random.randint(0, 100) for _ in range(num_elementos)]

# Vecindad de una solución: perturbación simple (puede ser personalizada)
def perturbar_solucion(solucion):
    indice = random.randint(0, len(solucion) - 1)
    nueva_solucion = solucion[:]
    nueva_solucion[indice] = random.randint(0, 100)
    return nueva_solucion

# Algoritmo de búsqueda tabú
def busqueda_tabu(num_iteraciones, tamano_lista_tabu):
    mejor_solucion = generar_solucion_inicial(10)
    mejor_valor = funcion_objetivo(mejor_solucion)
    lista_tabu = []
    
    for _ in range(num_iteraciones):
        vecindad = [perturbar_solucion(mejor_solucion) for _ in range(10)]
        mejor_vecino = min(vecindad, key=lambda x: funcion_objetivo(x))
        
        if funcion_objetivo(mejor_vecino) < mejor_valor and mejor_vecino not in lista_tabu:
            mejor_solucion = mejor_vecino
            mejor_valor = funcion_objetivo(mejor_vecino)
        
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamano_lista_tabu:
            lista_tabu.pop(0)
    
    return mejor_solucion, mejor_valor

# Ejemplo de uso
mejor_solucion, mejor_valor = busqueda_tabu(num_iteraciones=100, tamano_lista_tabu=5)
print("Mejor solución encontrada:", mejor_solucion)
print("Mejor valor:", mejor_valor)

#El código para un algoritmo de búsqueda tabú puede ser bastante extenso y complejo, ya que implica la implementación de una heurística específica, la definición de estructuras de datos para gestionar la lista tabú y la lógica para explorar el espacio de búsqueda. 
