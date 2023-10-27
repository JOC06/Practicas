# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:30:55 2023

@author: JOCELYNE
"""

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.va_a_la_escuela = False

    def ir_a_la_escuela(self):
        self.va_a_la_escuela = True

    def no_ir_a_la_escuela(self):
        self.va_a_la_escuela = False

    def saber_si_va_a_la_escuela(self):
        if self.va_a_la_escuela:
            return f"{self.nombre} va a la escuela."
        else:
            return f"{self.nombre} no va a la escuela."

# Crear un estudiante
estudiante1 = Estudiante("Juan")

# Utilizar la lógica modal para tomar una decisión
# En este ejemplo, el estudiante irá a la escuela si es un día de semana (de lunes a viernes)
dia_de_la_semana = True

if dia_de_la_semana:
    estudiante1.ir_a_la_escuela()
else:
    estudiante1.no_ir_a_la_escuela()

# Preguntar si el estudiante va a la escuela
print(estudiante1.saber_si_va_a_la_escuela())