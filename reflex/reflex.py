class Punto:
    """Representa puntos en 2D"""
    x_origen = 0
    y_origen = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        # Se ha intentado llamar a Punto.item(), pero no se encuentra
        if item == "getX":
            return lambda: self.x
        elif item == "getY":
            return lambda: self.y
        else:
            return lambda: None

    """def __getattribute__(self, item):
        return lambda: 0"""

    def __str__(self):
        return str.format("({0}, {1})", self.x, self.y)

def from_obj_to_str(obj):
    toret = ""
    id_miembros = dir(obj)
    for id_miembro in id_miembros:
        miembro = getattr(obj, id_miembro)
        if callable(miembro):
            toret += id_miembro + "()\n"
        else:
            toret += id_miembro + ": " + str(miembro) + "\n"
    return toret

p1 = Punto(5, 6)
print(p1)
print("Punto: " + str(dir(Punto)))
print("p1: " + str(dir(p1)))
print("p1.__class__: " + str(p1.__class__))
print("Punto.__mro__: " + str(Punto.__mro__))
print("p1.__dict__: " + str(p1.__dict__))
print("Punto.__dict__: " + str(Punto.__dict__))
print("Punto.__doc__: " + str(Punto.__doc__))

#Punto.getX = lambda self: self.x
#Punto.getY = lambda self: self.y

print(str.format("p1.getX(), p1.getY(): ({0}, {1})", p1.getX(), p1.getY()))
Punto.__str__ = lambda self: str.format("({0}-{1})", self.x, self.y)
print(p1)
p1.z = 0
print(p1.z)

print(p1.__dict__["x"])
p1.__dict__["x"] = 99
print(p1.__dict__["x"])
print(p1)

p1.metodo_no_existe()

print(from_obj_to_str(p1))