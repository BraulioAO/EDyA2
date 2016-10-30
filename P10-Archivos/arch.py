"""
try:
	a = open("/users/edaII08/edaII08alu02/Escritorio/P10/hola.txt", "rb")
	lista = a.readlines()
	print(lista)
except:
	print("Error al abrir el archivo")

print("Continua el programa")
"""
"""
with open('hola.txt','r') as archivo:
	for l in archivo:
		print(l)

archivo = open('hola.txt','w+')
cadena = "hola"
archivo.write(cadena+"\n")
"""

archivo = open('hola.txt','r+')
l = archivo.readlines()
print(l)
print(archivo.tell())	#Obtener la posicion de lect/esc
archivo.seek(archivo.tell()) #moverse a cierta posicion
archivo.write("Cadena nueva")
