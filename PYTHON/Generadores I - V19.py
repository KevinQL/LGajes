"""
	GENERADORES

	*	Estructuras que extaren valores de una función y se 
		almacenan en objetos iterables (que se pueden recorrer)
	*	Estos valores se almacenana de uno en uno.
	*	Cada vez que un generador almacena un valor, esta permanece en un
		estado pausado hasta que se solicite el siguiente. Esta caracteristica 
		es conocida como "suspensión de estado"

	PALABRAS CLAVES
	*	yield, objeto generador iterable, generador en suspensión, valor


	GENERADORES ¿QUÉ UTILIDAD TIENEN?
	*	Son más eficientes que las funciones tradicionales.
	*	Muy útiles con listas de valores infinitos
	*	Bajo determinados escenarios, será muy útil que un generador devuelva
		los valores de uno en uno. 

	SINTAXIS

	def generarNumeros():

		yield numero;  	# también se pueden usar return
"""




def generarPares(limite):
	num = 1
	miLista = []

	for x in range(limite):
	 	yield num*2
	 	num += 1


devuelvePares = generarPares(10)

## si usamos un bucle con respecto al generador, da error

print("CÓDGIO-------")
print(next(devuelvePares))
### CÓDGIO-------
### 2

print("CÓDGIO-------")
print(next(devuelvePares))
### CÓDGIO-------
### 4

print("MÁS CÓDGIO-------")
print(next(devuelvePares))
### MÁS CÓDGIO-------
### 6
