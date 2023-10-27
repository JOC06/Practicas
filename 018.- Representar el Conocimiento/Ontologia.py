# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:27:33 2023

@author: JOCELYNE
"""

class Concepto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = []

    def agregar_relacion(self, relacion, otro_concepto):
        self.relaciones.append((relacion, otro_concepto))

class Ontologia:
    def __init__(self):
        self.conceptos = {}

    def agregar_concepto(self, nombre):
        concepto = Concepto(nombre)
        self.conceptos[nombre] = concepto

    def agregar_relacion(self, nombre_concepto1, relacion, nombre_concepto2):
        concepto1 = self.conceptos.get(nombre_concepto1)
        concepto2 = self.conceptos.get(nombre_concepto2)
        if concepto1 and concepto2:
            concepto1.agregar_relacion(relacion, concepto2)

    def mostrar_ontologia(self):
        for nombre, concepto in self.conceptos.items():
            print(f"Concepto: {nombre}")
            for relacion, otro_concepto in concepto.relaciones:
                print(f"- {relacion}: {otro_concepto.nombre}")

# Crear una ontología
mi_ontologia = Ontologia()

# Agregar conceptos
mi_ontologia.agregar_concepto("Persona")
mi_ontologia.agregar_concepto("Lugar")
mi_ontologia.agregar_concepto("Ciudad")

# Agregar relaciones
mi_ontologia.agregar_relacion("Persona", "vive_en", "Lugar")
mi_ontologia.agregar_relacion("Lugar", "ubicado_en", "Ciudad")

# Mostrar la ontología
mi_ontologia.mostrar_ontologia()