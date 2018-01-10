"""


	POLIFORMISMO:
		Muchas formas.
		Un objeto puede cambiar de forma dependiendo del contexto donde se utilice, y por lo tanto cambia de omportamiento.
		Puede pasar de ser una clase(camión) a otra clase(moto) dependiendo del contexto.
		python es de tipado dinámico.

"""

class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")


class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")


class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()


miMoto = Moto()
miMoto.desplazamiento()


miCoche = Coche()
miCoche.desplazamiento()


miCamion = Camion()
miCamion.desplazamiento()


print("USO POLIMORFISMO")

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
