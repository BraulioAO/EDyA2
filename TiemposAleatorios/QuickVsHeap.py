import random
import time
import quickSortStaticPiv
import quickSortRandomPiv
import heapSort

def timeElapsed(algoritmo, arr):
	start_time = time.time()
	comparaciones = 0
	
	if(algoritmo == "quickStatic"):
		comparaciones = quickSortStaticPiv.quickSort(arr)
	elif(algoritmo == "quickAle"):
		comparaciones = quickSortRandomPiv.quickSort(arr)
	elif(algoritmo == "heap"):
		comparaciones = heapSort.heapSort(arr)
	
	elapsed_time = time.time() - start_time
	print("TamList: ", len(arr), "\tTime: ", elapsed_time, "Comps: ", comparaciones)


archivo = open("ArreglosAleatorios.txt","w+")
noArreglos = int(input("Número de arreglos a crear: ")) #numero de arreglos
tam = int(input("Tamaño de cada arreglo: "))


print("Creando arreglo aleatorios...")
for veces in range(1,noArreglos+1):
	tamArr = tam*veces #tamaño de cada arreglo creciente
	for cont in range(0,tamArr):
		if(cont == 0):
			archivo.write("["+str(random.randrange(-10000,10001))+",")
		elif (cont < tamArr-1):
			archivo.write(str(random.randrange(-10000,10001))+",")
		else:
			archivo.write(str(random.randrange(-10000,10001))+"]\n")
archivo.close()

algoritmos = ["quickStatic","quickAle","heap"]

for algoritmo in algoritmos:
	datos = open("ArreglosAleatorios.txt","r")
	print("\n",algoritmo)
	for line in datos.readlines():
		line = line.replace('[','') #recibimos un String y para volverlo
		line = line.replace(']','') #arreglo tenemos que elimiar esos chars
		line = line.split(',')      #para despues separar en un arr de letras
		line = list(map(int, line)) #y mappearlos o cast a enteros
		timeElapsed(algoritmo,line)
		
datos.close()

