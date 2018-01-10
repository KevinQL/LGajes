"""
	
	La herencia:
		qué es?
			es un mecanismo que nos permitirá traspasar caracteristicas y comportamientos a subclases
		para qué sirve?
			reutilización de código en caso de crear objetos similares
		cómo hacer que las clases hereden?
			Fijar que los objetos(barco, bus, camión, mototaxi) tengan caracteristicas y comportamientos comunes para luego crear una super-clase
			

	Al momento de heredar, solo tenemos que pasar el nombre de la clase padre dentro de los parentesis de la clase hija.


		TERMINOLOGÍAS:
			clase padre, super padre
			subclase. también puede ser super clase

"""


class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo,
			"\nEn Marcha?: ",self.enmarcha,"\nAcelera?: ",self.acelera,
			"\nFrena?: ",self.frena)


class Moto(Vehiculo):  ## Ejemplo de Heredación de la clase padre Vehiculo.
	pass
		


mimoto = Moto("HONDA","CBR")

mimoto.estado()












