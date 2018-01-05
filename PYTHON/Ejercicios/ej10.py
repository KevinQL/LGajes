"""

10) Crea un diccionario donde la clave sea el nombre 
del usuario y el valor sea el teléfono (no es necesario validar).
 Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere
  insertar mas. No se podrán meter nombres repetidos.

"""


registro = {}
usuario = ""
telefono = 0

while True:
	msj = input("OPCIONES: \n(1) INGRESAR REGISTRO. \n(2) SALIR.\n: ")
	if msj == "1":
		usuario = input("INGRESE USUARIO: ")
		telefono = int(input("INGRESE TELÉFONO: "))
		registro[usuario] = telefono
	elif msj == "2":
		print("EL PROGRAMA FINALIZÓ")
		break

print(registro)



	