"""

11) Crea una tupla con valores ya predefinidos del 1 al 10,
	pide un índice por teclado y muestra los valores de la tupla.

"""
lista = []
tupla = ()

for x in range(10):
	lista.append(x+1)

print(lista[:])

tupla = tuple(lista)

while True:
	indice = int(input("INGRESE ÍNDICE: "))
	if indice in tupla:
		break
	else:
		print("INGRESE INDICE VÁLIDO")

print("VALOR DEL ÍNDICE " + str(indice) + " " + " ES: " + str(tupla[indice]))
