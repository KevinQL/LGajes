"""
4) 	Pide números y mételos en una lista, cuando el usuario meta
	un 0 ya dejaremos de insertar. Por último, muestra los números
	ordenados de menor a mayor.

"""




def menor_numero_lista(lista):
	numL = len(lista)
	numN = 0
	numero_menor = 0
	val = False

	for x in lista:
		if numL-1 == lista.index(x):
			val = True
			continue

		for i in lista:
			if x <= i:
				numN = numN + 1
		if numN == numL:
			numero_menor = x
			break
		numN = 0
	else:
		if val:
			numero_menor = lista[numL-1]

	return numero_menor


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
	menor = menor_numero_lista(lista_numeros)

	otraLista.append(menor)
	lista_numeros.remove(menor)

print(otraLista[:])
	

	

