# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:09:58 2023

@author: JOCELYNE
"""

import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada y sus salidas correspondientes para XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Inicialización de pesos y sesgos de forma aleatoria
np.random.seed(1)
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

weights_input_hidden = 2 * np.random.random((input_neurons, hidden_neurons)) - 1
bias_hidden = np.random.rand(1, hidden_neurons)

weights_hidden_output = 2 * np.random.random((hidden_neurons, output_neurons)) - 1
bias_output = np.random.rand(1, output_neurons)

learning_rate = 0.1
epochs = 10000

# Entrenamiento de la red
for _ in range(epochs):
    # Capa de entrada a capa oculta
    input_hidden = np.dot(X, weights_input_hidden) + bias_hidden
    output_hidden = sigmoid(input_hidden)

    # Capa oculta a capa de salida
    input_output = np.dot(output_hidden, weights_hidden_output) + bias_output
    output_output = sigmoid(input_output)

    # Cálculo del error
    error = y - output_output

    # Retropropagación (backpropagation)
    d_output = error * sigmoid_derivative(output_output)
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(output_hidden)

    # Actualización de pesos y sesgos
    weights_hidden_output += output_hidden.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Impresión de la entrada y la salida una vez entrenada
print("Tu entrada fue:")
print("A  B  Y")
for i in range(len(X)):
    hidden_layer_input = np.dot(X[i], weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = sigmoid(output_layer_input)
    binary_output = round(output_layer_output[0][0])
    print(f"{X[i][0]}  {X[i][1]}  {binary_output}")