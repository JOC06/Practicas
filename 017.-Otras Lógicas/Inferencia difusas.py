
#La inferencia difusa es el proceso de aplicar reglas difusas a los conjuntos difusos para obtener una salida difusa
#realizar inferencia difusa utilizando la biblioteca scikit-fuzzy. En este ejemplo, se utilizará el mismo sistema que
# definimos anteriormente (temperatura, humedad y velocidad del ventilador):

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear universos de discurso
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir conjuntos difusos para temperatura, humedad y velocidad del ventilador (como en el ejemplo anterior)

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fría'] & humedad['seca'], velocidad_ventilador['alta'])
regla2 = ctrl.Rule(temperatura['fría'] & humedad['normal'], velocidad_ventilador['media'])
regla3 = ctrl.Rule(temperatura['fría'] & humedad['húmeda'], velocidad_ventilador['baja'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear el simulador
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Ingresar valores de temperatura y humedad
simulador.input['temperatura'] = 30
simulador.input['humedad'] = 60

# Realizar la inferencia
simulador.compute()

# Obtener el resultado
print("Velocidad del ventilador:", simulador.output['velocidad_ventilador'])

# Visualizar la salida difusa
velocidad_ventilador.view(sim=simulador)

#Este código utiliza las reglas difusas definidas para calcular la velocidad del ventilador basada en los valores de temperatura y humedad ingresados. 
#Puedes ajustar los valores de temperatura y humedad para observar cómo cambia la velocidad del ventilador de acuerdo con las reglas difusas definidas.

