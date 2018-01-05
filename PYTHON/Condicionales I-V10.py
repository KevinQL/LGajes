## CONFIGURACIÓN
## Correr con consola de teclado. necesario para el valor por teclado
## Tools/ SublimeREPL/ Python/ Python-RUN current file


## Flujo de ejecución.

"""
	* Orden de ejecución de las instrucciones.
	* Bloque de código
	* las CONDICIONALES alteran el orden de ejecución de las instruccíones.	

	* Cualquier cosa que sea introducido por teclado, en python es considerado como TEXTO.
	  Por eso convertimos la entrada texto en un valor numérico. 

	* Ambito de la variable.

"""

print("PROGRAMA NOTA ALUMNOS")
nota_alumno = input("Introduce nota alumno")  # valor por teclado



def evaluacion(nota):
	if nota > 10 and nota <= 20:
		valoracion = "APROBADO"
	else:
		valoracion = "DESAPROBADO"

	return valoracion





print(evaluacion(int(nota_alumno)))  ## la función INT(). permite convertir texto en entero





