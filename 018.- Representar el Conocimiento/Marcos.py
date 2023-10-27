# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:26:39 2023

@author: JOCELYNE
"""

class Marco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = {}

    def agregar_propiedad(self, nombre_propiedad, valor):
        self.propiedades[nombre_propiedad] = valor

    def mostrar(self):
        print(f"Marco: {self.nombre}")
        for nombre_propiedad, valor in self.propiedades.items():
            print(f"- {nombre_propiedad}: {valor}")

# Crear un marco para representar una persona
persona = Marco("Persona")
persona.agregar_propiedad("Nombre", "Juan")
persona.agregar_propiedad("Edad", 30)
persona.agregar_propiedad("Género", "Masculino")

# Crear un marco para representar un evento
evento = Marco("Evento")
evento.agregar_propiedad("Nombre", "Fiesta de Cumpleaños")
evento.agregar_propiedad("Lugar", "Casa de Juan")
evento.agregar_propiedad("Fecha", "10 de abril")

# Mostrar la representación de los marcos
persona.mostrar()
evento.mostrar()