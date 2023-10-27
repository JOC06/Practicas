from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

# Definir una clase de agente para la planificación condicional
class AgentePlanificador(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.objetivo = (random.randint(0, 4), random.randint(0, 4))

    def step(self):
        if self.pos == self.objetivo:
            print(f"Agente {self.unique_id}: He alcanzado mi objetivo en {self.pos}")
        else:
            siguiente_paso = self.planificar_siguiente_paso()
            self.model.grid.move_agent(self, siguiente_paso)

    def planificar_siguiente_paso(self):
        x, y = self.pos
        objetivo_x, objetivo_y = self.objetivo

        if x < objetivo_x:
            return (x + 1, y)
        elif x > objetivo_x:
            return (x - 1, y)
        elif y < objetivo_y:
            return (x, y + 1)
        elif y > objetivo_y:
            return (x, y - 1)
        else:
            return (x, y)

# Define el modelo de la simulación
class ModeloSimulacion(Model):
    def __init__(self, N, width, height):
        self.num_agentes = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Crea agentes planificadores
        for i in range(self.num_agentes):
            agente = AgentePlanificador(i, self)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agente, (x, y))
            self.schedule.add(agente)

    def step(self):
        self.schedule.step()

# Crea y ejecuta la simulación
modelo = ModeloSimulacion(5, 5, 5)  # 5 agentes en una cuadrícula de 5x5
for _ in range(10):  # Ejecutar la simulación durante 10 pasos de tiempo
    modelo.step()
