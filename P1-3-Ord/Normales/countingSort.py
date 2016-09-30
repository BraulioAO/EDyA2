def counting(l):
	min = l[0]
	max = min
	for i in range(len(l)):
		if min>l[i]:
			min = l[i]
		if max<l[i]:
			max = l[i]
	print("minimo: ", min)
	print("maximo: ",max)
	rango = max - min + 1

	#print(l)

	ocu = [0 for i in range(rango)]
	#print(ocu)	

	for i in range(len(l)):
		ocu[l[i]-min] += 1

	#print(ocu)

	for i in range(len(ocu)-1):
		ocu[i+1] = ocu[i] + ocu[i+1]

	#print(ocu)

	s = [0 for i in range(len(l))]
	
	for i in range(len(l)-1,-1,-1):
		ocu[l[i]-min]-=1
		s[ocu[l[i]-min]]=l[i]

	return s


print(counting([3,9,10,4,4,50,102]))
