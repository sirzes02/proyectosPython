from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font

from PIL import Image, ImageTk

from Juego import Juego


# noinspection SpellCheckingInspection
class Frame:
    botones = list()
    posicion = list()
    img = Image.open("./imagenes/signo.gif")

    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("600x600")
        self.frame.resizable(width=False, height=False)
        self.frame.iconbitmap("./imagenes/icon.ico")
        self.frame.protocol("WM_DELETE_WINDOW", self.cerrando)
        self.colocarComponentes()
        self.frame.mainloop()

    def cerrando(self):
        messagebox.showinfo('Fin', "Gracias por jugar.")
        self.frame.quit()

    def cargarMundo(self):
        self.miJuego = Juego()
        self.contador = 0
        self.miJuego.cargarJuego(self.aux)
        self.miJuego.reiniciarPartidad(self.miJuego.getContPartidas() - 1)

    def otroJuego(self, nivel):
        self.contador = 0
        self.colocarBotones(nivel)
        self.miJuego.cargarJuego(self.aux)
        self.miJuego.reiniciarPartidad(self.miJuego.getContPartidas() - 1)
        self.puntaje.configure(text=self.miJuego.getMiPartida(self.miJuego.getContPartidas() - 1).getPUNTAJEINICIAL())
        self.cont = 0
        self.enviari = 0
        self.enviarj = 0

    def colocarComponentes(self):
        self.frame.title("Concentrese")
        self.frame.configure(background="#fff")

        photo = PhotoImage(file="./imagenes/bienvenidos.gif")
        self.tituloMenu = Label(self.frame, image=photo, background="#fff")
        self.tituloMenu.image = photo
        self.tituloMenu.grid(row=0, column=0)

        photo = ImageTk.PhotoImage(Image.open("./imagenes/tablero.png"))
        self.tableroMenu = Label(self.frame, image=photo, background="#fff")
        self.tableroMenu.image = photo
        self.tableroMenu.grid(row=1, column=0)

        self.listaDesplegable = ttk.Combobox(self.frame, state="readonly", values=["Facil", "Medio", "Dificil"],
                                             font=Font(family="Nyala", size=27, slant="italic"), width=5)
        self.listaDesplegable.current(1)
        self.listaDesplegable.bind("<<ComboboxSelected>>", self.dificultad)
        self.listaDesplegable.grid(row=2, column=0)

    def dificultad(self, event=None):
        if self.listaDesplegable.get() == "Dificil":
            self.tituloMenu.grid_remove()
            self.tableroMenu.grid_remove()
            self.listaDesplegable.grid_remove()
            self.aux = 2
            self.cargarMundo()
            self.colocarExterior(2)
            self.colocarBotones(2)
        elif self.listaDesplegable.get() == "Medio":
            self.tituloMenu.grid_remove()
            self.tableroMenu.grid_remove()
            self.listaDesplegable.grid_remove()
            self.aux = 1
            self.cargarMundo()
            self.colocarExterior(1)
            self.colocarBotones(1)
        else:
            self.tituloMenu.grid_remove()
            self.tableroMenu.grid_remove()
            self.listaDesplegable.grid_remove()
            self.aux = 0
            self.cargarMundo()
            self.colocarExterior(0)
            self.colocarBotones(0)

    def colocarExterior(self, nivel):
        self.frame.configure(background="#E4D3F5")

        self.borde = Canvas(width=158, height=494, bg="#E4D3F5")
        self.borde.place(x=433, y=42)
        self.borde.create_rectangle(0, 0, 158, 494, width=0)

        self.titulo = Label(self.frame, text="      Encuentra los pares de los profesores",
                            font=Font(family="Nyala", size=21, weight="bold"), background="#E4D3F5")
        self.titulo.grid(row=0, column=0)

        img = Image.open("./imagenes/uscLogo.png")
        img = img.resize((72, 72), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        self.logo = Label(self.frame, image=photo, background="#E4D3F5")
        self.logo.image = photo
        self.logo.place(x=477, y=45)

        self.puntajeLetra = Label(self.frame, text="Puntaje:", font=Font(family="Nyala", size=28, weight="bold"),
                                  background="#E4D3F5")
        self.puntajeLetra.place(x=437, y=145)

        self.puntaje = Label(self.frame,
                             text=self.miJuego.getMiPartida(self.miJuego.getContPartidas() - 1).getPuntaje(),
                             font=Font(family="Nyala", size=50, weight="bold"), background="#E4D3F5")
        self.puntaje.place(x=447, y=215)

        self.botonReiniciar = ttk.Button(self.frame, text="Reiniciar", command=lambda: self.otroJuego(nivel))
        self.botonReiniciar.place(x=445, y=365, height=80, width=140)

        self.botonReporte = ttk.Button(self.frame, text="Reporte", command=lambda: self.generarReporte())
        self.botonReporte.place(x=445, y=455, height=80, width=140)

        img = Image.open("./imagenes/volver.png.png")
        photo = ImageTk.PhotoImage(img)
        self.botonSalir = ttk.Button(self.frame, image=photo, command=lambda: self.atras())
        self.botonSalir.image = photo
        self.botonSalir.place(x=20, y=550)

    def atras(self):
        self.titulo.grid_remove()
        self.logo.destroy()
        self.puntajeLetra.destroy()
        self.puntaje.destroy()
        self.botonReiniciar.destroy()
        self.botonReporte.destroy()
        self.botonSalir.destroy()
        self.borde.destroy()
        for i in self.botones:
            i.destroy()
        self.colocarComponentes()

    def generarReporte(self):
        self.miJuego.generarReporte()
        messagebox.showinfo("Reporte", self.miJuego.imprimirTodo())

    def colocarBotones(self, dificultad):
        contador = 0

        self.posicion.clear()
        self.botones.clear()
        photo = ImageTk.PhotoImage(self.img)
        if dificultad is 0:
            for i in range(2):
                for j in range(3):
                    self.botones.append(ttk.Button(self.frame, image=photo))
                    self.botones[contador].image = photo
                    self.botones[contador].place(x=(130 * i) + 120, y=(130 * j) + 105, height=100, width=100)
                    contador += 1
        elif dificultad is 1:
            for i in range(3):
                for j in range(4):
                    self.botones.insert(contador, ttk.Button(self.frame, image=photo))
                    self.botones[contador].image = photo
                    self.botones[contador].place(x=(130 * i) + 50, y=(130 * j) + 45, height=100, width=100)
                    contador += 1
        else:
            img = self.img.resize((60, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            for i in range(6):
                for j in range(4):
                    self.botones.insert(contador, ttk.Button(self.frame, image=photo))
                    self.botones[contador].image = photo
                    self.botones[contador].place(x=(65 * i) + 30, y=(130 * j) + 45, height=100, width=60)
                    contador += 1
        try:
            self.botones[0].configure(command=lambda: self.click(0, dificultad))
            self.botones[1].configure(command=lambda: self.click(1, dificultad))
            self.botones[2].configure(command=lambda: self.click(2, dificultad))
            self.botones[3].configure(command=lambda: self.click(3, dificultad))
            self.botones[4].configure(command=lambda: self.click(4, dificultad))
            self.botones[5].configure(command=lambda: self.click(5, dificultad))
            self.botones[6].configure(command=lambda: self.click(6, dificultad))
            self.botones[7].configure(command=lambda: self.click(7, dificultad))
            self.botones[8].configure(command=lambda: self.click(8, dificultad))
            self.botones[9].configure(command=lambda: self.click(9, dificultad))
            self.botones[10].configure(command=lambda: self.click(10, dificultad))
            self.botones[11].configure(command=lambda: self.click(11, dificultad))
            self.botones[12].configure(command=lambda: self.click(12, dificultad))
            self.botones[13].configure(command=lambda: self.click(13, dificultad))
            self.botones[14].configure(command=lambda: self.click(14, dificultad))
            self.botones[15].configure(command=lambda: self.click(15, dificultad))
            self.botones[16].configure(command=lambda: self.click(16, dificultad))
            self.botones[17].configure(command=lambda: self.click(17, dificultad))
            self.botones[18].configure(command=lambda: self.click(18, dificultad))
            self.botones[19].configure(command=lambda: self.click(19, dificultad))
            self.botones[20].configure(command=lambda: self.click(20, dificultad))
            self.botones[21].configure(command=lambda: self.click(21, dificultad))
            self.botones[22].configure(command=lambda: self.click(22, dificultad))
            self.botones[23].configure(command=lambda: self.click(23, dificultad))
        except:
            None

    def click(self, pos, dificultad):
        if len(self.posicion) is 0:
            self.revelar(pos, dificultad)
        elif len(self.posicion) is 1:
            self.revelar(pos, dificultad)
            if not self.botones[self.posicion[0]] is self.botones[self.posicion[1]]:
                if self.miJuego.validar(self.miJuego.getContPartidas() - 1, self.posicion[0], self.posicion[1]):
                    self.botones[self.posicion[0]].configure(state="disable")
                    self.botones[self.posicion[1]].configure(state="disable")
                    self.posicion.clear()
                    self.contador += 1
                self.puntaje.configure(
                    text=self.miJuego.getMiPartida(self.miJuego.getContPartidas() - 1).getPuntaje())
        else:
            self.girar()
            self.click(pos, dificultad)
        if self.contador == len(self.botones) / 2:
            messagebox.showinfo('Final', "Felicidades, ganaste.")

    def girar(self):
        photo = ImageTk.PhotoImage(self.img)
        self.botones[self.posicion[0]].configure(image=photo)
        self.botones[self.posicion[0]].image = photo
        self.botones[self.posicion[1]].configure(image=photo)
        self.botones[self.posicion[1]].image = photo
        self.posicion.clear()

    def revelar(self, pos, dificultad):
        self.posicion.append(pos)
        if dificultad == 2:
            img = Image.open(
                self.miJuego.getMiPartida(self.miJuego.getContPartidas() - 1).getMiFicha(pos).getDirImagen())
            img = img.resize((60, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
        else:
            photo = ImageTk.PhotoImage(Image.open(
                self.miJuego.getMiPartida(self.miJuego.getContPartidas() - 1).getMiFicha(pos).getDirImagen()))
        self.botones[pos].configure(image=photo)
        self.botones[pos].image = photo


def main():
    Frame()
    return 0


if __name__ == '__main__':
    main()
