l = [1, 2, 3]
# un elemento concreto
print(l[0])

# imprime el array concreto
for x in l:
        print(x, end=' ')

for i, x in enumerate(l):
        print(str.format("{0}: {1}", i, x), end=", ")

#numero de elementos
print("\nNum. de elementos: ", len(l))

# slices
# del segundo en adelante
print("\nDel segundo en adelante: ", l[1:])

# Los dos primeros elementos
print("\nLos dos primeros: ", l[0:2])

print("\nHasta el segundo: ", l[:2])

#Ultimo elemento
print("\nUltimo elemento: ", l[-1])

#Compresion de listas
print(list([(x if x%2 == 0 else 0) for x in l]))

#fibonacci
def fibonacci(x):
        l=[0,1]
        for _ in range(x-2):
                l.append(l[-1]+l[-2])
        return l[0:x]

print(fibonacci(4))

#primos
def primos(x):
        def esPrimo(x):
                label = True
                if x ==2:
                        label = False
                elif x%2 == 0:
                        label=False
                else:
                        for i in range(3, x, 2):
                                if x % i == 0:
                                        break
                        else:
                                toret = False
                return label
        l = []
        i = 2
        while len(l) < x:
                if esPrimo(i) == True:
                        l.append(i)
                i+=1;
        return l
print("\nNumeros primos: ", primos(6))
