"""
	nueva instrucción : yield from
	
	UTILIDAD:
	+ Simplificar el código de los generadores en el caso de utilizar bucles nidados.

"""


def devuelveCiudadades(*ciudades):  ## *-> la función recibirá un número indeterminado de elementos. Será en forma de tupla
	for elem in ciudades:
		yield from elem



cuidades_devueltas = devuelveCiudadades("Perú","Brasil","Ecuador")

print(next(cuidades_devueltas))
### P

print(next(cuidades_devueltas))
### e

print(next(cuidades_devueltas))
### r

print(next(cuidades_devueltas))
### ú
