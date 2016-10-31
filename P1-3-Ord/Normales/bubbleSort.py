comps = 0

def bubbleSort(l):
	global comps
	for j in range( len(l)-1 ):
		for i in range( len(l)-1-j):
			comps+=1
			if( l[i] > l[i+1] ):
				aux = l[i]
				l[i] = l[i+1]
				l[i+1] = aux
	
	return l


archivo = open("ListaDeArreglos.txt", "r")

for line in archivo.readlines():
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.split(',')
	line = list(map(int, line))
	comps = 0
	print(line)
	print(bubbleSort(line))
	print("No. de comparaciones: ", comps)
	print("Tamaño de la lista: ", len(line), "\n")

archivo.close()