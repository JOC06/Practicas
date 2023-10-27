# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:22:09 2023

@author: JOCELYNE
"""

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def __str__(self):
        return self.name

class Plan:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def __str__(self):
        return " -> ".join([str(action) for action in self.actions])

def order_partial_planning(actions, initial_state, goal_state):
    plan = Plan()
    while not is_subset(goal_state, initial_state):
        applicable_actions = [action for action in actions if is_subset(action.preconditions, initial_state)]
        if not applicable_actions:
            print("No se puede encontrar una solución.")
            return None
        chosen_action = applicable_actions[0]
        initial_state = apply_action(chosen_action, initial_state)
        plan.add_action(chosen_action)
    return plan

def is_subset(subset, superset):
    return all(item in superset for item in subset)

def apply_action(action, state):
    new_state = [s for s in state if s not in action.effects]
    new_state.extend(action.effects)
    return new_state

# Definir un problema de planificación de orden parcial
initial_state = ["A", "B"]
goal_state = ["C", "D"]
actions = [
    Action("Action1", ["A"], ["B"]),
    Action("Action2", ["B"], ["C"]),
    Action("Action3", ["A"], ["D"]),
    Action("Action4", ["D"], ["C"]),
]

# Resolver el problema de orden parcial
plan = order_partial_planning(actions, initial_state, goal_state)

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    print(plan)