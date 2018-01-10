"""
	Captura de varias Excepciones
	Claúsula finally 

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

while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))

		if op2 == 0:
			print("división entre cero. resultado infinito")
			continue

		break		
	except ValueError:
		print("Los valores introducidos no son correctos")

	
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