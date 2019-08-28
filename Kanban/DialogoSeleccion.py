from tkinter import *
from tkinter import ttk

from DialogoEliminar import DialogoEliminar
from DialogoIngresar import DialogoIngresar
from DialogoModificar import DialogoModificar


# noinspection SpellCheckingInspection
class DialogoSeleccion:

    def __init__(self, num):
        self.frame = Tk()
        self.frame.after(1, lambda: self.frame.focus_force())
        self.frame.resizable(width=False, height=False)
        self.frame.title(f"Seleccion: {num}")

        ttk.Button(self.frame, text="Agregar", command=lambda: DialogoIngresar(num)).grid(row=0, column=0, ipady=28,
                                                                                          ipadx=18)
        ttk.Button(self.frame, text="Eliminar", command=lambda: DialogoEliminar(num)).grid(row=1, column=0, ipady=28,
                                                                                           ipadx=18)
        ttk.Button(self.frame, text="Modificar", command=lambda: DialogoModificar(num)).grid(row=2, column=0, ipady=28,
                                                                                             ipadx=18)
