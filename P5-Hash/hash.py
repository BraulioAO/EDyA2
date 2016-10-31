# -*- coding: utf-8 -*-
import random
A = random.random()

#Función para convertir la cadena de entrada en un número entero
def preHash(cad): 
	salida = ""
	for l in cad:
		salida += str(ord(l))
	return int(salida)

#Función Hash para conversión de llaves
def hashD(cad):
	global m
	k = preHash(cad)
	return int(m*((k*A)%1)) #Hash con metodo de multiplicacion
	#return k % m #Hash con metodo de division

def agregar(cad): #Función para agregar un nuevo elemento
	global ht
	ht[hashD(cad)].append(cad)

def buscar(cad): #Función para buscar un elemento
	global ht
	h = hashD(cad)
	for e in ht[h]:
		if(e == cad):
			return True
		else:
			False

def borrar(cad): #Función para borrar un elemento
	global ht
	if(buscar(cad)==True):
		ht[hashD(cad)].remove(cad)
		return True
	return False
	

m = 10 #tamaño inicial de la tabla
ht = [[] for j in range(m)] #nester list (listas anidadas)
palabras = ["hola", "nuevo", "perro", "perrito", "gato", "estudiante","feo","jaja","arroz","Perro"]
for p in palabras:
	agregar(p)

print("Arreglo de entrada: ", ht)

while(1):
	cad = input("\nIngrese una cadena a borrar: ")
	print(borrar(cad))
	print("Nuevo Arreglo: ", ht)





