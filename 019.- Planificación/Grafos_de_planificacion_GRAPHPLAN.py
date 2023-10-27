
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class Problem:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

def is_subset(subset, superset):
    return all(item in superset for item in subset)

def apply_action(state, action):
    new_state = state.copy()
    for effect in action.effects:
        new_state.add(effect)
    return new_state

def graphplan(problem):
    # Inicializa el grafo de planificación
    level = 0
    states = {problem.initial_state}
    graph = {level: {'actions': set(), 'states': states}}

    while level < 100:  # Límite para evitar bucles infinitos
        actions = set()
        states = set()
        for action in problem.actions:
            if all(is_subset(precond, states) for precond in action.preconditions):
                actions.add(action)
                states.update(action.effects)

        if problem.goal_state in states:
            # Se ha alcanzado el objetivo
            plan = []
            for lv in range(level, -1, -1):
                state = problem.goal_state
                level_actions = graph[lv]['actions']
                for action in level_actions:
                    if all(is_subset(precond, state) for precond in action.preconditions):
                        plan.append(action)
                        state = apply_action(state, action)
            return plan[::-1]  # Invertir el plan para obtener la secuencia correcta

        level += 1
        graph[level] = {'actions': actions, 'states': states}

    return None  # No se ha encontrado una solución

# Ejemplo de uso
initial_state = {'A', 'B'}
goal_state = {'C'}
actions = [
    Action('Action1', [], ['A']),
    Action('Action2', ['A'], ['B']),
    Action('Action3', ['B'], ['C']),
]

problem = Problem(initial_state, goal_state, actions)
plan = graphplan(problem)

if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action.name)
else:
    print("No se encontró un plan para alcanzar el objetivo.")
