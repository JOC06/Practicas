from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

# Define una clase de tarea
class Tarea:
    def __init__(self, nombre, nivel, duracion):
        self.nombre = nombre
        self.nivel = nivel
        self.duracion = duracion

# Define una clase de agente para ejecutar tareas
class AgenteEjecutor(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tarea_actual = None

    def step(self):
        if self.tarea_actual is None:
            self.tarea_actual = self.seleccionar_tarea()
            if self.tarea_actual is not None:
                print(f"Agente {self.unique_id}: Comenzando tarea '{self.tarea_actual.nombre}'")

        if self.tarea_actual is not None:
            self.tarea_actual.duracion -= 1
            if self.tarea_actual.duracion == 0:
                print(f"Agente {self.unique_id}: Completada tarea '{self.tarea_actual.nombre}'")
                self.tarea_actual = None

    def seleccionar_tarea(self):
        tareas_disponibles = self.model.tareas_disponibles[self.unique_id]
        if tareas_disponibles:
            return tareas_disponibles.pop(0)
        else:
            return None

# Define el modelo de la simulación
class ModeloSimulacion(Model):
    def __init__(self, num_agentes, num_tareas):
        self.num_agentes = num_agentes
        self.num_tareas = num_tareas
        self.schedule = RandomActivation(self)

        # Crea agentes ejecutores
        for i in range(self.num_agentes):
            agente = AgenteEjecutor(i, self)
            self.schedule.add(agente)

        # Crea tareas jerárquicas
        self.tareas = []
        for i in range(self.num_tareas):
            nombre = f"Tarea-{i}"
            nivel = random.randint(1, 3)  # Nivel jerárquico (1, 2, o 3)
            duracion = random.randint(1, 5)  # Duración aleatoria
            tarea = Tarea(nombre, nivel, duracion)
            self.tareas.append(tarea)

        # Organiza tareas por nivel jerárquico
        self.tareas_por_nivel = {}
        for tarea in self.tareas:
            if tarea.nivel not in self.tareas_por_nivel:
                self.tareas_por_nivel[tarea.nivel] = []
            self.tareas_por_nivel[tarea.nivel].append(tarea)

        # Inicializa las tareas disponibles para cada agente
        self.tareas_disponibles = {i: [] for i in range(self.num_agentes)}
        for nivel in range(1, 4):
            if nivel in self.tareas_por_nivel:
                tareas_nivel = self.tareas_por_nivel[nivel]
                random.shuffle(tareas_nivel)
                for i in range(self.num_agentes):
                    if i < len(tareas_nivel):
                        self.tareas_disponibles[i].append(tareas_nivel[i])

    def step(self):
        self.schedule.step()

# Crea y ejecuta la simulación
modelo = ModeloSimulacion(5, 15)  # 5 agentes y 15 tareas
for _ in range(20):  # Ejecutar la simulación durante 20 pasos de tiempo
    modelo.step()
