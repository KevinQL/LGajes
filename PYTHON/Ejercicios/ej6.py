"""

6) Pide una cadena por teclado, mete los caracteres en una lista sin espacios.

"""

def eliminarEspacios(letra):
	ListaCaracteres = []
	for i in letra:
		if i == " ":
			continue
		ListaCaracteres.append(i)
	return ListaCaracteres



letra = input("INGRESE LETRA: ")
listaC = []

listaC = eliminarEspacios(letra)
print(listaC[:])