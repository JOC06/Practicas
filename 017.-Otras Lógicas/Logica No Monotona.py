# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:31:33 2023

@author: JOCELYNE
"""

class Restaurante:
    def __init__(self):
        self.menu = []
        self.oferta_especial = None

    def agregar_plato_al_menu(self, plato):
        self.menu.append(plato)

    def establecer_oferta_especial(self, plato):
        self.oferta_especial = plato

    def realizar_pedido(self, plato):
        if plato in self.menu:
            pedido = f"Pedido: {plato}"
        elif self.oferta_especial is not None and plato == self.oferta_especial:
            pedido = f"Pedido (oferta especial): {plato}"
        else:
            pedido = f"El plato {plato} no está en el menú ni es la oferta especial."

        return pedido

# Crear un restaurante
mi_restaurante = Restaurante()

# Agregar platos al menú
mi_restaurante.agregar_plato_al_menu("sopa")
mi_restaurante.agregar_plato_al_menu("ensalada")

# Establecer una oferta especial
mi_restaurante.establecer_oferta_especial("pasta")

# Realizar pedidos
pedido1 = mi_restaurante.realizar_pedido("sopa")
pedido2 = mi_restaurante.realizar_pedido("pasta")
pedido3 = mi_restaurante.realizar_pedido("filete")

# Mostrar pedidos
print(pedido1)
print(pedido2)
print(pedido3)