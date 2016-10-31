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


archivo = open("ListaDeArreglos.txt", "r")

for line in archivo.readlines():
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.split(',')
    line = list(map(int, line))
    comps = 0
    print(line)
    print(mergeSort(line))
    print("No. de comparaciones: ", comps)
    print("Tamaño de la lista: ", len(line), "\n")

archivo.close()