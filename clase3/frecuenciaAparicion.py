# Frecuencia de aparicion de cada palabra y nº palabras distintas
f = open("frecuenciaAparicion.py", "rU")

p = {}
for line in f:
    line = line.strip().lower()
    for palabra in line.split():
        if not palabra in p.keys():
            p[palabra] = 1
        else:
            p[palabra] += 1
print(p)
