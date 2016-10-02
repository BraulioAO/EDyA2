import sys
orden = 0

class vertex:
	def __init__(self,i):
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]
		self.orden=-1
	def agregarVecinos(self,v): 
		if v not in self.vecinos:
			self.vecinos.append(v)

class graph:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self,v):
		if v not in self.vertices:
			vert = vertex(v)
			self.vertices[v]=vert

	def agregarArista(self,a,b):
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecinos(b)

	def DFStopo(self,r,n=0): # Depth First Search (Busqueda por profundidad)
		global orden
		if r in self.vertices:
			self.vertices[r].visitado=True
			self.vertices[r].nivel = n
			for v in self.vertices[r].vecinos:
				if self.vertices[v].visitado == False:
					self.DFStopo(v,n+1)
			self.vertices[r].orden = orden
			orden -= 1
			print("({}, {})".format(self.vertices[r].id, self.vertices[r].orden))

	def topoSort(self): #Inducir un orden topologico
		global orden
		orden = len(self.vertices)
		for v in self.vertices:
			if	self.vertices[v].visitado==False:
				self.DFStopo(v)
class main:
	entrada = []
	g = graph()
	for line in sys.stdin.readlines():
		line = line.replace('[','')
		line = line.replace(']','')
		line = line.split(',')
		line = list(map(int,line))
		entrada.append(line)

	vertices = entrada[0]
	aristas = entrada[1]

	for nodo in vertices:
		g.agregarVertice(nodo)
	for cont in range(len(aristas)//2):
		g.agregarArista(aristas[2*cont],aristas[2*cont+1])    

	g.topoSort()