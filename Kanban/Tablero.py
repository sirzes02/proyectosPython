from tkinter import messagebox
from Tarea import Tarea


# noinspection SpellCheckingInspection
class Tablero:
    RUTAESCRITURA = "./data/reporte.txt"
    RUTALECTURA = "./data/lectura.txt"
    DELIMITANTE = "|"
    relacion = []

    def __init__(self, ruta):
        self.relacion.clear()
        self._lecturaDatos(ruta)

    def setMiTarea(self, nombre, estado, prioridad):
        for i in self.relacion:
            if i.getNombre() == nombre:
                messagebox.showinfo("Error", "Esta tarea ya existe")
                return
        self.relacion.append(Tarea(nombre, estado, prioridad))
        self.escrituraDatos()

    def deleteMiTarea(self, nombre):
        bandera = False

        for i in range(len(self.relacion)):
            if self.relacion[i].getNombre() == nombre:
                self.relacion.pop(i)
                bandera = True
                break

        if not bandera:
            messagebox.showinfo("Error", "Esta tarea no existe")

        self.escrituraDatos()

    def modificarTarea(self, nombreViejo, nombre, estado, prioridad):
        for i in self.relacion:
            if i.getNombre() == nombreViejo:
                i.setNombre(nombre)
                i.setEstado(estado)
                i.setPrioridad(prioridad)
                break
        self.escrituraDatos()

    def _lecturaDatos(self, ruta):
        br = open(ruta, "r")

        for i in br:
            datos = i.split(self.DELIMITANTE)
            self.relacion.append(Tarea(datos[0], datos[1], datos[2].replace("\n", "")))
        br.close()

    def escrituraDatos(self):
        pw = open(self.RUTALECTURA, "w")

        for i in self.relacion:
            pw.write(f"{i.getNombre()}{self.DELIMITANTE}{i.getEstado()}{self.DELIMITANTE}{i.getPrioridad()}\n")
        pw.close()
        self.reporte()

    def reporte(self):
        contPorHacer = 0
        contEnCurso = 0
        contFinalizada = 0

        for i in self.relacion:
            if i.getEstado() == "Por hacer":
                contPorHacer += 1
            elif i.getEstado() == "En curso":
                contEnCurso += 1
            else:
                contFinalizada += 1

        pw = open(self.RUTAESCRITURA, "w")
        pw.write(f"La cantidad de tareas por hacer es: {contPorHacer}.\n")
        pw.write(f"La cantidad de tareas en curso es: {contEnCurso}.\n")
        pw.write(f"La cantidad de tareas finalizadas es: {contFinalizada}.")
        pw.close()

    def getNombres(self, num):
        nombres = []
        if num == 1:
            for i in self.relacion:
                if i.getEstado() == "Por hacer" and i.getPrioridad() == "Urgente" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre())
        elif num == 2:
            for i in self.relacion:
                if i.getEstado() == "En curso" and i.getPrioridad() == "Urgente" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 3:
            for i in self.relacion:
                if i.getEstado() == "Finalizada" and i.getPrioridad() == "Urgente" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 4:
            for i in self.relacion:
                if i.getEstado() == "Por hacer" and i.getPrioridad() == "Importante" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 5:
            for i in self.relacion:
                if i.getEstado() == "En curso" and i.getPrioridad() == "Importante" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 6:
            for i in self.relacion:
                if i.getEstado() == "Finalizada" and i.getPrioridad() == "Importante" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 7:
            for i in self.relacion:
                if i.getEstado() == "Por hacer" and i.getPrioridad() == "Normal" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        elif num == 8:
            for i in self.relacion:
                if i.getEstado() == "En curso" and i.getPrioridad() == "Normal" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        else:
            for i in self.relacion:
                if i.getEstado() == "Finalizada" and i.getPrioridad() == "Normal" and not i.getNombre() in nombres:
                    nombres.append(i.getNombre)
        return nombres
