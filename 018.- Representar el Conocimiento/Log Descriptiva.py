# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:26:17 2023

 JOCELYNE
"""

# Definir una red semántica simple de relaciones entre personas
red_semantica = {
    "Juan": {"nombre": "Juan Pérez", "edad": 25, "profesion": "estudiante"},
    "María": {"nombre": "María Rodríguez", "edad": 35, "profesion": "profesor"},
    "relaciones": [
        {"persona1": "Juan", "persona2": "María", "parentesco": "amigo"},
        {"persona1": "María", "persona2": "Juan", "parentesco": "amigo"},
    ]
}

# Definir reglas para inferir propiedades
def regla_tiene_nombre(persona, red):
    return "nombre" in red[persona]

def regla_tiene_edad(persona, red):
    return "edad" in red[persona]

def regla_tiene_profesion(persona, red):
    return "profesion" in red[persona]

# Aplicar reglas para inferir propiedades
for persona in red_semantica:
    if regla_tiene_nombre(persona, red_semantica):
        print(f"{persona} tiene nombre: {red_semantica[persona]['nombre']}")
    if regla_tiene_edad(persona, red_semantica):
        print(f"{persona} tiene edad: {red_semantica[persona]['edad']}")
    if regla_tiene_profesion(persona, red_semantica):
        print(f"{persona} tiene profesión: {red_semantica[persona]['profesion']}")

# Mostrar relaciones semánticas
for relacion in red_semantica["relaciones"]:
    print(f"{relacion['persona1']} y {relacion['persona2']} son {relacion['parentesco']}s.")