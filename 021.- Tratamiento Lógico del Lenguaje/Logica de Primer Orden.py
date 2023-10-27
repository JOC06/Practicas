# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:03:00 2023

@author: JOCELYNE
"""

class Fact:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def __repr__(self):
        return f"{self.name}({', '.join(self.parameters)})"


class KnowledgeBase:
    def __init__(self):
        self.facts = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def check_fact(self, fact):
        for f in self.facts:
            if f.name == fact.name and len(f.parameters) == len(fact.parameters):
                for p1, p2 in zip(f.parameters, fact.parameters):
                    if p1 != p2:
                        break
                else:
                    return True
        return False

    def query(self, query):
        return [f for f in self.facts if f.name == query.name]


kb = KnowledgeBase()

kb.add_fact(Fact("has_pet", ["alice", "dog"]))
kb.add_fact(Fact("has_pet", ["bob", "cat"]))
kb.add_fact(Fact("has_pet", ["charlie", "hamster"]))

query = Fact("has_pet", ["bob", "cat"])
print(f"{query} is {'in' if kb.check_fact(query) else 'not in'} the knowledge base.")

results = kb.query(Fact("has_pet", ["charlie", ""]))
print(f"Results for the query {Fact('has_pet', ['charlie', ''])}:")
for result in results:
    print(f" - {result}")