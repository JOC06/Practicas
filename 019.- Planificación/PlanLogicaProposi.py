import pycosat

# Define variables proposicionales
variables = {
    'A': 1,
    'B': 2,
    'C': 3,
    # ... Más variables ...
}

# Define cláusulas lógicas
clauses = [
    [-variables['A']], [variables['B']], [-variables['C']],
    # ... Más cláusulas ...
]

# Resuelve el problema SAT
solution = pycosat.solve(clauses)

# Interpreta la solución como un plan
if solution is not None:
    plan = [var for var in solution if var > 0]
    print("Plan encontrado:", plan)
else:
    print("No se encontró solución.")
