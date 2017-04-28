# Conjuntos

s0 = set()
print(s0)

s1 = {1, 2, 3}# set([1, 2, 3, 3]) mejor así para distinguir con diccionarios
print(s1)

s2 = set([3, 4, 5])
print(s1 | s2)
print(s1 - s2)
print(s1 & s2)

elto = int(input("Elemento: "))
print(elto in (s1 | s2))