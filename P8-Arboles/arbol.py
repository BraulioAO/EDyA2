arb = [0,1,6,3,7,9,4,8,19,None,None,10]
lista_infix = []
lista_prefix = []
lista_postfix = []

def hijos(p):
	if len(arb)-1 >= 2*p+1 and arb[2*p] != None and arb[2*p+1] != None:
		return 3		#tiene ambos hijos
	elif len(arb)-1 >= 2*p+1 and arb[2*p+1] != None:
		return 2		#tiene solo hijo derecho
	elif len(arb)-1 >= 2*p and arb[2*p] != None:
		return 1		#tiene solo hijo izquierdo
	elif arb[p] != None:
		return 0		#No tiene hijos
	else:
		return -1		#En posicion p es nulo

def crecer(i):
	j = (i-len(arb))+1
	for l in range(j):
		arb.append(None)

def decrecer():
	global arb
	while(arb[len(arb)-1]==None):
		arb = arb[:len(arb)-1]

def insertar(v,p): #(valor,posicion)
	if p == len(arb):		#Si la posicion es igual al tam del arbol
			arb.append(v)
	elif p < len(arb):		#La posicion es menor que el tam del arbol
		if hijos(p) == 1 or hijos(p) == 3:	#Si tiene hijo izquierdo o ambos
			aux = arb[p]
			arb[p] = v
			insertar(aux,2*p)
		elif hijos(p) == 2:		#Si tiene hijo derecho
			arb[2*p] = arb[p]
			arb[p] = v
		elif hijos(p) == 0:		#Si no tiene hijos
			crecer(2*p)
			arb[2*p] = arb[p]
			arb[p] = v
		elif hijos(p) == -1:	#Si la posicion es 'None' estando dentro del tam del arbol
			if arb[p//2] != None:	#Si tiene nodo padre la posicion
				arb[p] = v
			else:
				print("Posicion invalida")
	else:
		print("Posicion invalida")

def eliminar(p):
	if p < len(arb):	#Si la posicion esta dentro del arbol
		if hijos(p) == 0:		#Si no tiene hijos la posicion
			arb[p] = None
		elif hijos(p) == 1 or hijos(p)==3:	#Si tiene hijo izquierdo o ambos
			arb[p] = arb[2*p]
			eliminar(2*p)
		elif hijos(p) == 2: 	#Si solo tiene hijo derecho
			arb[p] = arb[2*p+1]
			eliminar(2*p+1)
	else:
		print("La posicion no existe")
	decrecer()

def infix(p = 1):
	if 2*p < len(arb):
		if arb[2*p] != None:
			infix(2*p)
	#print(arb[p])
	lista_infix.append(arb[p])
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			infix(2*p+1)

def prefix(p=1):
	lista_prefix.append(arb[p])
	if 2*p < len(arb):
		if arb[2*p] != None:
			prefix(2*p)
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			prefix(2*p+1)

def postfix(p=1):
	if 2*p < len(arb):
		if arb[2*p] != None:
			postfix(2*p)
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			postfix(2*p+1)
	#print(arb[p])
	lista_postfix.append(arb[p])


infix()
prefix()
postfix()
print("Arbol binario: ", arb[1:])
print("Recorrido INFIX: ", lista_infix)
print("Recorrido PREFIX: ", lista_prefix)
print("Recorrido POSTFIX: ", lista_postfix)
lista_infix = []
lista_prefix = []
lista_postfix = []


print("\n\nINSERCIONES Y ELIMINACIONES EN EL ARBOL")
#print(arb)
insertar(99,11)
insertar(88,9)
insertar(33,18)
insertar(23,19)
#print(arb)
insertar(1,12)
insertar(44,13)
#print(arb)
eliminar(22)
eliminar(1)
eliminar(1)
eliminar(1)
eliminar(8)
#print(arb)
print("Nuevo arbol: ", arb[1:])
infix()
prefix()
postfix()
print("Recorrido INFIX: ", lista_infix)
print("Recorrido PREFIX: ", lista_prefix)
print("Recorrido POSTFIX: ", lista_postfix)


