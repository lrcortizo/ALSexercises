num = int(input("Inserta un número: "))
print("Numero a calcular -> " + str(num))

# java -> python
# --------------
# &&   -> and
# ||   -> or
# !    -> not
# x++  -> x+=1

def doble(x):
    def multiplica(x,y):
        return x*y
    return multiplica(x,2)


# Problema al llamar a la función recursiva muchas veces: 1000(ej)
def factorial_recursivo(x):
    if x < 2:
        return 1
    else:
        return x*factorial_recursivo(x-1)


def factorial(x):
    toret = x
    # for <var> in range(<inicio>, <fin>, <incremento/decremento>):
    for i in range(x, 1, -1):
        toret *= i
    return toret

print(doble(num))

print(factorial(num))

print(isinstance(5, int))

range(5)

list(range(5))

list(range(1, 5, 2))

simple = str.format("{0}x{1}={2}", 5, 6, 5*6)

print(simple)

formateado = str.format("{0:02.2f}x{1:02.2f}={2:04.2f}", 5, 6, 5*6)

print(formateado)

"TEsT".isupper()  # false