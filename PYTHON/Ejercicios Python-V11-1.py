
"""
	Ejercicio 1:
	• Crea un programa que pida dos números por teclado.
	  El programa tendrá una función llamada “DevuelveMax” encargada de devolver
	  el número más alto de los dos introducidos.
"""


def DevuelveMax(num1, num2):

	if num1>num2:
		resultado = str(num1) + " es mayor"
	elif num1 == num2:
		resultado = "Son iguales"
	else:
		resultado = str(num2) + " es mayor"

	return resultado


num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))

print(DevuelveMax(num1,num2))