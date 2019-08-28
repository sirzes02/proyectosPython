# noinspection SpellCheckingInspection
class Tarea:

    def __init__(self, nombre, estado, prioridad):
        self.nombre = nombre
        self.estado = estado
        self.prioridad = prioridad

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPrioridad(self):
        return self.prioridad

    def setPrioridad(self, prioridad):
        self.prioridad = prioridad
