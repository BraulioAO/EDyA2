# -*- coding: utf-8 -*-

def busquedaBinaria(l,clave):
	#print(len(l),clave)
	#print(l)

	if(len(l) <= 1): #Caso Base con lista de tamaño uno o vacia
		if(clave == int(l[0][0])): 
			return l[len(l)//2-1]
		return None

	if(clave == int(l[len(l)//2-1][0]) ): #Clave igual a la media
		return l[len(l)//2-1]

	if(clave > int(l[len(l)//2-1][0])):	#Lista a la derecha de la media
		valor = busquedaBinaria(l[ len(l)//2:],clave)

	if(clave < int(l[len(l)//2-1][0])):	#Lista a la izquierda de la media
		valor =	busquedaBinaria(l[:len(l)//2],clave)

	return valor

archivo = open("lista.txt","r", encoding='utf-8')
la = []
for linea in archivo.readlines():
	tupla = linea.split("\t")
	tupla[2] = tupla[2].replace("\n","")
	la.append(tupla)

print(busquedaBinaria(la,int(input("Ingrese la clave a buscar: "))))
#for cont in range(-5,45):
#	print(busquedaBinaria(la,cont))
archivo.close()
