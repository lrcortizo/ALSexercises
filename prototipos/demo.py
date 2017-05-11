class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str.format("({0}, {1})", self.x, self.y)

class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return str.format("({0}, {1}, {2})", self.x, self.y, self.z)

if __name__ == "__main__":
    p1 = Punto(5, 6)
    print(str(p1))
    print(p1.__class__)
    p1.__class__ = Punto3D
    p1.z = 0
    print(p1.__class__)
    print(str(p1))

    p2 = Punto3D(1, 2, 3)
    print(p2)
    print(p2.__class__)

    p2.__class__ = Punto
    print(p2)
    print(p2.__class__)
