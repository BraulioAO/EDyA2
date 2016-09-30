import sys

def radix(l):
	max = 0
	for i in l:  #Determinar el numero mayor
		if(len(i)>max):
			max = len(i)
	
	for i in range(len(l)):
		while(len(l[i])<max):
			l[i] = "0"+l[i]

	for j in range(max-1,-1,-1):
		ocu=[0 for i in range(10)] #Arreglo ocurrencias inicializado en 'cero'

		for i in range(len(l)): #Conteo de ocurrencias
			ocu[ int(l[i][j]) ] +=1

		for i in range(9):  #Suma arreglo ocu
			ocu[i+1] = ocu[i] + ocu[i+1]

		s = [0 for i in range(len(l))]

		for i in range(len(l)-1,-1,-1):  #Reacomodo en el nuevo arreglo
			ocu[ int(l[i][j]) ] -= 1 
			s[ ocu[ int(l[i][j]) ] ] = l[i]

		l = s

	return l

for line in sys.stdin:
    line = line.replace('[','') #recibimos un String y para volverlo
    line = line.replace(']','') #arreglo tenemos que elimiar los caracteres '[ ]'
    line = line.split(',')      #para despues separar en un array de strings
    arr= radix(line)
    arr = list(map(int,arr)) #Se hace cast a enteros
    print(arr)
  
    
