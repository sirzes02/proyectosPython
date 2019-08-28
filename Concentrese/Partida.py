import random

from Ficha import Ficha


# noinspection SpellCheckingInspection, PyPep8Naming
class Partida:
    PUNTAJEINICIAL = 0
    miFicha = []

    def __init__(self, numPartida):
        self.intento = 0
        self.puntaje = self.PUNTAJEINICIAL
        self.numPartida = numPartida
        self.cantFichas = 0
        self.miFicha = list()
        self.elementosM = list()

    def crearFicha(self, dirImagen, nombre):
        self.miFicha.append(Ficha(dirImagen, nombre))
        self.cantFichas += 1

    def reiniciarFicha(self):
        random.shuffle(self.miFicha)

    def getMiFicha(self, i):
        return self.miFicha[i]

    def setLaFicha(self, dirImagen, nombre, i):
        self.miFicha[i].setDirImagen(dirImagen)
        self.miFicha[i].setNombre(nombre)

    def subePuntaje(self):
        self.puntaje += 20

    def bajaPuntaje(self):
        self.puntaje -= 5

    def intento(self):
        self.puntaje -= 0

    def getNumeroPartida(self):
        return self.numPartida

    def setNumPartida(self, numPartida):
        self.numPartida = numPartida

    def getIntento(self):
        return self.intento

    def setIntento(self, intento):
        self.intento = intento

    def getPuntaje(self):
        return self.puntaje

    def setPuntaje(self, puntaje):
        self.puntaje = puntaje

    def getPUNTAJEINICIAL(self):
        return self.PUNTAJEINICIAL
