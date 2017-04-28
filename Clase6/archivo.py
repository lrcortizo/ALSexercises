# Files

# --------Abrir--------
# f = open("path/to/file", "it")

# --------Leer--------
# lista_lineas = f.readlines()
# for linea in f

# f.close()

# rt -> lectura de texto
# rU -> lectura de texto multiplataforma
# wt -> escritura de texto


def escribe_archivo(nombre, datos):
    """
    f = open(nombre, "wt")

    f.writelines([str(x + '\n' for x in datos)])

    f.close()
    """

    with open(nombre, "wt") as f:
        f.writelines([str(x + '\n' for x in datos)])
        # El error está en la cadena

def lee_archivo(nombre):
    f = open(nombre, "rU")

    toret = f.readlines()

    # with open ... se usa tambien

    f.close()
    return toret


datos = [1, 2, 3]
escribe_archivo("datos.txt", datos)
datos_leidos =  lee_archivo("datos.txt")

for l in datos_leidos:
    print(l)
print(datos_leidos)
