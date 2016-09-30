comps = 0

#Separa en elementos mayores y menores respecto al pivote
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
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.split(',')
    line = list(map(int, line))
    comps = 0
    print(line)
    print(quickSort(line))
    print("No. de comparaciones: ", comps)
    print("Tamaño de la lista: ", len(line), "\n")

archivo.close()