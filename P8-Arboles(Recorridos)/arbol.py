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

def crecer(i):			#i = 2*i, sería hijo izquierdo
	j = (i-len(arb))+1	#Solo incrementamos las casillas necesarias
	for l in range(j):	#Para que len(arb) == 2*p y así
		arb.append(None)	#tener lugar para el hijo izquierdo

def decrecer():
	global arb
	while(arb[len(arb)-1]==None):
		arb = arb[:len(arb)-1]
#Recorremos el arreglo de derecha a izquierda eliminando los "None"
#hasta encontrar algun valor, de esa manera no tenemos mas "none"
#al final del arbol los cuales desperdiciarian memoria

def insertar(v,p): #(valor,posicion)
	if p == len(arb):		#Si la posicion es igual al tam del arbol
			arb.append(v)	#Solo se inserta al final de la lista

	elif p < len(arb):		#La posicion es menor que el tam del arbol
		if hijos(p) == 1 or hijos(p) == 3:	#Si tiene hijo izquierdo o ambos
			aux = arb[p]  	#Elemento que se desplazara
			arb[p] = v 		#Elemento insertado
			insertar(aux,2*p)
			#Ahora se inserta el elemento desplazado de manera
			#recursiva hasta que quede en una hoja el nodo 
			#desplazado y solo entre al primer If o al ultimo ELIF

		elif hijos(p) == 2:		#Si tiene solo hijo derecho
			arb[2*p] = arb[p]	#Ahora tiene hijo izquierdo :)
			arb[p] = v 			#Y no tuvimos que desplazar nada

		elif hijos(p) == 0:		#Si no tiene hijos
			crecer(2*p)			#Para evitar salirnos del rango se crece el arreglo
			arb[2*p] = arb[p]	#El padre pasa a ser hijo izquierdo
			arb[p] = v 			#y el insertado a ser padre

		elif hijos(p) == -1:	#Si la posicion es 'None' estando dentro del tam del arbol
			if arb[p//2] != None:	#Si tiene nodo padre la posicion
				arb[p] = v 			#Se inserta al elemento
			else:					#En caso de no tener padre no se inserta
				print("Posicion invalida")
	else:
		print("Posicion invalida")

def eliminar(p):
	if p < len(arb):	#Verificamos si la posicion esta dentro del arbol
		if hijos(p) == 0:		#Si no tiene hijos la posicion
			arb[p] = None 		#solo lo eliminamos
		elif hijos(p) == 1 or hijos(p)==3:	#Si tiene hijo izquierdo o ambos
			arb[p] = arb[2*p] 	#El izquierdo pasa a ser padre y aplicamos recursividad
			eliminar(2*p)		#hasta que llegaremos a entrar al primer if	
							
		elif hijos(p) == 2: 	#Si solo tiene hijo derecho
			arb[p] = arb[2*p+1]  #Ese hijo pasa a ser padre y aplicamos de
			eliminar(2*p+1)		 #nuevo recursividad
	else:
		print("La posicion no existe")
	decrecer() #Cuando termina la reasignacion se limpian los None al final del arreglo

def infix(p = 1):  #Recorrido infix(izq,raiz,der)
	if 2*p < len(arb):	      #Si la posicion 2*p esta dentro del arbol
		if arb[2*p] != None:  #y esta no es 'None'
			infix(2*p)	      #se llama recursivamente a infix con la nueva posicion 2*p
	lista_infix.append(arb[p])#recorriendo de esta forma al arbol iniciando por los hijos izq.
	#print(arb[p])	          #cuando ya no se cumple lo anterior, se imprime el elemento
	if 2*p+1 < len(arb):	  #y ahora se verifica si la posicion 2*p+1 esta dentro del arbol,
		if arb[2*p+1] != None:#si esta no es 'None'
			infix(2*p+1)	  #se llama recursivamente a infix pero con la posicion 2*p+1

def prefix(p=1):	#Recorrido prefix(raiz,izq,der)
	lista_prefix.append(arb[p])	#Ahora primero se imprime la raiz
	#print(arb[p])				#y posteriormente se manda a llamar recursivamente la funcion
	if 2*p < len(arb):			#logrando que el orden de impresion del arbol sea raiz, izq, der.
		if arb[2*p] != None:
			prefix(2*p)
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			prefix(2*p+1)

def postfix(p=1):	#Recorrido postfix(izq,der,raiz)
	if 2*p < len(arb):			#Se llama primero de forma recursiva a la funcion
		if arb[2*p] != None:	#Y hasta el final es donde se imprime el valor	
			postfix(2*p)		#logrando que el orden de impresion del arbol sea izq, der, raiz.
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			postfix(2*p+1)
	lista_postfix.append(arb[p])
	#print(arb[p])



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


