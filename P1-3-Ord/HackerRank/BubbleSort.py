import sys

comps = 0

def bubbleSort(l):
	global comps
	for j in range( len(l)-1 ):
		for i in range( len(l)-1-j):
			comps+=1
			if( l[i] > l[i+1] ):
				aux = l[i]
				l[i] = l[i+1]
				l[i+1]= aux
	
	return l

for line in sys.stdin:
    line = line.split(',')      #separar en un arr de letras
    line = list(map(int, line)) #y mappearlos o cast a enteros
    comps = 0
    print (bubbleSort(line))
    print(comps)