

## paso de parámetros y argumentos en funciones

## aumentar tamño de letra "Ctrol+ruedaRatón"
## principal utilidad de función. reutilización de código

## Error al intentar crear dos funciones con el mismo nombre y diferentes números de argumentos.
## Para python, paso de valor siempre por referencia. 


##-------------------------------------




def suma():		##función suma dos números
	num1=5
	num2=3
	print(num1+num2)


def suma2(num1, num2):		##función suma con parámetros
	print(num1+num2)


def suma3(num1, num2):		##función suma con return
	resultado = num1 + num2
	return resultado



suma()		##llamando función suma

suma2(2,4)	
suma2(2,123)
suma2("hola", "adios")	

resultado =suma3(23,4) 
print(resultado)
