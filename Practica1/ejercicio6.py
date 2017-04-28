def calcuar(num1, num2, op):
    def sumar(x,y):
        return x+y

    def restar(x,y):
        return x-y

    def multiplicar(x,y):
        return x*y

    def dividir(x,y):
        return x/y

    def elevar(x,y):
        return x**y

    return {
        '+': sumar(num1, num2),
        '-': restar(num1, num2),
        '*': multiplicar(num1, num2),
        '/': dividir(num1, num2),
        '^': elevar(num1, num2)
    }[op]


def introducir():
    num1 = float(input("Operando 1: "))
    num2 = float(input("Operando 2: "))
    op = input("Operador: ")
    return calcuar(num1, num2, op)

print(introducir())