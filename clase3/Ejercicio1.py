# Conversion fechas

def conversionFecha(fecha):
    meses = {"Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4, "May": 5, "Jun": 6, "Jul": 7, "Ago": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec":12}
    f = fecha.split()
    mes = meses[f[1]]
    toret = f[2] + "-" + str(mes) + "-" + f[0]

    return toret

print(conversionFecha("12 Feb 2015"))