"""
8) 	Crea una tupla con números, pide un numero por teclado
	e indica cuantas veces se repite.


"""

def CantidadRepetidas(tupla,numero):
	cantidad = 0

	for x in tupla:
		if numero == x:
			cantidad = cantidad + 1

	return cantidad



numeros = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)

while True:
	numero = int(input("INGRESE NÚMERO: "))
	if numero == 0:
		print("PROGRANA FINALIZÓ")
		break
	else:
		cantidad = CantidadRepetidas(numeros,numero)
		print("SE REPITE: " + str(cantidad))
