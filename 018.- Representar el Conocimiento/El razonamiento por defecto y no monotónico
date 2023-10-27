class SistemaRazonamientoDefecto:
    def __init__(self):
        self.hechos = {"Tweety": {"plumas", "canta"}}

    def inferir(self, entidad):
        if "plumas" in self.hechos[entidad] and "canta" in self.hechos[entidad]:
            return "Es probable que {} sea un canario.".format(entidad)
        else:
            return "No se puede determinar si {} es un canario.".format(entidad)

# Ejemplo de uso del sistema de razonamiento por defecto
sistema = SistemaRazonamientoDefecto()
entidad = "Tweety"
resultado = sistema.inferir(entidad)
print(resultado)
