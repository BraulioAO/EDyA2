import random
import time

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
	for i in range(len(list)//2,0,-1 ):
		list = heapify_rec(list,i)
	
	list3 = []
	for i in range(0, len(list)-1):
		aux = list[1]
		list[1] = list[len(list)-1]
		list3.append(aux)
		list = list[:len(list)-1]

		list = heapify_rec(list,1)

	return list3

def timeElapsed(arr):            #Función para obtener los tiempos de ejecución
    global comps 
    comps = 0
    start_time = time.time()
    heapSort(arr)           #Se envia la lista a ordenar
    elapsed_time = time.time() - start_time
    print("Tam_list: ", len(arr), "\tTiempo[s]: ", float("{0:.12f}".format(elapsed_time)), "\tComparaciones: ", comps)
    
        
lista = []                      #Lista donde se guardaran los números generados aleatoriamente
for veces in range(1, 11):                     #veces de iteraciones (1, n+1)
    for cont in range(500*veces):                # elementos por iteracion (5,10,15,....5*veces)
        lista.append(random.randrange(-1000, 1000))     #muestreo en rango
    timeElapsed(lista)                  #llamar función de tiempos de ejecucion
    lista = [] #Vacia la lista