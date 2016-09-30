#!/usr/bin/env python
# -*- coding: utf-8 -*-

def BinarySearch(arr,query,start,end):
    if(start > end):
        print("False")
        return False

    medium = int((end - start)/2) + start

    arrInt = int(arr[medium][0])
    if(arrInt == query):
        return medium

    else:
        arrInt = int(arr[medium][0])
        if(query > arrInt):
            return BinarySearch(arr,query,medium+1,end)

        else:
            return  BinarySearch(arr,query,start,medium-1)
           

archivo = open("lista.txt","r")
lista_alumnos = []
for linea in archivo.readlines():
	tupla = linea.split("\t")
	tupla[2] = tupla[2].replace("\n","")
	lista_alumnos.append(tupla)

lista = lista_alumnos #Beautify code 

query = int(input("Ingrese la clave a buscar: "))

index = BinarySearch(lista,query,0, (len(lista)-1) )

print(lista[index])