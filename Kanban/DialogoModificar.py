from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tablero import Tablero


# noinspection SpellCheckingInspection
class DialogoModificar:

    def __init__(self, num):
        self.accion = Tablero("./data/lectura.txt")
        self.frame = Tk()
        self.frame.after(1, lambda: self.frame.focus_force())
        self.frame.resizable(width=False, height=False)
        self.frame.title(f"Modificar: {num}")

        self.numero = num

        Label(self.frame, text="Seleccione:", width=15).grid(row=0, column=0)
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

        Label(self.frame, text="Nombre", width=15).grid(row=1, column=0)
        self.nombre = Entry(self.frame, state="disable", width=23)
        self.nombre.grid(row=1, column=1)

        Label(self.frame, text="Estado", width=15).grid(row=2, column=0)
        self.selecEstado = ttk.Combobox(self.frame, state="disable")
        self.selecEstado.grid(row=2, column=1)

        Label(self.frame, text="Prioridad", width=15).grid(row=3, column=0)
        self.selecPrioridad = ttk.Combobox(self.frame, state="disable")
        self.selecPrioridad.grid(row=3, column=1)

        self.boton1 = ttk.Button(self.frame, state="disable", text="Modificar", command=lambda: self.modificar())
        self.boton1.grid(row=4, column=0, ipadx=18)

    # noinspection PyUnusedLocal
    def validar(self, event=None):
        if not self.seleccion.get() == "Sin tareas" and not self.seleccion.get() == "Seleccione:":
            self.nombre.configure(state="normal")
            self.nombre.insert(0, self.seleccion.get())
            self.nombre.focus_set()

            self.selecEstado.configure(state="readonly")
            self.selecEstado["values"] = ["Por hacer", "En curso", "Finalizada"]

            self.selecPrioridad.configure(state="readonly")
            self.selecPrioridad["values"] = ["Normal", "Importante", "Urgente"]

            self.boton1.configure(state="enable")
            if self.numero == 1:
                self.selecEstado.current(0)
                self.selecPrioridad.current(2)
            elif self.numero == 2:
                self.selecEstado.current(1)
                self.selecPrioridad.current(2)
            elif self.numero == 3:
                self.selecEstado.current(2)
                self.selecPrioridad.current(2)
            elif self.numero == 4:
                self.selecEstado.current(0)
                self.selecPrioridad.current(1)
            elif self.numero == 5:
                self.selecEstado.current(1)
                self.selecPrioridad.current(1)
            elif self.numero == 6:
                self.selecEstado.current(2)
                self.selecPrioridad.current(1)
            elif self.numero == 7:
                self.selecEstado.current(0)
                self.selecPrioridad.current(0)
            elif self.numero == 8:
                self.selecEstado.current(1)
                self.selecPrioridad.current(0)
            else:
                self.selecEstado.current(2)
                self.selecPrioridad.current(0)

    def modificar(self):
        if not self.nombre.get():
            messagebox.showinfo("Error", "Debe ingresar un nombre.")
            self.frame.after(1, lambda: self.frame.focus_force())
        else:
            self.accion.modificarTarea(self.seleccion.get(), self.nombre.get(), self.selecEstado.get(),
                                       self.selecPrioridad.get())
            self.frame.destroy()
