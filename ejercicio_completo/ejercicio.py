# Ejercicio completo
# 1. Crea una clase Libro, que guarde título, autor,
# editorial, y fecha de devolución.
# Crea también la clase biblioteca, que guarda libros.

from datetime import date
import pickle

class Libro:
    def __init__(self, t, a, e):
        self.titulo = t
        self.autor = a
        self.editorial = e
        self.fechadevolucion = date.min

    def pon_fecha_devolucion(self, v):
        self.fechadevolucion = v

    def __getattr__(self, item):
        if item == "esta_prestado":
            return lambda: (self.fechadevolucion > date.today())
    def __str__(self):
        return "(" + str(self.titulo) + ", " + str(self.autor) + ", " + str(self.editorial) + ", " + str(self.fechadevolucion) + ")"

class Biblioteca:

    def __init__(self):
        self.biblioteca = []

    def inserta(self, l):
        self.biblioteca += [l]

    def guarda(self, nf):
        with open(nf, "wb") as f:
            for l in self.biblioteca:
                pickle.dump(l, f)

    @staticmethod
    def carga(self, nf):
        toret = Biblioteca()
        try:
            with open(nf, "rb") as f:
                while(True):
                    toret.inserta(pickle.load(f))
        finally:
            return toret

    def __len__(self):
        return len(self.biblioteca)

    def __str__(self):
        toret = ""
        for libro in self.biblioteca:
            toret += str(libro)
        return toret




if __name__ == "__main__":

    b = Biblioteca()
    if(len(b) == 0):
        l1 = Libro("El conde de montecristo", "Alejandro Dumas", "Timun-Mas")
        l1.pon_fecha_devolucion(date(2017, 5, 9))

        l2 = Libro("Viaje al centro de la Tierra", "Julio Verne", "Timun-Mas")
        l2.pon_fecha_devolucion(date(2017, 5, 1))
        b.inserta(l1)
        b.inserta(l2)

    print(l1)
    print(l2)

    print("l1 esta prestado: ", l1.esta_prestado())
    print("l2 esta prestado: ", l2.esta_prestado())

    print(b)





