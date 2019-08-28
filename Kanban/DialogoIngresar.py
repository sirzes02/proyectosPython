from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tablero import Tablero


# noinspection SpellCheckingInspection
class DialogoIngresar:

    def __init__(self, num):
        self.accion = Tablero("./data/lectura.txt")
        self.frame = Tk()
        self.frame.after(1, lambda: self.frame.focus_force())
        self.frame.resizable(width=False, height=False)
        self.frame.title(f"Agregar: {num}")

        Label(self.frame, text="Nombre", width=15).grid(row=0, column=0)
        self.texto = Entry(self.frame, width=15)
        self.texto.focus_set()
        self.texto.grid(row=0, column=1)

        ttk.Button(self.frame, text="Agregar", command=lambda: self.enviar(num)).grid(row=1, column=0, ipadx=18)

    def enviar(self, num):
        if not self.texto.get():
            messagebox.showinfo("Error", "Debe ingresar un nombre.")
            self.frame.after(1, lambda: self.frame.focus_force())
        else:
            if num == 1:
                self.accion.setMiTarea(self.texto.get(), "Por hacer", "Urgente")
            elif num == 2:
                self.accion.setMiTarea(self.texto.get(), "En curso", "Urgente")
            elif num == 3:
                self.accion.setMiTarea(self.texto.get(), "Finalizada", "Urgente")
            elif num == 4:
                self.accion.setMiTarea(self.texto.get(), "Por hacer", "Importante")
            elif num == 5:
                self.accion.setMiTarea(self.texto.get(), "En curso", "Importante")
            elif num == 6:
                self.accion.setMiTarea(self.texto.get(), "Finalizada", "Importante")
            elif num == 7:
                self.accion.setMiTarea(self.texto.get(), "Por hacer", "Normal")
            elif num == 8:
                self.accion.setMiTarea(self.texto.get(), "En curso", "Normal")
            else:
                self.accion.setMiTarea(self.texto.get(), "Finalizada", "Normal")
            self.frame.destroy()
