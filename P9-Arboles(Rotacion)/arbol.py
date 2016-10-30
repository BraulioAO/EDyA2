class vertex:
	def __init__(self,v):
		self.id = v
		self.padre = None
		self.hizq = None
		self.hder = None
		self.altura = -1

class arbol:
	def __init__(self):
		self.raiz = None

	def agregar(self,act, ver):
		if act.id < ver.id:
			if act.hder != None:
				self.agregar(act.hder,ver)
			else:
				act.hder = ver
				ver.padre = act
		else:
			if act.hizq != None:
				self.agregar(act.hizq,ver)
			else:
				act.hizq = ver
				ver.padre = act
		
	def agregarVertice(self,v):
		ver = vertex(v)
		if self.raiz == None:
			self.raiz = ver
		else:
			self.agregar(self.raiz, ver)

	def crearArbol(self,listVer):
		for i in range(len(listVer)):
			self.agregarVertice(listVer[i])

	def imprimir(self,act):	#recorrido infix
		if act != None:
			self.imprimir(act.hizq)
			if act.padre == None:
				x = None
			else:
				x = act.padre.id
			print("({}, {}, {})".format(act.id,act.altura,x))
			self.imprimir(act.hder)

	def imprimirDesv(self,act,arrDesv = []):
		if act != None:
			self.imprimirDesv(act.hizq,arrDesv)
			if act.hizq != None and act.hder != None and abs(act.hizq.altura - act.hder.altura) > 1:
				#print(act.id)
				arrDesv.append(act.id)
			elif (act.hizq == None and act.hder != None) and act.hder.altura > 0:
				#print(act.id)
				arrDesv.append(act.id)
			elif (act.hizq != None and act.hder == None) and act.hizq.altura > 0:
				#print(act.id)
				arrDesv.append(act.id)
			self.imprimirDesv(act.hder,arrDesv)
		return arrDesv

	def altura(self,act):	#Recorrido postorden
		if act != None:
			a1 = self.altura(act.hizq)
			a2 = self.altura(act.hder)
			#print(max([a1,a2]))
			act.altura = max([a1,a2]) + 1
			return act.altura
		else:
			return -1

	def RR(self,act,n):	#Rotacion a la derecha
		print("act: ", act.id)
		if (act.hizq != None) and act.id == n :
			nr = act.hizq	#nr = Nodo Referencia
			act.hizq = nr.hder
			nr.hder = act
			nr.padre = act.padre
			act.padre = nr 
			if act.hizq != None:
				act.hizq.padre = act
			if nr.padre != None:
				if nr.padre.hizq != None:
					nr.padre.hder = nr
				else:
					nr.padre.hizq = nr
			if self.raiz == act:
				self.raiz = nr
		else:
			if act.hizq != None and act.hder != None:
				self.RR(act.hizq,n)
				self.RR(act.hder,n)
			elif act.hizq != None and act.hder == None:
				self.RR(act.hizq,n)
			elif act.hizq == None and act.hder != None:
				self.RR(act.hder,n)

	def LR(self,act,n):	#Rotacion a la izquierda
		print("act: ", act.id)
		if (act.hder != None) and act.id == n :
			nr = act.hder	#nr = Nodo Referencia
			act.hder = nr.hizq
			nr.hizq = act
			nr.padre = act.padre
			act.padre = nr 
			if act.hder != None:
				act.hder.padre = act
			if nr.padre != None:
				nr.padre.hder = nr
			if self.raiz == act:
				self.raiz = nr
		else:
			if act.hizq != None and act.hder != None:
				self.LR(act.hizq,n)
				self.LR(act.hder,n)
			elif act.hizq != None and act.hder == None:
				self.LR(act.hizq,n)
			elif act.hizq == None and act.hder != None:
				self.LR(act.hder,n)


		

class main:
	t = arbol()
	u = arbol()
	
	#t.crearArbol([5, 25, 17, 94, 43, 50, 18, 60, 51, 82])
	#t.crearArbol([23, 54, 89, 39, 13, 56, 36, 75, 14, 27])
	#t.crearArbol([8, 14, 27, 30, 4, 9])
	t.crearArbol([20,10,25,8,15,6])
	#t.crearArbol([7,2,1,5,4,6,8])
	print("\n*****ALTURAS*****")
	t.altura(t.raiz)
	t.imprimir(t.raiz)
	print("*****NODOS DESVALANCEADOS*****")
	print(t.imprimirDesv(t.raiz,[]))

	print("\n***ROTACION IZQUIERDA***")
	t.LR(t.raiz,int(input()))
	t.altura(t.raiz)
	t.imprimir(t.raiz)
	print("*****NODOS DESVALANCEADOS*****")
	print(t.imprimirDesv(t.raiz,[]))
	"""
	print("\n***ROTACION IZQUIERDA***")
	t.LR(t.raiz, int(raw_input()))
	t.altura(t.raiz)
	t.imprimir(t.raiz)
	print("*****NODOS DESVALANCEADOS*****")
	print(t.imprimirDesv(t.raiz,[]))
	"""




#							23
#					13				54
#				14				39			89
#							36			56
#						27					75


