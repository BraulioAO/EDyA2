import sys
lista_infix = []
lista_prefix = []
lista_postfix = []

def infix(p = 1):
	if 2*p < len(arb):
		if arb[2*p] != None:
			infix(2*p)
	lista_infix.append(arb[p])
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			infix(2*p+1)

def prefix(p=1):
	lista_prefix.append(arb[p])
	if 2*p < len(arb):
		if arb[2*p] != None:
			prefix(2*p)
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			prefix(2*p+1)

def postfix(p=1):
	if 2*p < len(arb):
		if arb[2*p] != None:
			postfix(2*p)
	if 2*p+1 < len(arb):
		if arb[2*p+1] != None:
			postfix(2*p+1)
	lista_postfix.append(arb[p])


for line in sys.stdin:
    line = line.replace('[','').replace(']','').split(',')
    line = list(map(int,line))

arb = line
infix()
prefix()
postfix()

print(lista_infix)
print(lista_prefix)
print(lista_postfix)