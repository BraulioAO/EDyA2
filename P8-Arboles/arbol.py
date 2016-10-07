arb = [0,1,6,3,7,9,4,8,19,None,None,10]

def hijos(p):
#	if p >= len(arb): #Posicion invalida
#		return -1
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
	if p > len(arb):
		print("La posicion no existe")
	elif p == len(arb):
		arb.append(v)
	elif hijos(p) == -1:
		arb[p] = v
	else:
		if hijos(p) == 1 or hijos(p) == 3:
			aux = arb[p]
			arb[p] = v
			insertar(aux,2*p)
		elif hijos(p) == 2:
			aux = arb[p]
			arb[p] = v
			insertar(aux,2*p+1)
		elif hijos(p) == 0:
			crecer(2*p)
			arb[2*p] = arb[p]
			arb[p] = v

def eliminar(p):
	if p < len(arb):	     #if hijos(p) != -1:
		if hijos(p) == 0:
			arb[p] = None
		elif hijos(p) == 1 or hijos(p)==3:
			arb[p] = arb[2*p]
			eliminar(2*p)
		elif hijos(p) == 2:
			arb[p] = arb[2*p+1]
			eliminar(2*p+1)
	else:
		print("Posicion invalida")
	decrecer()

			

print(arb)
insertar(100,10)
insertar(100,10)
insertar(100,10)
insertar(100,10)
print(arb)
eliminar(10)
eliminar(10)
eliminar(10)
eliminar(10)
print(arb)
