# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:13:37 2023

@author: JOCELYNE
"""

import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

nltk.download("movie_reviews")

# Obtén las revisiones de películas y etiquetas
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Mezcla los documentos
import random
random.shuffle(documents)

# Define una función para extraer características de un documento
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Obtén las palabras más frecuentes en las documentos
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:2000]

# Crea conjuntos de entrenamiento y prueba
featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[:1500], featuresets[1500:]

# Entrena un clasificador de Bayes ingenuo
classifier = NaiveBayesClassifier.train(train_set)

# Evalúa el clasificador
print("Exactitud del clasificador:", accuracy(classifier, test_set))

# Ejemplo de clasificación
text_to_classify = "This movie was great!"
features = document_features(text_to_classify.split())
result = classifier.classify(features)
print("Clasificación:", result)