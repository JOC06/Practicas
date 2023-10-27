# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:21:09 2023

@author: JOCELYNE
"""

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

# Crear un grafo RDF
g = Graph()

# Definir un espacio de nombres para nuestra ontología
my_ontology = Namespace("http://example.org/myontology#")

# Definir clases y propiedades
g.add((my_ontology.Person, RDF.type, RDFS.Class))
g.add((my_ontology.hasName, RDF.type, RDF.Property))
g.add((my_ontology.hasAge, RDF.type, RDF.Property))

# Agregar instancias
john = URIRef("http://example.org/john")
g.add((john, RDF.type, my_ontology.Person))
g.add((john, my_ontology.hasName, Literal("John")))
g.add((john, my_ontology.hasAge, Literal(30)))

# Serializar y mostrar el grafo
print(g.serialize(format="turtle").decode("utf-8"))
