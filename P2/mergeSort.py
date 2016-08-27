import random
import time

comps = 0  #Se establece una variable global para llevar las comparaciones

#Función que que compara el primer elemento de las listas y los reordena en otra auxiliar
def merge(lista1,lista2): 
    global comps
    listaAux=[]

    while( len(lista1)> 0 and len(lista2) > 0):
        comps+=1
        if( lista1[0] < lista2[0]):
            listaAux.append(lista1[0])
            lista1=lista1[1:]
        else:
            listaAux.append(lista2[0])
            lista2=lista2[1:]

    while(len(lista1)>0):
        listaAux.append(lista1[0])
        lista1=lista1[1:]

    while(len(lista2)>0):
        listaAux.append(lista2[0])
        lista2=lista2[1:]

    return listaAux

#Funcion para subdividir una lista de entrada
def mergeSort(lista):
    if( len(lista) == 1 ):
        return lista
    
    listaIzq = lista[ :len(lista)//2]
    listaDer = lista[ len(lista)//2:]

    listaIzq = mergeSort(listaIzq)
    listaDer = mergeSort(listaDer)

    return merge(listaIzq,listaDer)

def timeElapsed(arr):            #Función para obtener los tiempos de ejecución
    global comps 
    comps = 0
    start_time = time.time()
    mergeSort(arr)           #Se envia la lista a ordenar
    elapsed_time = time.time() - start_time
    print("Tam_list: ", len(arr), "\tTiempo[s]: ", float("{0:.12f}".format(elapsed_time)), "\tComparaciones: ", comps)
    
        
lista = []                      #Lista donde se guardaran los números generados aleatoriamente
for veces in range(1, 11):                     #veces de iteraciones (1, n+1)
    for cont in range(500*veces):                # elementos por iteracion (5,10,15,....5*veces)
        lista.append(random.randrange(-1000, 1000))     #muestreo en rango
    timeElapsed(lista)                  #llamar función de tiempos de ejecucion
    lista = [] #Vacia la lista