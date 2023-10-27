
def planificacion_orden_parcial(tareas):
    resultado = []  # Lista para almacenar el orden de las tareas planificadas
    
    def buscar_siguiente_tarea():
        for tarea in tareas:
            # Si la tarea no está en el resultado y todas sus tareas precedentes han sido completadas, la agregamos
            if tarea not in resultado and all(predecesora in resultado for predecesora in tarea[1]):
                return tarea
        return None
    
    while len(resultado) < len(tareas):
        siguiente_tarea = buscar_siguiente_tarea()
        if siguiente_tarea is None:
            print("No se puede encontrar un orden parcial válido. Puede haber ciclos en las dependencias.")
            break
        resultado.append(siguiente_tarea[0])

    return resultado

# Ejemplo de uso
tareas = [
    ("Tarea A", []),
    ("Tarea B", ["Tarea A"]),
    ("Tarea C", ["Tarea A"]),
    ("Tarea D", ["Tarea B", "Tarea C"]),
]

orden_parcial = planificacion_orden_parcial(tareas)
if orden_parcial:
    print("Orden parcial de tareas:")
    for tarea in orden_parcial:
        print(tarea)