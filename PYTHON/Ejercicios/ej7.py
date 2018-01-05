"""

7) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.

"""

def almacenarCSR(cadena):

	lista=[]

	for x in cadena:
		if x in lista:
			pass  ## sin el PASS sale ERROR!!
		else:
			lista.append(x)

	return lista

##EJECUTADNDO PROGRAMAA

cadena = input("INGRESE CADENA: ")

print(almacenarCSR(cadena))

