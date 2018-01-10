"""
	Lanzamiento de excepciones
		Instrucción Raise
		Creación de excepciones propias (POO)

"""

import math


def evaluaEdad(edad):

	if edad < 0:
		raise ZeroDivisionError("No se permiten edades negativas!!") ## tenemos que definir clases para los errores

		return "Eres joven"
	elif edad < 40:
		return "Eres mayor"
	elif edad < 100:
		return "Eres cocho" 
	else:
		return "Eres inmortal"


def calculaRaiz(num1):

	if num1 < 0:
		raise ValueError("El número no puede ser negativo!!")
	else:
		return math.sqrt(num1)




#print(evaluaEdad(-18))  
## ERROR



try:
	print(calculaRaiz(-144))
except ValueError as ErrorDeNumNegativo:  ## el 'as' nos permite nombrar
	print(ErrorDeNumNegativo)
print("PROGRAMA TERMINADO!!!")
### El número no puede ser negativo!!
### PROGRAMA TERMINADO!!!

