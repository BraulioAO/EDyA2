def radix(l):
	max = 0
	for i in l:  #Determinar la palabra mas grande
		if(len(i)>max):
			max = len(i)
    
	for i in range(len(l)): #Normalización de las cadenas
		while(len(l[i])<max):
			l[i] = l[i] + chr(96)  #Normalizamos las cadenas por la derecha. 96 = `, 97 = a, ....

	for j in range(max-1,-1,-1):
		ocu=[0 for i in range(27)] #Arreglo ocurrencias inicializado en 'cero'

		for i in range(len(l)): #Conteo de ocurrencias
			ocu[ ord(l[i][j]) - 96 ] +=1

		for i in range(26):  #Suma arreglo ocu
			ocu[i+1] = ocu[i] + ocu[i+1]

		s = [0 for i in range(len(l))]

		for i in range(len(l)-1,-1,-1):  #Reacomodo en el nuevo arreglo
			ocu[ ord(l[i][j]) - 96 ] -= 1 
			s[ ocu[ ord(l[i][j]) - 96] ] = l[i]

		l = s

	return l

arr= radix(['hola', 'como', 'vi', 'adios', 'bienvenido', 'jaja', 'diminuto', 'bonito','zarzamora'])
arr = list(map(lambda elem: elem.replace(chr(96),''), arr))  #Eliminamos el caracter que usamos para normalizar
print(arr)