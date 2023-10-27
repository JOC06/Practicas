# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:56:45 2023

@author: JOCELYNE
"""

import nltk
from nltk.grammar import Nonterminal, Production

# Define una gramática probabilística
producciones = [
    # S -> NP VP
    Production(Nonterminal('S'), [Nonterminal('NP'), Nonterminal('VP')]),
    # NP -> Det N
    Production(Nonterminal('NP'), [Nonterminal('Det'), Nonterminal('N')]),
    # NP -> N
    Production(Nonterminal('NP'), [Nonterminal('N')]),
    # VP -> V NP
    Production(Nonterminal('VP'), [Nonterminal('V'), Nonterminal('NP')]),
    # VP -> V
    Production(Nonterminal('VP'), [Nonterminal('V')]),
    # Det -> 'el'
    Production(Nonterminal('Det'), ['el']),
    # Det -> 'un'
    Production(Nonterminal('Det'), ['un']),
    # N -> 'perro'
    Production(Nonterminal('N'), ['perro']),
    # N -> 'gato'
    Production(Nonterminal('N'), ['gato']),
    # N -> 'ratón'
    Production(Nonterminal('N'), ['ratón']),
    # V -> 'persigue'
    Production(Nonterminal('V'), ['persigue']),
    # V -> 'captura'
    Production(Nonterminal('V'), ['captura'])
]

# Crear una gramática probabilística
pcfg = nltk.grammar.induce_pcfg(Nonterminal('S'), producciones)

# Crear un parser para la gramática probabilística
parser = nltk.ViterbiParser(pcfg)

# Generar oraciones basadas en la gramática
for tree in parser.parse("el perro persigue el gato".split()):
    print(tree)