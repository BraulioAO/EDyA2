comps = 0

def heapify_rec(list,i):
	global comps
	if(2*i+1 <= len(list)-1):
		comps+=1
		if(list[2*i] < list[2*i+1]):
			max = 2*i+1
		else:
			max = 2*i
           
		comps+=1
		if (list[i] < list[max]):
			aux       = list[i]
			list[i]   = list[max]
			list[max] = aux
			heapify_rec(list,max)
            
	elif (2*i <= len(list)-1):
		comps+=1
		if(list[i] < list[2*i]):
			aux		  = list[i]
			list[i]	  = list[2*i]
			list[2*i] = aux
			heapify_rec(list,2*i)
	
	return list

def heapSort(list):
	for i in range(len(list)//2,0,-1 ): #Formacion del MaxHeap
		list = heapify_rec(list,i)
	
	list3 = []
	for i in range(0, len(list)-1): #Reordenamiento en lista auxiliar
		aux = list[1]
		list[1] = list[len(list)-1]
		list3.append(aux)
		list = list[:len(list)-1]

		list = heapify_rec(list,1)

	return list3


archivo = open("ListaDeArreglos.txt", "r")

for line in archivo.readlines():
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.split(',')
	line = list(map(int, line))
	print(line)
	line.insert(0,0)
	comps = 0
	print(heapSort(line))
	print("No. de comparaciones: ", comps)
	print("Tamaño de la lista: ", len(line)-1, "\n")

archivo.close()