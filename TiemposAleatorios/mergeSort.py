comps = 0  #Se establece una variable global para llevar las comparaciones

#Función que que compara el primer elemento de las listas y los reordena en otra auxiliar
def merge(lista1,lista2): 
	global comps
	listaAux=[]

	while( len(lista1)> 0 and len(lista2) > 0):
		comps+=1
		if( lista1[0] < lista2[0]):
			listaAux.append(lista1[0])
			lista1=lista1[1:]
		else:
			listaAux.append(lista2[0])
			lista2=lista2[1:]

	while(len(lista1)>0):
		listaAux.append(lista1[0])
		lista1=lista1[1:]

	while(len(lista2)>0):
		listaAux.append(lista2[0])
		lista2=lista2[1:]

	return listaAux

#Funcion para subdividir una lista de entrada
def mergeSortRec(lista):
	global comps
	if( len(lista) == 1 ):
		return lista
	
	listaIzq = lista[ :len(lista)//2]
	listaDer = lista[ len(lista)//2:]

	listaIzq = mergeSortRec(listaIzq)
	listaDer = mergeSortRec(listaDer)

	return merge(listaIzq,listaDer)

def mergeSort(lista):
	global comps
	mergeSortRec(lista)
	aux = comps
	comps = 0
	return aux

	