from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

# Definir una clase de agente para la vigilancia y replanificación
class AgenteVigilante(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tarea_completada = False

    def step(self):
        if not self.tarea_completada:
            # Simula una tarea que lleva tiempo
            if random.random() < 0.2:
                self.tarea_completada = True
                print(f"Agente {self.unique_id}: Tarea completada")
        else:
            # Replanificación si es necesario
            if random.random() < 0.1:
                self.tarea_completada = False
                print(f"Agente {self.unique_id}: Replanificando")

# Define el modelo de la simulación
class ModeloSimulacion(Model):
    def __init__(self, N, width, height):
        self.num_agentes = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Crea agentes de vigilancia
        for i in range(self.num_agentes):
            agente = AgenteVigilante(i, self)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agente, (x, y))
            self.schedule.add(agente)

    def step(self):
        self.schedule.step()

# Crea y ejecuta la simulación
modelo = ModeloSimulacion(10, 5, 5)  # 10 agentes en una grilla de 5x5
for _ in range(100):
    modelo.step()
