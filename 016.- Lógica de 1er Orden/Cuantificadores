import sympy

# Definimos las variables y el dominio
x, y = sympy.symbols('x y')
dominio = sympy.Integers

# Expresión cuantificada: ∀x ∈ Z, ∃y ∈ Z, y = x^2
expresion = sympy.ForAll(x, sympy.Implies(sympy.And(x >= -10, x <= 10), sympy.Exists(y, y == x**2)), domain=dominio)

# Evaluamos la expresión
resultado = sympy.ask(expresion)

if resultado is True:
    print("La expresión es verdadera.")
else:
    print("La expresión es falsa.")
