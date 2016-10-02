#Clase "vertex" para la creación de "vertices o nodos" de una grafica
class vertex:
	def __init__(self,i):
		self.id=i
		self.visitado=False
		self.nivel=-1
		self.vecinos=[]
	def agregarvecinos(self,v): 
		if v not in self.vecinos:
			self.vecinos.append(v)
	#def eliminarvecinos(self,v):

#Clase "graph" para la creacion de una "Grafica"
class graph:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self,v): #Agrega un vertice a la grafica
		if v not in self.vertices:
			vert = vertex(v)
			self.vertices[v]=vert

	def agregarArista(self,a,b): #Agrega una arista entre dos vertices
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarvecinos(b)
			self.vertices[b].agregarvecinos(a)
		else:
			print("no se pudo agregar arista")
	def imprimirGrafica(self):
		print("Grafica: ")
		print("Vertice--Vecinos")
		for v in self.vertices:
			print(self.vertices[v].id, "\t", self.vertices[v].vecinos)

	def BFS(self,r): 	#Breadth First Search (Busqueda por expanción)
		if r in self.vertices:
			print("Busqueda por expansion: ")
			print("(vertice, nivel)")
			cola=[]
			cola.append(r)
			self.vertices[r].visitado=True
			self.vertices[r].nivel=0
			print("({0:3d}, {1})".format(self.vertices[r].id, self.vertices[r].nivel))
			while(len(cola)>0):
				act=cola[0]
				cola=cola[1:]	#cola.remove(0)
				for vec in self.vertices[act].vecinos:
					if self.vertices[vec].visitado == False:
						cola.append(vec)
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel = self.vertices[act].nivel + 1
						print("({0:3d}, {1})".format(self.vertices[vec].id,self.vertices[vec].nivel))
		else:
			print("El vertice no existe")

	def caminoMasCorto(self,s,f):
		self.BFS(f)
		aux = s
		print("\nEl camino mas corto es por los vertices: ")
		if(self.vertices[s].nivel > 0):
			print(self.vertices[s].id)
		else:
			print("No existe camino")

		while(self.vertices[aux].nivel > 0):
			for v in self.vertices[aux].vecinos:
				if self.vertices[v].nivel < self.vertices[aux].nivel:
						print(self.vertices[v].id)
						aux = self.vertices[v].id	

class main:
	nodos = [45, 84, 169, 64, 21, 155, 83, 52, 22, 162, 27, 110, 60, 154, 128, 181, 114]
	vertices = [[84, 128], [60, 169], [169, 60], [27, 52], [154, 155], [162, 84], [128, 60], 
	[162, 181], [154, 155], [60, 114], [21, 181], [27, 52], [52, 155], [155, 52], [110, 60], 
	[110, 114], [64, 84], [114, 22], [45, 22], [114, 162], [169, 22], [83, 110], [181, 60], 
	[154, 181], [169, 110], [110, 169]]
	g = graph()
	
	for n in nodos:
		g.agregarVertice(n)
	for v in vertices:
		g.agregarArista(v[0],v[1])

	g.imprimirGrafica()	
	g.caminoMasCorto( int(input("\nCamino del vertice: ")), int(input("al vertice: ")) )
	#g.BFS( int(input("Vertice para Busqueda por extención: ")) )



