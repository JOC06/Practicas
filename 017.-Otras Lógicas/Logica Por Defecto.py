# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:31:48 2023

@author: JOCELYNE
"""

class SistemaDePermisos:
    def __init__(self):
        self.reglas_generales = {}
        self.excepciones = {}

    def establecer_regla_general(self, usuario, accion):
        self.reglas_generales[usuario] = accion

    def establecer_excepcion(self, usuario, accion):
        self.excepciones[usuario] = accion

    def verificar_permiso(self, usuario):
        if usuario in self.excepciones:
            permiso = self.excepciones[usuario]
        elif usuario in self.reglas_generales:
            permiso = self.reglas_generales[usuario]
        else:
            permiso = "Sin permiso (por defecto)"

        return f"Usuario {usuario}: {permiso}"

# Crear un sistema de permisos
sistema_permisos = SistemaDePermisos()

# Establecer reglas generales
sistema_permisos.establecer_regla_general("usuario1", "lectura")
sistema_permisos.establecer_regla_general("usuario2", "escritura")

# Establecer excepciones
sistema_permisos.establecer_excepcion("usuario2", "sin acceso")

# Verificar permisos
permiso_usuario1 = sistema_permisos.verificar_permiso("usuario1")
permiso_usuario2 = sistema_permisos.verificar_permiso("usuario2")
permiso_usuario3 = sistema_permisos.verificar_permiso("usuario3")

# Mostrar permisos
print(permiso_usuario1)
print(permiso_usuario2)
print(permiso_usuario3)