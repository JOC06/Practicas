# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:58:00 2023

@author: PC
"""

import pandas as pd

# Cargar el conjunto de datos desde un archivo CSV
df = pd.read_csv('datos.csv')

# Mostrar las primeras filas del conjunto de datos
print("Primeras 5 filas del conjunto de datos:")
print(df.head())

# Resumen estadístico del conjunto de datos
print("\nResumen estadístico del conjunto de datos:")
print(df.describe())

# Información sobre las columnas y tipos de datos
print("\nInformación de las columnas y tipos de datos:")
print(df.info())

# Filtrar y seleccionar datos
print("\nSelección de filas que cumplen una condición:")
filtro = df['Columna1'] > 50
datos_filtrados = df[filtro]
print(datos_filtrados)

# Agrupar datos y calcular estadísticas
print("\nAgrupación de datos por una columna y cálculo de la media:")
grupo = df.groupby('Columna2')
media_por_grupo = grupo['Columna3'].mean()
print(media_por_grupo)

# Visualización básica (requiere matplotlib)
import matplotlib.pyplot as plt

# Gráfico de barras
df['Columna4'].value_counts().plot(kind='bar')
plt.title('Frecuencia de valores en Columna4')
plt.show()
