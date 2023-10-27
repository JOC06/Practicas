class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class State:
    def __init__(self, predicates):
        self.predicates = predicates

def strips_planner(initial_state, goal_state, actions):
    plan = []

    while not state_satisfies_goal(initial_state, goal_state):
        applicable_actions = []

        for action in actions:
            if state_satisfies_preconditions(initial_state, action.preconditions):
                applicable_actions.append(action)

        if not applicable_actions:
            print("No plan found.")
            return None

        chosen_action = applicable_actions[0]

        initial_state = apply_action(initial_state, chosen_action)
        plan.append(chosen_action)

    return plan

def state_satisfies_preconditions(state, preconditions):
    for precondition in preconditions:
        if precondition not in state.predicates:
            return False
    return True

def state_satisfies_goal(state, goal_state):
    return state_satisfies_preconditions(state, goal_state.predicates)

def apply_action(state, action):
    new_state_predicates = set(state.predicates)
    new_state_predicates.difference_update(action.effects)
    new_state_predicates.update(action.preconditions)
    return State(new_state_predicates)

# Ejemplo de uso
if __name__ == "__main":
    # Define acciones
    action1 = Action("Action1", {"A"}, {"B"})
    action2 = Action("Action2", {"B"}, {"C"})

    # Define estados iniciales y de objetivo
    initial_state = State({"A"})
    goal_state = State({"C"})

    # Planificar
    plan = strips_planner(initial_state, goal_state, [action1, action2])

    if plan:
        print("Plan encontrado:")
        for action in plan:
            print(action.name)
    else:
        print("No se encontró un plan.")
