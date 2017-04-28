#objetos
import math

class Punto:
    _origen = None

    @staticmethod
    def get_origen():
        if not(Punto._origen):
            Punto._origen = Punto(0, 0)
        return Punto._origen

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    def distancia_origen(self):
        return self.distancia(Punto.get_origen())

    def distancia(self, other):
        a = abs(self.x - other.x)
        b = abs(self.y - other.y)
        return math.sqrt((a ** 2 + b ** 2))

    def coordinates(self):
        return (self._x, self.y)

    def __gt__(self, other):
        toret = False

        if isinstance(other, Punto):
            toret = self.distancia_origen() > other.distancia_origen()
        return toret

    def __lt__(self, other):
        toret = False

        if isinstance(other, Punto):
            toret = self.distancia_origen() < other.distancia_origen()
        return toret

    def __eq__(self, other):
        toret = False

        if isinstance(other, Punto):
            toret = (self.x == other.x and self.y == other.y)
        return toret

    def __ne__(self, other):
        #return not(self.__eq__(other))
        toret = False

        if isinstance(other, Punto):
            toret = (self.x != other.x or self.y != other.y)
        return toret

    def  __len__(self):
        return 2

    def __add__(self, other):
        toret = None

        if isinstance(other, Punto):
            toret = Punto(self.x + other.x, self.y + other.y)
        return toret

    def __sub__(self, other):
        toret = None

        if isinstance(other, Punto):
            toret = Punto(self.x - other.x, self.y - other.y)
        return toret

    def __mul__(self, other):
        toret = None
        if isinstance(other, int):
            other = float(other)

        if isinstance(other, float):
            toret = Punto(self.x * other, self.y * other)
        return toret

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
class Linea:
    def __init__(self, x1, y1, x2=None, y2=None):
        if isinstance(x1, Punto):
            self.p1 = x1
            self.p2 = y1
        else:
            self.p1 = Punto(x1, y1)
            self.p2 = Punto(x2, y2)

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, v):
        self._p1 = v

    @property
    def p2(self):
        return self._p2

    @p1.setter
    def p2(self, v):
        self._p2 = v

    def __str__(self):
        return str(p1) + " - " + str(p2)

p1 = Punto(10, 10)
print(p1)

p2 = Punto(20, 20)
print(p2)

x, y = p2.coordinates()
print(x, y)

print(Punto.get_origen())
print(p1.distancia_origen())
print(p1.distancia(p2))

l1 = Linea(p1.x, p1.y, p2.x, p2.y)
print(l1)

l2 = Linea(p1, p2)
print(l2)

print("p1 < p2", p1 < p2)
print("p2 < p1", p2 < p1)
print("p1 > p2", p1 > p2)
print("p2 > p1", p2 > p1)
print("p1 == p2", p1 == p2)
print("p1 != p2", p1 != p2)
print(str.format("len{0} =", p1), len(p1))
print(str.format("{0} + {1} = ", p2, p1), p2+p1)
print(str.format("{0} - {1} = ", p2, p1), p2-p1)
print(str.format("{0} - {1} = ", p1, p2), p1-p2)
print(str.format("{0} * {1} = ", p1, 3), p1*3)