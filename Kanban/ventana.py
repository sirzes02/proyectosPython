from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk

from DialogoSeleccion import DialogoSeleccion


# noinspection SpellCheckingInspection
class Frame:

    def __init__(self):
        self.frame = Tk()
        self.frame.resizable(width=False, height=False)
        self.frame.title("Kanban")
        self.frame.protocol("WM_DELETE_WINDOW", self.cerrando)

        img = Image.open("./img/uscLogo.png")
        img = img.resize((70, 70), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        Label(self.frame, image=photo).grid(row=0, column=0)

        Label(self.frame, relief=GROOVE, text="Por hacer", width=15, height=5).grid(row=0, column=1)
        Label(self.frame, relief=GROOVE, text="En curso", width=15, height=5).grid(row=0, column=2)
        Label(self.frame, relief=GROOVE, text="Finalizada", width=15, height=5).grid(row=0, column=3)
        Label(self.frame, relief=GROOVE, text="Urgente", width=15, height=5).grid(row=1, column=0)
        Label(self.frame, relief=GROOVE, text="Importante", width=15, height=5).grid(row=2, column=0)
        Label(self.frame, relief=GROOVE, text="Nomal", width=15, height=5).grid(row=3, column=0)

        ttk.Button(self.frame, text=1, command=lambda: DialogoSeleccion(1)).grid(row=1, column=1, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=2, command=lambda: DialogoSeleccion(2)).grid(row=1, column=2, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=3, command=lambda: DialogoSeleccion(3)).grid(row=1, column=3, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=4, command=lambda: DialogoSeleccion(4)).grid(row=2, column=1, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=5, command=lambda: DialogoSeleccion(5)).grid(row=2, column=2, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=6, command=lambda: DialogoSeleccion(6)).grid(row=2, column=3, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=7, command=lambda: DialogoSeleccion(7)).grid(row=3, column=1, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=8, command=lambda: DialogoSeleccion(8)).grid(row=3, column=2, ipady=28, ipadx=18)
        ttk.Button(self.frame, text=9, command=lambda: DialogoSeleccion(9)).grid(row=3, column=3, ipady=28, ipadx=18)

        self.frame.mainloop()

    def cerrando(self):
        br = open("./data/reporte.txt", "r")
        texto = ""
        for i in br:
            texto += i
        messagebox.showinfo("Reporte", texto)
        self.frame.quit()


def main():
    Frame()
    return 0


if __name__ == '__main__':
    main()
