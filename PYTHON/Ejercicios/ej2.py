"""
2) 	Crea una tupla con los meses del año, pide números al usuario, 
	si el numero esta entre 1 y la longitud máxima de la tupla, muestra
	el contenido de esa posición sino muestra un mensaje de error.

	El programa termina cuando el usuario introduce un cero.

"""


meses = ("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE")


while True:  
	numero = int(input("INGRESE NUMERO DE MES: "))
	if 0<numero<=len(meses):   	## condicional concatenado es un AND
		print("MES " + str(numero) + " " + meses[numero-1])
	elif numero == 0:
		print("EL PROGRAMA FINALIZÓ")
		break
	else:
		print("ERORR en el numero ingresado")
		

		



