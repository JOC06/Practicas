# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:26:34 2023

@author: JOCELYNE
"""

import random

# Definimos un diccionario de preguntas y respuestas
dialogo = {
    "Hola": "¡Hola! ¿En qué puedo ayudarte?",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿Cuál es tu nombre?": "Soy un asistente virtual.",
    "¿Qué tiempo hace hoy?": "Lo siento, no tengo acceso a información en tiempo real.",
    "Adiós": "Hasta luego. ¡Ten un buen día!",
}

# Función para procesar preguntas y generar respuestas
def responder_pregunta(pregunta):
    pregunta = pregunta.lower()
    respuesta = dialogo.get(pregunta, "Lo siento, no entiendo la pregunta.")
    return respuesta

# Loop de diálogo
while True:
    pregunta = input("Tú: ")
    if pregunta.lower() == "adiós":
        print("Asistente: Hasta luego. ¡Ten un buen día!")
        break
    respuesta = responder_pregunta(pregunta)
    print("Asistente:", respuesta)
