"""
	SUNATAXIS

	while condicion:
		cuerpo_bucle

"""

import math   ## inportando librería


edad = int(input("INGRESE EDAD: "))

while edad<0:
	print("Ingrese una edad correcta")
	edad = int(input("INGRESE EDAD: "))

print("Tu edad es ",edad)





## PROGRAMA MATEMÁTICO

numero = int(input("INGRESE NÚMERO PARA RAÍZ: "))
intentos = 1;

while numero<1:
	print("LE SOBRAN " + str(3-intentos) + " INTENTOS")
	numero = int(input("INGRESE NÚMERO PARA RAÍZ: "))
	if intentos == 2:
		break;
	intentos= intentos+1 

if intentos<2 or numero>0:
	raiz = math.sqrt(numero)
	print("La raís de " + str(numero) + " es " + str(raiz))
else:
	print("Se acabaron sus intentos. Valor inoperable para raiz")



