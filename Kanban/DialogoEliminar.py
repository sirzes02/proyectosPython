from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tablero import Tablero


# noinspection SpellCheckingInspection
class DialogoEliminar:

    def __init__(self, num):
        self.accion = Tablero("./data/lectura.txt")
        self.frame = Tk()
        self.frame.after(1, lambda: self.frame.focus_force())
        self.frame.resizable(width=False, height=False)
        self.frame.title(f"Eliminar: {num}")

        Label(self.frame, text="Nombre", width=15).grid(row=0, column=0)
        self.seleccion = ttk.Combobox(self.frame, state="readonly")
        if len(self.accion.getNombres(num)) > 0:
            cache = list()
            cache.append("Seleccione:")
            for i in self.accion.getNombres(num):
                cache.append(i)
            self.seleccion["values"] = cache
        else:
            self.seleccion["values"] = ["Sin tareas"]
        self.seleccion.current(0)
        self.seleccion.focus_set()
        self.seleccion.grid(row=0, column=1)
        self.seleccion.bind("<<ComboboxSelected>>", self.validar)

        self.boton1 = ttk.Button(self.frame, state="disable", text="Eliminar", command=lambda: self.eliminar())
        self.boton1.grid(row=1, column=0, ipadx=18)

    # noinspection PyUnusedLocal
    def validar(self, event=None):
        if not self.seleccion.get() == "Sin tareas":
            self.boton1.configure(state="enable")

    def eliminar(self):
        if not self.seleccion.get() == "Seleccione:":
            self.accion.deleteMiTarea(self.seleccion.get())
            self.frame.destroy()
        else:
            messagebox.showinfo("Error", "Debe Seleccionar una opcion.")
            self.frame.after(1, lambda: self.frame.focus_force())
