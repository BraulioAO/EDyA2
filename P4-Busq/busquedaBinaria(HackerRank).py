import sys
def BinarySearch(arr,query,start,end):
    if(start > end):             #Si el inicio de la localidad
        print("False")           #excede el final no se encuentra
        return False

    medium = int((end - start)/2) + start
    arrInt = int(arr[medium][0]) #Evitamos que nuestro IF 
    if(arrInt == query):         # se vea muy amontonado
        return medium
    else:
        arrInt = int(arr[medium][0])
        if(query > arrInt): #Regresamos +1 porque medium ya esta checada
            return BinarySearch(arr,query,medium+1,end)
        else: #Regresamos -1 porque medium ya esta checada
            return  BinarySearch(arr,query,start,medium-1)                      
query = "" 
lista_alumnos = []
for linea in sys.stdin:
    
    tupla = linea.split("\t")
    if(query == ""): #Solo cumple la primera vuelta
        query = tupla[0].replace("\n","")
    
    else:
        tupla[2] = tupla[2].replace("\n","")
        lista_alumnos.append(tupla)

        
lista = lista_alumnos #hacer mas leible la llamada a lafuncion
index = BinarySearch(lista,int(query),0, (len(lista)-1) )
print(lista[index])