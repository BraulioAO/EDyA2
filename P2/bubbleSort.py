import random
import time

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

def timeElapsed(arr):            #Función para obtener los tiempos de ejecución
    global comps 
    comps = 0
    start_time = time.time()
    bubbleSort(arr)           #Se envia la lista a ordenar
    elapsed_time = time.time() - start_time
    print("Tam_list: ", len(arr), "\tTiempo[s]: ", float("{0:.12f}".format(elapsed_time)), "\tComparaciones: ", comps)
    
        
lista = []                      #Lista donde se guardaran los números generados aleatoriamente
for veces in range(1, 11):                     #veces de iteraciones (1, n+1)
    for cont in range(500*veces):                # elementos por iteracion (5,10,15,....5*veces)
        lista.append(random.randrange(-1000, 1000))     #muestreo en rango
    timeElapsed(lista)                  #llamar función de tiempos de ejecucion
    lista = [] #Vacia la lista

