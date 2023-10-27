# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:52:11 2023

@author: JOCELYNE
"""

class Evento:
    def __init__(self, nombre, fecha, participantes):
        self.nombre = nombre
        self.fecha = fecha
        self.participantes = participantes

# Ejemplo de creación de un evento
evento_reunion = Evento("Reunión de Equipo", "2023-11-01", ["Alice", "Bob", "Charlie"])

# Acceso a los atributos del evento
print(f"Evento: {evento_reunion.nombre}")
print(f"Fecha: {evento_reunion.fecha}")
print(f"Participantes: {', '.join(evento_reunion.participantes)}")


class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    
    def presentarse(self):
        print(f"¡Hola! Soy {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}.")

# Ejemplo de creación de un objeto mental para una persona
persona1 = Persona("Alice", 30, "Ingeniera")
persona2 = Persona("Bob", 35, "Doctor")

# Llamada al método de presentación
persona1.presentarse()
persona2.presentarse()
