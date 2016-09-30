def radix(l):
	max = 0
	for i in l:  #Determinar el numero mayor
		if(len(i)>max):
			max = len(i)
	#print(max)
	
	for i in range(len(l)):  #Normalizacion del arreglo
		while(len(l[i])<max):
			l[i] = "0"+l[i]
	#print(l)

	for j in range(max-1,-1,-1):
		ocu=[0 for i in range(10)] #Arreglo ocurrencias en ceros

		for i in range(len(l)): #Conteo de ocurrencias
			ocu[ int(l[i][j]) ] +=1
		#print(ocu)

		for i in range(9): #Suma arreglo de ocu
			ocu[i+1] = ocu[i] + ocu[i+1]
		#print(ocu)

		s = [0 for i in range(len(l))] #Arreglo auxiliar

		for i in range(len(l)-1,-1,-1):  #Reacomodo en arr aux
			ocu[ int(l[i][j]) ] -= 1
			s[ ocu[ int(l[i][j]) ]] = l[i]

		l = s
		#print(l)
	return l

arr = ["1","4","10","100","2","40","100","252","323","99"]
print(arr)
arrOrd = radix(arr)
#print(arrOrd)
arrOrd = list(map(int,arrOrd))
print(arrOrd)

