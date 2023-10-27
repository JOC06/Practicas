# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:04:13 2023

@author: User
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Descarga recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')

def search_policy(text, policy_keywords):
    # Tokeniza el texto en palabras
    words = word_tokenize(text)

    # Obtiene palabras de detención (stop words)
    stop_words = set(stopwords.words('english'))

    # Filtra las palabras de detención
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Busca las palabras clave de la política en el texto
    found_keywords = [keyword for keyword in policy_keywords if keyword in words]

    return found_keywords

# Ejemplo de texto en el que buscar la política
sample_text = "Este es un ejemplo de un texto en el que buscamos una política. La política se refiere a las normas y reglas que rigen nuestra organización."

# Palabras clave de política que deseas buscar
policy_keywords = ["política", "normas", "reglas", "organización"]

# Realiza la búsqueda de política en el texto
found_keywords = search_policy(sample_text, policy_keywords)

if found_keywords:
    print("Se encontraron las siguientes palabras clave de política:")
    for keyword in found_keywords:
        print(keyword)
else:
    print("No se encontraron palabras clave de política en el texto.")
#Este código buscará las palabras clave de política en un texto dado. Puedes ajustar las palabras clave de política según tus necesidades y aplicar este código a tus propios documentos o textos. Asegúrate de proporcionar un texto real en lugar de sample_text para que la búsqueda de política sea efectiva.