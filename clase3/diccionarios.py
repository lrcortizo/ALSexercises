# Diccionarios
def f1():
    print("f1")

def f2():
    print("f2")



d0 = {}
d = {"Ourense": 10, "Vigo": 12, "Coruña": 12}

print(d0)
print(d)
print(d["Ourense"])
print(d.get("Vigo"))
print(d.get("Teruel"))
print(d.keys())
print(d.values())

for k in d.keys():
    print(d[k], end=' ')

for k, v in enumerate(d):
    print(str.format("{0} = {1}", k, v))

print("\n")
op = int(input("Opc: "))
f = {1: f1, 2: f2}.get(op)
if f:
    f()
else:
    print("opc. incorrecta")