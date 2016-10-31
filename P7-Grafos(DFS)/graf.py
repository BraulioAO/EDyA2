orden = 0
#Clase "vertex" para la creación de "vertices o nodos" de una grafica
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

	def agregarVertice(self,v): #Agrega un vertice a la grafica
		if v not in self.vertices:
			vert = vertex(v)
			self.vertices[v]=vert

	def agregarArista(self,a,b,p): #Agrega una arista entre dos vertices y peso
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecinos([b,p]) #Grafica dirigida
			#self.vertices[b].agregarVecinos(a) #Grafica no difiriga
		else:
			print("no se pudo agregar arista")

	def imprimirGrafica(self):
		print("Grafica: ")
		print("Vertice-----Costo--Anterior--OrdTop--Nivel--Vecinos")
		for v in self.vertices:
			x = self.vertices[v]
			print("{:4}{:12d}{:8d}{:9d}{:8d}\t{}".format(x.id, x.costo, x.anterior, x.orden, x.nivel, x.vecinos))

	def DFS(self,r,n=0): # Depth First Search (Busqueda por profundidad)
		if r in self.vertices:
			self.vertices[r].visitado=True
			self.vertices[r].nivel = n
			print(r,n)
			for v in self.vertices[r].vecinos:
				if self.vertices[v[0]].visitado == False:
					self.DFS(v[0],n+1)
		else:
			print("El vertice no existe")
	
	def DFStopo(self,r,n=0): # Depth First Search (Busqueda por profundidad)
		global orden
		self.vertices[r].visitado=True
		self.vertices[r].nivel = n
		for v in self.vertices[r].vecinos:
			if self.vertices[v[0]].visitado == False:
				self.DFStopo(v[0],n+1)
		self.vertices[r].orden = orden
		orden -= 1
		print("({}, {})".format(self.vertices[r].id, self.vertices[r].orden))

	def topoSort(self): #Inducir un orden topologico
		global orden
		orden = len(self.vertices)
		for v in self.vertices:
			#print("vertice: ", v)
			if	self.vertices[v].visitado==False:
				self.DFStopo(v)

	def minimoCosto(self,l):
		m = self.vertices[l[0]].costo
		v=l[0]
		for e in l:
			if m>self.vertices[e].costo:
				m=self.vertices[e].costo
				v=e
		return v

	def dijkstra(self,a,b):
		if a in self.vertices and b in self.vertices:
			lista=[] #quiue
			self.vertices[a].costo = 0
			for v in self.vertices[a].vecinos:
				self.vertices[v[0]].costo = v[1]
				self.vertices[v[0]].anterior = self.vertices[a].id
				lista.append(v[0])
			#print(lista)

			while(len(lista)>0):
				m=self.minimoCosto(lista)

				for vec in self.vertices[m].vecinos:
					if self.vertices[m].costo + vec[1] < self.vertices[vec[0]].costo:
						self.vertices[vec[0]].costo = self.vertices[m].costo + vec[1]
						self.vertices[vec[0]].anterior = self.vertices[m].id
						#print(self.vertices[vec[0]].costo)

					if self.vertices[vec[0]].visitado == False:
						lista.append(vec[0])

				lista.remove(m)
				self.vertices[m].visitado = True
				#print(lista)

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
		else:
			print("No existe camino")


	
class main:
	vertices = [173, 78, 26, 13, 170, 35, 80, 189, 199, 142, 180, 191, 161, 176, 18, 36, 33]
	aristas = [[36, 173, 812], [36, 199, 6665], [173, 78, 8381], [26, 170, 7338], [180, 176, 5786], 
	           [161, 142, 9609], [26, 161, 5308], [80, 170, 6885], [180, 176, 4721], [18, 36, 5593], 
	           [142, 180, 2992], [78, 26, 7615], [36, 33, 762], [18, 33, 8309], [36, 176, 861], 
	           [78, 170, 9476], [161, 78, 66], [176, 199, 81], [173, 180, 2399], [78, 33, 2991], 
	           [170, 26, 6422], [78, 33, 7289], [33, 176, 321], [180, 189, 6621]]

	g=graph()
	for vertice in vertices:
		g.agregarVertice(vertice)
	for arista in aristas:
		g.agregarArista(arista[0],arista[1],arista[2])


	g.imprimirGrafica()
	#g.DFS(int(input()))
	g.topoSort()
	#g.dijkstra(int(input("a:")),int(input("b:")))#170,199
	print("\n")
	g.imprimirGrafica()
	

