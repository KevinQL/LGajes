"""
5) 	Pide números y mételos en una lista, cuando el usuario meta
	un 0 ya dejaremos de insertar. Por último, muestra los números
	ordenados de mayor a menor.

"""




def mayor_numero_lista(lista):
	numL = len(lista)
	numN = 0
	numero_mayor = 0
	val = False

	for x in lista:
		if numL-1 == lista.index(x):
			val = True
			continue

		for i in lista:
			if x >= i:
				numN = numN + 1
		if numN == numL:
			numero_mayor = x
			break
		numN = 0
	else:
		if val:
			numero_mayor = lista[numL-1]

	return numero_mayor


"""
"""

lista_numeros = []
while True:
	numero = int(input("INGRESE NÚMERO: "))
	if numero == 0:
		print("EL PROGRAMA FINALIZÓ!!!")
		break
	lista_numeros.append(numero)

otraLista = []

for x in range(len(lista_numeros)):
	mayor = mayor_numero_lista(lista_numeros)

	otraLista.append(mayor)
	lista_numeros.remove(mayor)

print(otraLista[:])
	

	

