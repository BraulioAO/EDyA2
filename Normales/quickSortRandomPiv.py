import time
import random

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

def quickSort(list):
    if(len(list) <= 1):
        return list

    pivRand  = random.randint(0,len(list)-1)
    aux =  list[len(list)-1]
    list[len(list)-1] = list[pivRand]
    list[pivRand] = aux

    piv = len(list)-1
    retorno = reacomodo(list,piv)
    list = retorno[0]
    piv = retorno[1]

    li = quickSort(list[:piv])
    ld = quickSort(list[piv+1:])
    li.append(list[piv])

    return li[:] + ld[:]


archivo = open("ListaDeArreglos.txt", "r")

for line in archivo.readlines():
    line = line.replace('[','') #recibimos un String y para volverlo
    line = line.replace(']','') #arreglo tenemos que elimiar esos chars
    line = line.split(',')      #para despues separar en un arr de letras
    line = list(map(int, line)) #y mappearlos o cast a enteros
    comps = 0
    print(quickSort(line))
    print("No. de comparaciones: ", comps)
    print("Tamaño de la lista: ", len(line), "\n")

archivo.close()