# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:14:53 2023

@author: JOCELYNE
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los valores de píxeles a un rango de 0 a 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Crear un modelo de red neuronal profunda
model = Sequential([
    Flatten(input_shape=(28, 28)),   # Aplanar las imágenes 28x28 a un vector de 784
    Dense(128, activation='relu'),    # Capa oculta con 128 neuronas y función de activación ReLU
    Dense(10, activation='softmax')   # Capa de salida con 10 neuronas para las 10 clases y función de activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo en el conjunto de prueba
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f'Exactitud en el conjunto de prueba: {test_accuracy}')