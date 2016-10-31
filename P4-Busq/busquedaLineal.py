# -*- coding: utf-8 -*-

def busquedaLineal(lista,key):
	for i in range(len(lista)): #Ciclo para recorrer todas las claves del arreglo
		if( key == int(lista[i][0]) ):	#Compara la 'key' con cada elemento del arreglo
			return lista[i]	 #En caso de coincidencia se retorna los valores en esa clave
	return None					

archivo = open("lista.txt","r", encoding='utf-8')
la = []
for linea in archivo.readlines():
	tupla = linea.split("\t")
	tupla[2] = tupla[2].replace("\n","")
	la.append(tupla)

print(busquedaLineal(la, int(input("Ingrese la clave a buscar: "))))

archivo.close()