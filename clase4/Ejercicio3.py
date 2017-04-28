# Ejercicio 3

class Pieza:
    def __init__(self, p):
        self.precio = p

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, v):
        self._precio = v

class Tuberia(Pieza):
    def __init__(self, p):
        super().__init__(p)

class Tuerca(Pieza):
    def __init__(self, p):
        super().__init__(p)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, v):
        self._precio = v

class Codo(Pieza):
    def __init__(self, p):
        super().__init__(p)

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, v):
        self._precio = v

class Inventario:
    def __init__(self):
        self.lista = []

    def alta(self, p):
        self.lista.append(p)

    def baja(self, p):
        self.lista.remove(p)

    def modificar(self, x, p):
        self.lista[self.lista.index(x)].precio = p

    def listar(self):
        for x in self.lista:
            print(str(x.__class__.__name__) + ": " + str(x.precio))

tub1 = Tuberia(50)
tub2 = Tuberia(40)
tub3 = Tuberia(35)
tuer1 = Tuerca(52)
tuer2 = Tuerca(34)
tuer3 = Tuerca(47)
c1 = Codo(12)
c2 = Codo(32)
c3 = Codo(24)

inv = Inventario()
inv.alta(tub1)
inv.alta(tub2)
inv.alta(tub3)
inv.alta(tuer1)
inv.alta(tuer2)
inv.alta(tuer3)
inv.alta(c1)
inv.alta(c2)
inv.alta(c3)
inv.listar()

inv.baja(tub2)
inv.baja(c1)
inv.baja(tuer3)
print("------Despues de borrado---------")
inv.listar()

inv.modificar(tub1, 99)
inv.modificar(c2, 87)
inv.modificar(tuer2, 71)
print("------Despues de modificar---------")
inv.listar()