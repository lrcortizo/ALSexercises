# Examen parcial 2 ALS 2014-15
# coding=UTF-8

import unittest
import pickle
import json

# Pregunta 1 -----------------------------------------------------------------
class Pieza:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def __str__(self):
        return str.format("{0}: {1}", self.id, self.nombre)
	
def save():
    f = None
    try:
        f = open("piezas.dat", "wb")
        pickle.dump(dictPiezas, f)
    finally:
        if f != None:
            f.close()
    
def load():
    dPiezas = {}
    f = None
    try:
        f = open("piezas.dat", "rb")
        dPiezas = pickle.load(f)
    finally:
        if f != None:
            f.close()
            
    return dPiezas
            
def piezas2str(dp):
    toret = "\n"
    for p in dp.values():
        toret += str(p) + '\n'
        
    return toret

# Pregunta 2 -----------------------------------------------------------------
class ListaOrdenada:
    def __init__(self):
        self.l = []
        
    def to_list(self):
        return self.l.copy()
    
    def inserta(self, x):
        i = 0
        
        while( i < len(self.l)
           and self.l[i] < x):
            i += 1
            
        self.l.insert(i, x)
        return
    
    def borraEn(self, i):
        if (len(self.l) > i):
            self.l.pop(i)
    
    def __str__(self):
        toret = "[ "
        for x in l:
            toret += str(x) + ' '
        toret += ']'
        return toret
    
class TestListaOrdenada(unittest.TestCase):
    def setUp(self):
        self.l = ListaOrdenada()
        self.l.inserta(1)
        self.l.inserta(4)
        self.l.inserta(6)
        
    def test_inserta(self):
        resultado = [ 1, 2, 3, 4, 5, 6 ]
        self.l.inserta(2)
        self.l.inserta(3)
        self.l.inserta(5)
        
        self.assertEqual(resultado, self.l.to_list())
        
    def test_borraEn(self):
        resultado = [ 1, 6 ]
        self.l.borraEn(1)
        self.assertEqual(resultado, self.l.to_list())

# Pregunta 3 -----------------------------------------------------------------
collatz = lambda n: \
	[] if n <= 1 else \
	[(3 * n) + 1] + collatz((3 * n) + 1) if n % 2 != 0 else \
	[n // 2] + collatz(n // 2)

# Pregunta 4 -----------------------------------------------------------------
def invoke(obj, strMth):
	toret = None
	m = getattr(obj, strMth)
	if    (m != None
	  and callable(m)):
		toret = m()
	return toret
	
# Pregunta 5 -----------------------------------------------------------------
class PuntosPartido:
	def __init__(self):
		self.puntos = {}
		
	def inserta(self, dorsal, nombre):
		dorsal = str(dorsal)
		self.puntos[dorsal] = {"nombre": nombre, "faltas": 0, "puntos": 0}
		
	def ponFalta(self, dorsal):
		dorsal = str(dorsal)
		self.puntos[dorsal]["faltas"] += 1
		
	def ponCanasta(self, dorsal):
		dorsal = str(dorsal)
		self.puntos[dorsal]["puntos"] += 2
		
	def getFaltas(self, dorsal):
		dorsal = str(dorsal)
		return self.puntos[dorsal]["faltas"]
		
	def getPuntos(self, dorsal):
		dorsal = str(dorsal)
		return self.puntos[dorsal]["puntos"]
		
	def getInfo(self, dorsal):
		dorsal = str(dorsal)
		return self.puntos[dorsal]

	def save(self, nf):
		f = open(nf, "w");
		json.dump(self.puntos, f)
		f.close()
		
	@staticmethod
	def load(nf):
		toret = PuntosPartido()
		f = open(nf, "r");
		info = json.load(f)
		f.close()
		toret.puntos = info
		return toret

# Demo -----------------------------------------------------------------------
class A:
	def foo(self):
		print("hola")

print("collatz(255): " + str(collatz(255)))
invoke(A(), "foo")

p = PuntosPartido()
p.inserta(1, "Fernando Martin")
p.inserta(15, "Petrovic")
p.ponCanasta(1)
p.ponCanasta(15)
p.ponFalta(15)
print(p.getInfo(1))
print(p.getInfo(15))
print("Saving as JSON...")
#p.save("partido.json")
#p = None

#print("Loading JSON...")
#p = PuntosPartido.load("partido.json")
#print(p.getInfo(1))
#print(p.getInfo(15))
