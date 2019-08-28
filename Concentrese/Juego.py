from Partida import Partida


# noinspection SpellCheckingInspection, PyPep8Naming
class Juego:
    CANTIDADPARTIDAS = 5
    totalPartidas = 0
    RUTAS = ["./data/entrada.txt", "./data/entrada2.txt", "./data/entrada3.txt"]

    def __init__(self):
        self.miPartida = list()
        self.contPartida = 0

    def cargarJuego(self, indice):
        br = open(self.RUTAS[indice], "r")

        if self.contPartida is self.CANTIDADPARTIDAS:
            self.miPartida.pop(0)
            self.miPartida.append(Partida(self.totalPartidas))
        else:
            self.miPartida.append(Partida(self.totalPartidas))
            self.contPartida += 1
        self.totalPartidas += 1

        cantFichas = int(br.readline().replace("\n", ""))

        for i in range(cantFichas):
            self.miPartida[self.contPartida - 1].crearFicha(br.readline().replace("\n", ""),
                                                            br.readline().replace("\n", ""))
        br.close()

    def imprimirTodo(self):
        return open("./data/salida.txt", "r").read()

    def reiniciarPartidad(self, i):
        self.miPartida[i].reiniciarFicha()

    def generarReporte(self):
        pw = open("./data/salida.txt", "w")

        for i in self.miPartida:
            pw.write(f"Para la partida numero {i.getNumeroPartida() + 1} el puntaje es: {i.getPuntaje()}\n")

        poss = 0
        cont = 0
        puntajeM = self.miPartida[0].getPuntaje()
        for i in self.miPartida:
            if puntajeM < i.getPuntaje():
                puntajeM = i.getPuntaje()
                poss = cont
            cont += 1

        pw.write(f"El mayor puntaje fue el de la partida {(self.miPartida[poss].getNumeroPartida() + 1)} "
                 f"con un puntaje de : {self.miPartida[poss].getPuntaje()}")
        pw.close()

    def validar(self, i, i1, i2):
        if self.miPartida[i].getMiFicha(i1).getNombre() == self.miPartida[i].getMiFicha(i2).getNombre():
            self.miPartida[i].subePuntaje()
            return True
        else:
            self.miPartida[i].bajaPuntaje()
            return False

    def getMiPartida(self, i):
        return self.miPartida[i]

    def setMiPartida(self, i, numPartida):
        self.miPartida[i].setNumPartida(numPartida)

    def getContPartidas(self):
        return self.contPartida

    def setContPartidas(self, contPartidas):
        self.contPartida = contPartidas

    def getCANTIDADPARTIDAS(self):
        return self.CANTIDADPARTIDAS

    def getTotalPartidas(self):
        return self.totalPartidas

    def setTotalPartidas(self, totalPartidas):
        self.totalPartidas = totalPartidas
