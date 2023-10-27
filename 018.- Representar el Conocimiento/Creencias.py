# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:23:18 2023

@author: JOCELYNE
"""

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.creencias = {}

    def agregar_creencia(self, concepto, valor):
        self.creencias[concepto] = valor

    def obtener_creencia(self, concepto):
        return self.creencias.get(concepto, "No se ha encontrado la creencia.")

    def mostrar_creencias(self):
        print(f"Creencias del agente {self.nombre}:")
        for concepto, valor in self.creencias.items():
            print(f"- {concepto}: {valor}")

# Crear un agente y establecer sus creencias
agente1 = Agente("Agente1")
agente1.agregar_creencia("Lugar de nacimiento", "Ciudad A")
agente1.agregar_creencia("Idioma principal", "Español")

# Mostrar las creencias del agente
agente1.mostrar_creencias()

# Consultar una creencia específica
lugar_de_nacimiento = agente1.obtener_creencia("Lugar de nacimiento")
print("Lugar de nacimiento:", lugar_de_nacimiento)

# Actualizar una creencia
agente1.agregar_creencia("Lugar de nacimiento", "Ciudad B")
nuevo_lugar_de_nacimiento = agente1.obtener_creencia("Lugar de nacimiento")
print("Nuevo lugar de nacimiento:", nuevo_lugar_de_nacimiento)