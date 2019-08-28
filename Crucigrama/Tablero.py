from Letra import Letra


# noinspection SpellCheckingInspection,PyPep8Naming
class Tablero:

    def __init__(self):
        self.miLetra = list()
        self.copia = list()
        self.palabras = list()
        self.cargarDatos()

    def cargarDatos(self):
        br = open("./data/data.txt", "r")
        cantPalabras = br.readline()

        for i in range(int(cantPalabras)):
            self.palabras.append(br.readline().replace("\n", ""))

        for i in br:
            self.miLetra.append([])
            self.copia.append([])
            for j in i.split(","):
                self.miLetra[len(self.miLetra) - 1].append(Letra(j.replace("\n", "")))
                self.copia[len(self.miLetra) - 1].append(Letra(j.replace("\n", "")))
        self.imprimir()

    def imprimir(self):
        print("\nCrucigrama:\n")
        for i in range(len(self.copia)):
            for j in range(len(self.copia[i])):
                print(self.copia[i][j].getLetra() + " ", end="")
            print()

    def resolverAutomaticoV1(self):
        for palabra in self.palabras:
            bandera = False
            i = 0
            while i < len(self.miLetra) and not bandera:
                j = 0
                while j < len(self.miLetra[i]) and not bandera:
                    if palabra[0] == self.miLetra[i][j].getLetra() and j + len(palabra) <= len(self.miLetra[i]):
                        cont = 0
                        bandera = True
                        for letra in palabra:
                            if letra != self.miLetra[i][j + cont].getLetra() or self.miLetra[i][
                                j + cont].getLetra() == '0':
                                bandera = False
                                break
                            cont += 1
                        if bandera:
                            for k in range(len(palabra)):
                                self.copia[i][j + k].setLetra('*')
                            palabra = '*'
                        if not bandera and i + len(palabra) <= len(self.miLetra):
                            cont = 0
                            bandera = True
                            for letra in palabra:
                                if letra != self.miLetra[i + cont][j].getLetra() or self.miLetra[i + cont][
                                    j].getLetra() == '0':
                                    bandera = False
                                    break
                                cont += 1
                            if bandera:
                                for k in range(len(palabra)):
                                    self.copia[i + k][j].setLetra('*')
                                palabra = '*'
                    j += 1
                i += 1
        self.miLetra.clear()
        self.imprimir()

    def resolverAutomaticoV2(self):
        for palabra in self.palabras:
            bandera = False
            i = 0
            while i < len(self.miLetra) and not bandera:
                linea = ""
                for j in range(len(self.miLetra[i])):
                    linea += self.miLetra[i][j].getLetra()
                if 0 <= linea.find(palabra) <= len(linea):
                    bandera = True
                    for j in range(len(palabra)):
                        self.copia[i][linea.find(palabra) + j].setLetra('*')
                    palabra = '*'
                i += 1
            if not bandera:
                i = 0
                while i < len(self.miLetra[0]) and not bandera:
                    linea = ""
                    for j in range(len(self.miLetra)):
                        linea += self.miLetra[j][i].getLetra()
                    if 0 <= linea.find(palabra) <= len(linea):
                        for j in range(len(palabra)):
                            self.copia[linea.find(palabra) + j][i].setLetra('*')
                        palabra = '*'
                    i += 1
        self.miLetra.clear()
        self.imprimir()
