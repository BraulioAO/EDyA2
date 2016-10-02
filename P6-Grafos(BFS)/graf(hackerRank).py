import sys

class vertex:
	def __init__(self,i):
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]

	def agregarvecinos(self,v):
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
			self.vertices[a].agregarvecinos(b)
			self.vertices[b].agregarvecinos(a)

	def imprimirGrafica(self):
		print("Grafica: ")
		print("Vertice--Vecinos")
		for v in self.vertices:
			print(self.vertices[v].id, "\t", self.vertices[v].vecinos)
	
    #Breadth First Search
	def BFS(self,r):
		if r in self.vertices:
			cola=[]
			cola.append(r)
			self.vertices[r].visitado=True
			self.vertices[r].nivel=0
			print("({}, {})".format(self.vertices[r].id,self.vertices[r].nivel))
			while(len(cola)>0):
				act=cola[0]
				cola=cola[1:]
				for vec in self.vertices[act].vecinos:
					if self.vertices[vec].visitado == False:
						cola.append(vec)
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel = self.vertices[act].nivel + 1
						print("({}, {})".format(self.vertices[vec].id,self.vertices[vec].nivel))

class main:
    entrada = []
    g = graph()
    for line in sys.stdin.readlines():
        line = line.replace('[','') 
        line = line.replace(']','') 
        line = line.split(',')      
        line = list(map(int, line)) 
        entrada.append(line)
        
    for nodo in entrada[0]:
        g.agregarVertice(nodo)
      
    for cont in range(len(entrada[1])//2):
        g.agregarArista(entrada[1][2*cont],entrada[1][2*cont+1])
    
    g.BFS(entrada[2][0])