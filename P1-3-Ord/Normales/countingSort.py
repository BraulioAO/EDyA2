def counting(l):
	min = l[0]
	max = min
	for i in range(len(l)): #Encuentra el elemento menor y mayor
		if min>l[i]:
			min = l[i]
		if max<l[i]:
			max = l[i]
	print("minimo: ", min)
	print("maximo: ",max)
	rango = max - min + 1
	print("Tamaño Arr Ocu: ", rango)
	#print(l)

	ocu = [0 for i in range(rango)] #Arreglo de ocurrencias en ceros
	#print(ocu)	

	for i in range(len(l)): #Conteo de las ocurrencias
		ocu[l[i]-min] += 1
	#print(ocu)

	for i in range(len(ocu)-1): #Suma del arreglo de ocurrencias
		ocu[i+1] = ocu[i] + ocu[i+1]
	#print(ocu)

	s = [0 for i in range(len(l))] #Arreglo Auxiliar
	for i in range(len(l)-1,-1,-1): #Reacomodo
		ocu[l[i]-min]-=1
		s[ocu[l[i]-min]]=l[i]

	return s


archivo = open("ListaDeArreglos.txt", "r")

for line in archivo.readlines():
	line = line.replace('[','')
	line = line.replace(']','')
	line = line.split(',')
	line = list(map(int, line))
	print(line)
	print(counting(line))
	print("Tamaño de la lista: ", len(line), "\n")

archivo.close()

