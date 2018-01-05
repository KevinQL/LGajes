"""
	1) Mete los valores del 1 al 100 en una lista.
"""

lista = []

for x in range(100): ## x va desde el 0
	lista.extend([x+1]) ## lista.append(num)

mitupla = tuple(lista)

print("Cantidad de elementos: " + str(len(mitupla)))
print(mitupla)