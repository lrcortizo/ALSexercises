#Ejercicio 2
class Prestamo:
    def __init__(self, c, imp, int):
        self.numCuotas = c
        self.importe = imp + (imp+int)
        self.interes = int
        self.cuota = self.importe/c

    @property
    def importe(self):
        return self._importe

    @importe.setter
    def importe(self, v):
        self._importe = v

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, v):
        self._interes = v

    @property
    def cuota(self):
        return self._cuota

    @cuota.setter
    def cuota(self, v):
        self._cuota = v

    def paga_cuota(self):
        self.importe -= self.cuota

    def get_num_cuotas(self):
        return self.importe/self.cuota

    def amortiza(self, x):
        self.importe -= x
        self.cuota = self.importe/self.numCuotas

p1 = Prestamo(90, 8000, 10)
print("Interes: ", p1.interes)
print("Cuota: ", p1.cuota)
print("Importe:", p1.importe)
print("Cuotas restantes: ", p1.get_num_cuotas())

p1.amortiza(250)
print("-------Despues de amortizar 250----------")
print("Cuota: ", p1.cuota)
print("Importe:", p1.importe)

for x in range(0, 5, 1):
    p1.paga_cuota()
print("-------Despues de pagar 5 cuotas----------")
print("Cuota: ", p1.cuota)
print("Importe:", p1.importe)
print("Cuotas restantes: ", p1.get_num_cuotas())