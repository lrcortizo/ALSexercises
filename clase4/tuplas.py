#tuplas
t0 = ()
t1 = (1,)
t = (1, 2, 3)

def getOrigen():
    return (0, 0)

def multiplica_punto(p, k):
    l = list(p)
    for i, x in enumerate(l):
        l[i] *= k
    return tuple(l)

def multiplica_punto2(p, k):
    l = []
    for x in p:
        l.append(x * k)
    return tuple(l)

p0 = getOrigen()
print("Origen:", p0)

x0, y0 = getOrigen()
print(str.format("Origen: ({0}, {1})", x0, y0))
t = (10, 10)
print("(10, 10) * 2", multiplica_punto(t, 2))

t9 =(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("t9[1:5]:", t9[1:5])
print("len(t9):", len(t9))
print("4 in t9:", 4 in t9)