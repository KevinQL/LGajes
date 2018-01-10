"""
	
	Excepciones: Error en ejecución.
		Son errores que ocurren durante la ejecución del programa. La sintaxis del 
		código es correcta pero durante la ejecución a ocurrido "algo inesperado"

		Este tipo de errores de ejecución se pueden controlar para que la ejecución
		del programa continué. Es lo que se conoce como manejo o control de excepciones.	


"""


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
	try:
		return num1/num2
	except ZeroDivisionError:
		return "Operación errónea"


op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("""Introduce la operación a realizar :\nsuma(1)
resta(2)\nmultiplica(3)\ndivide(4)\n: """)

if operacion=="suma" or operacion == "1":
	print(suma(op1,op2))

elif operacion=="resta" or operacion == "2":
	print(resta(op1,op2))

elif operacion=="multiplica" or operacion == "3":
	print(multiplica(op1,op2))

elif operacion=="divide" or operacion == str(4):
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")