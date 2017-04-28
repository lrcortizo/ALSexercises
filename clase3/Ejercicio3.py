import sys

d = {}

def introducir(d):
    nombre = input("Introduce nombre: ")
    email = input("Introduce email: ")
    if d.get(nombre) == None:
        d[nombre] = email
    else:
        print("Ya existe")
def borrar(d):
    nombre = input("Introduce nombre al borrar: ")
    if d.get(nombre) == None:
        print("No existe")
    else:
        del d[nombre]
def buscar(d):
    nombre = input("Introduce nombre: ")
    if d.get(nombre) == None:
        print("No existe")
    else:
        print("Nombre: ", nombre)
        print("Email: ", d[nombre])
def listar(d):
    for x in d.keys():
        print("Nombre: ", x)
        print("Email:", d[x])
def menu():
    print("\nMENÚ PRINCIPAL:")
    print("1. Introducir")
    print("2. Borrar")
    print("3. Buscar")
    print("4. Listar")
    print("5. Salir")
    while True:
        try:
            op = int(input("Elige una opción: "))
            break
        except ValueError:
            print("Caracter no válido")
    if op <= 4:
        {1: introducir, 2: borrar, 3: buscar, 4: listar}[op](d)
    elif op == 5:
        sys.exit()
    else: print("Opción inválida")
    return op

# Inicio
op = menu()
while(op!=5):
    op = menu()