import sys
def hijos(p):
	if len(arb)-1 >= 2*p+1 and arb[2*p] != None and arb[2*p+1] != None:
		return 3		#tiene ambos hijos
	elif len(arb)-1 >= 2*p+1 and arb[2*p+1] != None:
		return 2		#tiene solo hijo derecho
	elif len(arb)-1 >= 2*p and arb[2*p] != None:
		return 1		#tiene solo hijo izquierdo
	elif arb[p] != None:
		return 0		#No tiene hijos

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
	decrecer()


arb = []
entrada = []
for line in sys.stdin.readlines():
    line = line.replace('[','').replace(']','').split(',')
    line = list(map(int,line))
    entrada.append(line)

arb = entrada[0]
valorIns = entrada[1][0]
posIns = entrada[1][1]
posElim = entrada[2][0]

insertar(valorIns,posIns)
eliminar(posElim)

print(arb)