import random
import time

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
    
    piv = len(list)-1
    retorno = reacomodo(list,piv)
    list = retorno[0]
    piv = retorno[1]

    li = quickSort(list[:piv])
    ld = quickSort(list[piv+1:])
    li.append(list[piv])

    return li[:] + ld[:]

def timeElapsed(arr):            #Función para obtener los tiempos de ejecución
    global comps 
    comps = 0
    start_time = time.time()
    quickSort(arr)           #Se envia la lista a ordenar
    elapsed_time = time.time() - start_time

    print("Tam_list: ", len(arr), "\tTiempo[s]: ", float("{0:.12f}".format(elapsed_time)), "\tComparaciones: ", comps)
    
        
lista = []                      #Lista donde se guardaran los números generados aleatoriamente
for veces in range(1, 11):                     #veces de iteraciones (1, n+1)
    for cont in range(500*veces):                # elementos por iteracion (5,10,15,....5*veces)
        lista.append(random.randrange(-1000, 1000))     #muestreo en rango
    timeElapsed(lista)                  #llamar función de tiempos de ejecucion
    lista = [] #Vacia la lista