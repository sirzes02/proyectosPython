"""
Damas no convencionales
REGLAS:
1. No en valido retroseder las fichas
GANAR:
1. Se deben tener 7 fichas en la zona del oponente
2. El oponente debe tener minimo 7 fichas
TURNOS:
0 - las X
1 - Las O
"""

# sys para terminar el programa con el comando sys.exit()
import sys
# time para pausar la pantalla con el comando time.sleep(), por parametro recibe los segundos que se pausara el programa
import time


class Board:

    # Constructor
    def __init__(self):
        # Se define damas como una lista
        self.miDama = list()
        self.create()
        # Se empieza el juego y se envia por parametro el primer turno, 0
        self.play(0)

    def create(self):
        # Creacion de matriz
        self.miDama = [['-', 'O', '-', 'O', '-', 'O', '-', 'O', '-', 'O'],
                       ['O', '-', 'O', '-', 'O', '-', 'O', '-', 'O', '-'],
                       ['-', 'O', '-', 'O', '-', 'O', '-', 'O', '-', 'O'],
                       ['O', '-', 'O', '-', 'O', '-', 'O', '-', 'O', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                       ['-', 'X', '-', 'X', '-', 'X', '-', 'X', '-', 'X'],
                       ['X', '-', 'X', '-', 'X', '-', 'X', '-', 'X', '-'],
                       ['-', 'X', '-', 'X', '-', 'X', '-', 'X', '-', 'X'],
                       ['X', '-', 'X', '-', 'X', '-', 'X', '-', 'X', '-']]

    def show(self):
        # Impresion numeracion superior
        print("\n    0 1 2 3 4 5 6 7 8 9\n")
        # Se recorre el arreglo
        # Para i desde 0 hasta 10
        for i in range(len(self.miDama)):
            # Impresion indice izquierdo sin saltar
            print(f"{i}   ", end='')
            # Para cada miDama un j
            for j in self.miDama[i]:
                # Impresion ficha sin saltar
                print(f"{j} ", end='')
            # Impresion indice derecho sin saltar
            print(f"  {i}")
        # Impresion numeracion inferior
        print("\n    0 1 2 3 4 5 6 7 8 9\n")

    # Recursion en funcion de juego
    def play(self, count):
        # Se llama a imprimir
        self.show()

        # Si el contador es 0
        if count == 0:
            # contador es igual a 1
            count = 1
            print("Turno de las Blancas (X)")
            # Se llama a la deleccion de movimiento
            self.selectionMove('X')
        # Sino
        else:
            # contador es igual a 0
            count = 0
            print("Turno de las Negras (O)")
            # Se llama a la deleccion de movimiento
            self.selectionMove('O')

        # Se llama a si misma con la variable actualizada
        self.play(count)

    def selectionMove(self, dama):
        # Mientras infinito
        while True:
            print("Seleccione la ficha a mover, (Coordenadas X, Y)")
            # Captura de datos

            """
            En la lectura de la posicion y el move, se verificara que solo sean dos digitos ingresdos desde 00 a
            99, desde la primera columna y fila hasta la ultima de cada uno.
            De los dos digitos: 
            int(selection[0]), devuelve el primer digito del numero ingresado
            int(selection[1]), devuelve el segundo digito del numero ingresado
            """

            selection = input()
            # Si la ficha seleccionada es corresponde al turno y la funcion ingreso retorna verdadero
            if self.miDama[int(selection[0])][int(selection[1])] == dama and self.verificarIngreso(selection):
                # Se declara la flag con falso
                flag = False

                print("Seleccione el lugar a mover, (Coordenadas X, Y)")
                move = input()
                # Si la funcion ingreso retorna verdadero
                if self.verificarIngreso(move):
                    # Validacion en X, se verifica que la ficha avance hacia el lado del oponente
                    # Si el turno es de X y el move a hacer se encuentra una fila descendiente
                    if dama == 'X' and int(move[0]) == int(selection[0]) - 1:
                        # La direccion a tomar decrese, entre 9 a 0
                        dirY = -1
                        # El inverso de la dama es 'O'
                        inverso = 'O'
                        # Bandera es verdadero
                        flag = True
                    # Sino si el turno es de O y el move a hacer se encuentra una fila ascendente
                    elif dama == 'O' and int(move[0]) == int(selection[0]) + 1:
                        # La direccion a tomar aumenta, entre 0 a 9
                        dirY = 1
                        # El inverso de la dama es 'X'
                        inverso = 'X'
                        # Bandera es verdadero
                        flag = True
                    # Si la flag es verdadera y la posicion en el tablero del move es valida (que no sea una
                    # dama de las mismas)
                    if flag and self.miDama[int(move[0])][int(move[1])] != dama:
                        # Validacion en Y, se verifica el sentido, si es derecha o izquierda respecto a las columnas
                        # Si el move horizontal va por derecha
                        if int(move[1]) == int(selection[1]) + 1:
                            # Direccion en X es positiva
                            dirX = 1
                        # Sino si el move horizontal va por izquierda
                        elif int(move[1]) == int(selection[1]) - 1:
                            # Direccion en X es negativa
                            dirX = -1
                        # Se rompe el while infinito
                        break
                    else:
                        self.error()
                else:
                    self.error()
            else:
                self.error()
        # Se llama a la funcion comer y se le envia por parametro, el turno, la ficha seleccionada, el lugar de
        # move, la direccion en x, la direccion en y, el contador de comidas, el inverso de la dama, la
        # disminusion en X y la disminusion en y
        self.comer(dama, selection, move, dirX, dirY, 0, inverso, 0, 0)

    # Funcion error
    def error(self):
        print("Error al elegir el lugar a mover, vuela a intentarlo...")
        # Esperar un segundo
        time.sleep(1)

    # Recursion en funcion comer
    def comer(self, dama, seleccion, movimiento, dirX, dirY, contComidas, inverso, disX, disY):
        # Si la suma entre el movimiento en Y y el contador por la direccion en X es 9
        if int(movimiento[1]) + (contComidas * dirX) == 9:
            # La disminusion en X equivale a 1
            disX = 1
        # Sino si la suma entre el movimiento en Y y el contador por la direccion en X es 0
        elif int(movimiento[1]) + (contComidas * dirX) == 0:
            # La disminusion en X equivale a -1
            disX = -1
        # Si la suma entre el movimiento en X y el contador por la direccion en Y es 9
        if int(movimiento[0]) + (contComidas * dirY) == 9:
            # La disminusion en Y equivale a 1
            disY = 1
        # Si la suma entre el movimiento en X y el contador por la direccion en Y es 0
        elif int(movimiento[0]) + (contComidas * dirY) == 0:
            # La disminusion en X equivale a -1
            disY = -1

        """
        Funcion matematica usando el cambio de signo multiplicando con -1, esto, segun el movimiento. 
        Ejemplo: las fichas X solo pueden disminuir su posicion en las filas para asi acercarse al contrincate, las 
        fichas O solo pueden aumentar su posicon en las filas para asi acercarse al contrincante.
        
        A su vez, se resta la dismusion, esta, funciona de la siguiente forma: en caso de la ultima ficha en comer se
        encuentre en un borde (derecho o izquierdo), se le restara o sumara 1, para asi reemplazar la ultima ficha y no 
        romper la matriz. 
        Ejemplo 1: Si la ultima ficha a comer se encuentra en la columna 9 (la ultima), y no se usa la disminucion, la
        ficha se imprimira en la columnas 10, la cual no existe y generara un error, por eso se resta 1 para asi
        imprimirla sobre la ultima ficha.
        Ejemplo 2: Si la ultima ficha a comer se encuentra en la columna 0 (la primera), y no se usa la disminucion, la
        ficha se imprimira en la columnas -1, la cual no existe y generara un error, por eso se suma 1 para asi
        imprimirla sobre la ultima ficha.
        
        self.miDama[int(movimiento[0]) + (cont * dirY) - disY][int(movimiento[1]) + (cont * dirX) - disX]
        
        El index i representa: El sitio del movimiento en X + (contador de fichas comidas * la direccion en Y
        respecto al turno) - la disminucion en y en caso de que sea 0 o 9
        
        El index j representa: El sitio del movimiento en Y + (contador de fichas comidas * la direccion en X
        respecto al turno) - la disminucion en X en caso de que sea 0 o 9
        """

        # Si la ficha ubicada en el movimiento segun las fichas comidas es igual a una ficha del oponente
        if self.miDama[int(movimiento[0]) + (contComidas * dirY) - disY][
            int(movimiento[1]) + (contComidas * dirX) - disX] == inverso:
            # La ficha ubicada en el movimiento segun las fichas comiedas sera comida, se reemplaza por un '-'
            self.miDama[int(movimiento[0]) + (contComidas * dirY)][int(movimiento[1]) + (contComidas * dirX)] = '-'
            # Aumenta el contador de fichas comidas es 1
            contComidas += 1
            # La funcion se llama a si misma con las variables actualizadas
            self.comer(dama, seleccion, movimiento, dirX, dirY, contComidas, inverso, disX, disY)
        # Sino
        else:
            # La ultima posicion analizada que no se puede comer sera reemplazada por la dama que fue seleccionada
            self.miDama[int(movimiento[0]) + (contComidas * dirY)][int(movimiento[1]) + (contComidas * dirX)] = \
                self.miDama[int(seleccion[0])][int(seleccion[1])]
            # La dama que fue seleccionada sera reemplazada por un '-'
            self.miDama[int(seleccion[0])][int(seleccion[1])] = '-'
            # Se verifica si hay un ganador por mas de 7 fichas en la zona del oponente
            #self.verificarFinalZona()
            # Se verifica si hay un ganador por menos de 7 fichas del oponente
            #self.VerificarFinalCantFicha()

    def verificarFinalZona(self):
        # Se declaran los respectivos contadores por cada dama
        contX = 0
        contO = 0

        # Se recorre el arreglo
        for i in range(len(self.miDama)):
            for j in self.miDama[i]:
                # i es menor o igual a 3 y la posicion es 'X'
                if i <= 3 and j == 'X':
                    # Contador de X aumenta en 1
                    contX += 1

                    # Si contador de X es mayor o igual a 7
                    if contX >= 7:
                        # Se llama a la funciona ganar y se envia por parametro 'O'
                        self.ganar('X')
                # Sino si i es igual a 4 o a 5
                elif i == 4 or i == 5:
                    # Rompe el segundo for
                    break
                # Sino si la posicion es 'O'
                elif j == 'O':
                    # Contador de O aumenta en 1
                    contO += 1

                    # Si contador de O es mayor o igual a 7
                    if contO >= 7:
                        # Se llama a la funciona ganar y se envia por parametro 'O'
                        self.ganar('O')

    def VerificarFinalCantFicha(self):
        # Se declaran los respectivos contadores por cada dama
        contX = 0
        contO = 0

        # Se recorre el arreglo
        for i in self.miDama:
            for j in i:
                # Si la posicion es igual a 'X'
                if j == 'X':
                    # Contador de X aumenta en 1
                    contX += 1
                # Sino si la posicion es igual a 'O'
                elif j == 'O':
                    # Contador de O aumenta en 1
                    contO += 1
        # Si contador de X es menor o igual a 7
        if contX <= 7:
            # Se llama a ganar y se envia por parametro 'O'
            self.ganar('O')
        # Si contador de O es menor o igual a 7
        if contO <= 7:
            self.ganar('X')

    # Funcion ganar
    def ganar(self, dama):
        # Se imprime la dama que gano
        print(f"Ganadoras las fichas {dama}, felicidades!.")
        # Se termina el programa
        sys.exit()

    # Funcion de verificacion de captura de datos
    def verificarIngreso(self, dato):
        # try catch
        try:
            # Se convierte en intero el dato ingresado, si se genera una excepcion se captura esta
            int(dato)
            return True if len(dato) == 2 else False
        except:
            # Si se genero una excepcion se retorna falso
            return False


def main():
    # Se llama a Tablero
    Board()


# Proceso de creacion
if __name__ == '__main__':
    main()
