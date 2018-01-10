

def divide():

	try:
		op1=float(input("Introduce primer número: "))
		op2=float(input("Introduce segundo número: "))

		print("La división es: " + str(op1/op2))

	except ValueError:
		print("los valores introducidos son erroneos")
	except ZeroDivisionError:
		print("No se puede dividir entre cero!!!")
	except:		## No se conoce la excepción 
		print("Ha ocurrido un error!!")
	finally:	## La instrucción SIEMPRE se ejecutará
		print("Clausula finally!!")


	print("Cálculo finalizado")


divide()