import sys

class vertex:
	def __init__(self,i):
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]
		self.costo=99999999
		self.orden=-1
		self.anterior=-1
	def agregarVecinos(self,v): 
		if v[0] not in self.vecinos:
			self.vecinos.append(v)

#Clase "graph" para la creacion de una "Grafica"
class graph:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self,v): 
		if v not in self.vertices:
			vert = vertex(v)
			self.vertices[v]=vert

	def agregarArista(self,a,b,p): 
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecinos([b,p])

	def minimoCosto(self,l):
		m = self.vertices[l[0]].costo
		v=l[0]
		for e in l:
			if m>self.vertices[e].costo:
				m=self.vertices[e].costo
				v=e
		return v

	def dijkstra(self,a,b):
		lista=[]
		self.vertices[a].costo = 0
		for v in self.vertices[a].vecinos:
			self.vertices[v[0]].costo = v[1]
			self.vertices[v[0]].anterior = self.vertices[a].id
			lista.append(v[0])

		while(len(lista)>0):
			m=self.minimoCosto(lista)

			for vec in self.vertices[m].vecinos:
				if self.vertices[m].costo + vec[1] < self.vertices[vec[0]].costo:
					self.vertices[vec[0]].costo = self.vertices[m].costo + vec[1]
					self.vertices[vec[0]].anterior = self.vertices[m].id

				if self.vertices[vec[0]].visitado == False:
					lista.append(vec[0])

			lista.remove(m)
			self.vertices[m].visitado = True

		v = self.vertices[b]
		if(v.costo == 99999999):
			print("No existe camino")
		else:
			while v.anterior != -1:
				lista.insert(0,v.id)	
				v = self.vertices[v.anterior]
			lista.insert(0,v.id)
			print(lista)
			print(self.vertices[b].costo)


class main:
	entrada = []
	g=graph()

	for line in sys.stdin.readlines():
		line = line.replace('[','')
		line = line.replace(']','')
		line = line.replace('(','')
		line = line.replace(')','')
		line = line.split(',')
		line = list(map(int, line)) 
		entrada.append(line)

	vertices = entrada[0]
	aristas = entrada[1]
	datos = entrada[2]
	
	for vertice in vertices:
		g.agregarVertice(vertice)
	for cont in range(len(aristas)//3):
		g.agregarArista(aristas[3*cont],aristas[3*cont+1],aristas[3*cont+2])
    
	g.dijkstra(datos[0],datos[1])