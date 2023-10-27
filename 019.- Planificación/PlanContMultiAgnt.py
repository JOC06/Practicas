
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random

# Define un agente simple para la simulación
class AgenteSimple(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.valor = random.randint(0, 100)

    def step(self):
        # Ejemplo de comportamiento del agente
        self.valor += random.choice([-1, 1])
        self.interactuar(self.model.schedule.agents)
       
    def interactuar(self, otros_agentes):
    # En este ejemplo, los agentes interactúan con agentes cercanos.
        vecinos = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        
        for vecino in vecinos:
            vecino.valor += self.valor * 0.1  # Un vecino incrementa su valor en un 10% del valor de este agente    

# Define el modelo de la simulación
class ModeloSimulacion(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Crea agentes y los coloca en la grilla
        for i in range(self.num_agents):
            agente = AgenteSimple(i, self)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agente, (x, y))
            self.schedule.add(agente)

        # Agrega un colector de datos
        self.datacollector = DataCollector(agent_reporters={"Valor": "valor"})

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

# Crea y ejecuta la simulación
modelo = ModeloSimulacion(100, 10, 10)  # 100 agentes en una grilla de 10x10
for _ in range(100):  # Ejecuta la simulación durante 100 pasos de tiempo
    modelo.step()

# Accede a los datos recopilados
data = modelo.datacollector.get_agent_vars_dataframe()

# Imprime los datos de los agentes
print(data)
