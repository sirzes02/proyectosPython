# noinspection SpellCheckingInspection
class Ficha:

    def __init__(self, dirImagen, nombre):
        self.dirImagen = dirImagen
        self.nombre = nombre

    def getDirImagen(self):
        return self.dirImagen

    def setDirImagen(self, dirImagen):
        self.dirImagen = dirImagen

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
