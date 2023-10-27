# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:28:53 2023

@author: JOCELYNE
"""

class Concepto:
    def __init__(self, nombre):
        self.nombre = nombre

class Categoria(Concepto):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel
        self.subcategorias = []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    def mostrar(self):
        indentacion = "  " * self.nivel
        print(f"{indentacion}{self.nombre}")
        for subcategoria in self.subcategorias:
            subcategoria.mostrar()

# Crear una taxonomía
raiz = Categoria("Reino Animal", nivel=0)
vertebrados = Categoria("Vertebrados", nivel=1)
invertebrados = Categoria("Invertebrados", nivel=1)
mamiferos = Categoria("Mamíferos", nivel=2)
aves = Categoria("Aves", nivel=2)
peces = Categoria("Peces", nivel=2)

raiz.agregar_subcategoria(vertebrados)
raiz.agregar_subcategoria(invertebrados)

vertebrados.agregar_subcategoria(mamiferos)
vertebrados.agregar_subcategoria(aves)
vertebrados.agregar_subcategoria(peces)

# Mostrar la taxonomía
raiz.mostrar()