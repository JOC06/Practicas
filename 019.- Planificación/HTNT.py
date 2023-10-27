# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:21:46 2023

@author: JOCELYNE
"""

class HTNTask:
    def __init__(self, name, task_type, preconditions=None, subtasks=None):
        self.name = name
        self.task_type = task_type
        self.preconditions = preconditions or []
        self.subtasks = subtasks or []

    def __str__(self):
        return self.name

class HTNPlanner:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.name] = task

    def plan(self, goal, state):
        if goal == state:
            return []
        for task in self.tasks.values():
            if task.task_type == "primitive" and task.name == goal:
                if all(subgoal in state for subgoal in task.preconditions):
                    return [task]
            elif task.task_type == "compound" and task.name == goal:
                if all(subtask in state for subtask in task.preconditions):
                    plan = []
                    for subtask in task.subtasks:
                        subplan = self.plan(subtask, state)
                        if subplan is None:
                            return None
                        plan.extend(subplan)
                    return plan
        return None

# Definir tareas compuestas (HTN operators) y primitivas
# En este ejemplo, definimos tareas para hacer una taza de té
boil_water = HTNTask("BoilWater", "primitive", ["KettleEmpty"])
make_tea = HTNTask("MakeTea", "compound", ["KettleBoiled", "TeaLeaves"])
drink_tea = HTNTask("DrinkTea", "primitive", ["TeaReady"])

# Crear un planificador HTN y agregar tareas
planner = HTNPlanner()
planner.add_task(boil_water)
planner.add_task(make_tea)
planner.add_task(drink_tea)

# Definir el objetivo y el estado inicial
goal_state = ["TeaReady"]
initial_state = ["KettleEmpty", "TeaLeaves"]

# Planificar
plan = planner.plan("MakeTea", initial_state)

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    for task in plan:
        print(task)
else:
    print("No se puede encontrar un plan.")