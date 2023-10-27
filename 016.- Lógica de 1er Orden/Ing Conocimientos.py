# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:45:12 2023

@author: JOCELYNE
"""

base_de_datos_peliculas = {
    "Pelicula1": ["Aventura", "Acción", "Ciencia Ficción"],
    "Pelicula2": ["Comedia", "Romance"],
    "Pelicula3": ["Drama", "Romance"],
    # ... Más películas ...
}

preferencias_usuario = {
    "Aventura": 5,
    "Acción": 4,
    "Romance": 3,
    # ... Más preferencias ...
}

# Razonamiento: Recomendar películas en función de las preferencias del usuario.

def recomendar_peliculas(base_de_datos, preferencias, umbral=3):
    recomendaciones = []
    for pelicula, generos in base_de_datos.items():
        puntaje = 0
        for genero in generos:
            if genero in preferencias:
                puntaje += preferencias[genero]
        if puntaje >= umbral:
            recomendaciones.append(pelicula)
    return recomendaciones

# Llamada a la función para obtener recomendaciones basadas en preferencias del usuario
recomendaciones = recomendar_peliculas(base_de_datos_peliculas, preferencias_usuario)

# Resultados: Imprimir las películas recomendadas.
if recomendaciones:
    print("Películas recomendadas:")
    for pelicula in recomendaciones:
        print(pelicula)
else:
    print("No se encontraron películas recomendadas.")

# En este código:
# - La base de datos de películas y preferencias del usuario representa el conocimiento del sistema.
# - El razonamiento se realiza al calcular un puntaje para cada película en función de las preferencias del usuario.
# - Las recomendaciones se generan a partir del razonamiento basado en las preferencias del usuario.