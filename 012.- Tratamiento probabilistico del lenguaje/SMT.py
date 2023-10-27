# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:58:55 2023

@author: JOCELYNE
"""

import numpy as np

# Oraciones de ejemplo en el idioma de origen y destino
source_sentences = ["I am a student", "He is a teacher", "She is a doctor"]
target_sentences = ["Je suis étudiant", "Il est professeur", "Elle est médecin"]

# Tokenización de las oraciones
source_tokens = [sentence.split() for sentence in source_sentences]
target_tokens = [sentence.split() for sentence in target_sentences]

# Construcción del vocabulario de origen y destino
source_vocab = set(word for sentence in source_tokens for word in sentence)
target_vocab = set(word for sentence in target_tokens for word in sentence)

# Inicialización de las probabilidades de alineación uniformemente
alignment_probs = np.ones((len(source_tokens), len(target_tokens))) / len(target_tokens)

# Número de iteraciones de entrenamiento (ajuste)
num_iterations = 10

# Entrenamiento del modelo IBM Model 1
for iteration in range(num_iterations):
    # Paso de Expectation-Maximization (E-step)
    e_counts = np.zeros((len(source_tokens), len(target_tokens)))
    for i, source_sentence in enumerate(source_tokens):
        for j, target_sentence in enumerate(target_tokens):
            total_prob = sum(alignment_probs[i, j] for j in range(len(target_sentence)))
            for source_word in source_sentence:
                for k, target_word in enumerate(target_sentence):
                    e_counts[i, j] += alignment_probs[i, j] * (source_word == source_sentence) / total_prob

    # Paso de Maximization (M-step)
    f_counts = np.sum(e_counts, axis=1)
    for i, source_sentence in enumerate(source_tokens):
        for j, target_sentence in enumerate(target_tokens):
            alignment_probs[i, j] = e_counts[i, j] / f_counts[i]

# Traducción de una nueva oración
new_source_sentence = "I am a student"
new_source_tokens = new_source_sentence.split()
new_target_tokens = []

for source_token in new_source_tokens:
    max_prob = 0
    max_prob_index = 0
    for j, target_sentence in enumerate(target_tokens):
        for k, target_token in enumerate(target_sentence):
            if alignment_probs[j, k] > max_prob and source_token == source_tokens[j][k]:
                max_prob = alignment_probs[j, k]
                max_prob_index = k
    new_target_tokens.append(target_tokens[max_prob_index][max_prob_index])

new_target_sentence = " ".join(new_target_tokens)
print(f"Fuente: {new_source_sentence}")
print(f"Destino: {new_target_sentence}")