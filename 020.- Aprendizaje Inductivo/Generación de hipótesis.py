# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:59:08 2023

@author: JOCELYNE
"""

import pandas as pd

# Cargar datos de ventas y datos de clima desde archivos CSV (asegúrate de tener los archivos)
datos_ventas = pd.read_csv('datos_ventas.csv')
datos_clima = pd.read_csv('datos_clima.csv')

# Calcular la correlación entre las ventas y las condiciones climáticas (hipótesis inicial)
correlacion = datos_ventas['Ventas'].corr(datos_clima['Temperatura'])

# Generar una hipótesis en función de la correlación
if correlacion > 0.6:
    hipotesis = "Existe una correlación positiva fuerte entre la temperatura y las ventas."
elif correlacion < -0.6:
    hipotesis = "Existe una correlación negativa fuerte entre la temperatura y las ventas."
else:
    hipotesis = "No se observa una correlación fuerte entre la temperatura y las ventas."

print(hipotesis)
