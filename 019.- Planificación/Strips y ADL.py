# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:22:34 2023

@author: JOCELYNE
"""

class State:
    def __init__(self, predicates):
        self.predicates = predicates

    def __str__(self):
        return str(self.predicates)

class Action:
    def __init__(self, name, preconditions, add_effects, delete_effects):
        self.name = name
        self.preconditions = preconditions
        self.add_effects = add_effects
        self.delete_effects = delete_effects

    def __str__(self):
        return self.name

def strips_adl(problem, initial_state, goal_state):
    plan = []
    while not is_subset(goal_state.predicates, initial_state.predicates):
        applicable_actions = [action for action in problem if is_subset(action.preconditions, initial_state.predicates)]
        if not applicable_actions:
            print("No se puede encontrar una solución.")
            return None
        chosen_action = applicable_actions[0]
        initial_state = apply_action(chosen_action, initial_state)
        plan.append(chosen_action)
    return plan

def is_subset(subset, superset):
    return all(item in superset for item in subset)

def apply_action(action, state):
    new_predicates = [p for p in state.predicates if p not in action.delete_effects]
    new_predicates.extend(action.add_effects)
    return State(new_predicates)

# Definir un problema de planificación simple con ADL
initial_state = State(["At(Robot, A)"])
goal_state = State(["At(Robot, C)"])
actions = [
    Action("Move", ["At(Robot, X)", "CanMove(Robot, X, Y)"], ["At(Robot, Y)"], ["At(Robot, X)"]),
    Action("Drive", ["At(Robot, Y)", "CanDrive(Robot, Y, Z)"], ["At(Robot, Z)"], ["At(Robot, Y)"]),
]

# Resolver el problema
plan = strips_adl(actions, initial_state, goal_state)

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action)