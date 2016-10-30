import os

def crearDirectorio(ruta):
	try:
		os.makedirs(ruta)
	except OSError:
		print("El directorio ya existe")
	os.chdir(ruta)


crearDirectorio('/users/edaII08/edaII08alu02/Escritorio/P10/newDir')

dic = {}
a = open("texto.txt","r")

l = a.readlines()
#print(l)
for line in l:
	line = line.replace('\n','').replace(',','').replace('.','').split()
	#print(line)

	for palabra in line:
		#print(palabra)
		if palabra not in dic.keys():
			dic[palabra] = 1
		else:
			dic[palabra]+=1

#print dic
print "\n\n"
print sorted(dic.items(), key=lambda x: x[1])
for pal in dic.keys():
	print(pal)
	archivo = open(pal,'w')
	archivo.write(pal + ' ' + str(dic[pal]))
	archivo.close
