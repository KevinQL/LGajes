"""
	Serialización de colecciones, objetos.

	Bibliotecas necesarias:
		Pickle
			Método dump(): volcado de datos al fichero binario externo.
			Método load(): carga de los datos del fichero binario externo.


"""

import pickle

lista_nombres=["Pedro", "Ana", "María", "Isabel"]

fichero_binario = open("lista_nombres","wb")  ## wb(escritura binaria)

pickle.dump(lista_nombres, fichero_binario)  ## la información de la lista lo volcamos al fichero en memoria

fichero_binario.close()  ## cerramos el fichero en memoria

del(fichero_binario) ## borrando de la memoria