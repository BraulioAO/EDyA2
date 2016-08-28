comps = 0

def reacomodo(list,piv):
    global comps
    j=0
    for i in range(0,piv):
        comps+=1
        if (list[i] < list[piv]):
            aux     = list[j]
            list[j] = list[i]
            list[i] = aux
            j+=1
    
    aux       = list[j]
    list[j]   = list[piv]
    list[piv] = aux
    return [list, j] 

def quickSortRec(list):
    if(len(list) <= 1):
        return list
    
    piv = len(list)-1
    retorno = reacomodo(list,piv)
    list = retorno[0]
    piv = retorno[1]

    li = quickSortRec(list[:piv])
    ld = quickSortRec(list[piv+1:])
    li.append(list[piv])

    return li[:] + ld[:]

def quickSort(lista):
	global comps
	quickSortRec(lista)
	aux = comps
	comps = 0
	return aux
