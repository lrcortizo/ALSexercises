latitud = input("Latitud: ")
longitud = input("Longitud ")


def formatea_cordenadas(lat,long):
    return "(" + lat + "," + long + ")"


def formatea_cordenadas_format(lat,long):
    return str.format("({0},{1})", lat, long)

print(formatea_cordenadas(latitud,longitud))
print(formatea_cordenadas_format(latitud,longitud))