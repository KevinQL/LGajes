"""

	Encapsulación de métodos:
		qué es?
		por qué utilizar la encapsulación?


"""

class Coche():

	def __init__(self):			## constructor de la clase
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4		## Encapsulado propiedad. Se podrá modicar sólo desde dentro de la clase
		self.__enMarcha = False

	def arrancar(self, arrancamos):
		self.__enMarcha = arrancamos
		chequeo = self.__chequeo_interno()

		if self.__enMarcha and chequeo:
			return "El coche está en marcha"
		else:
			return "El coche está parado"
		

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
			self.__largoChasis)

	def __chequeo_interno(self):		# Encapsulado método
		print("Realizando chequeo interno")
		self.gasolina = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if self.gasolina == "ok" and self.aceite=="ok" and self.puertas == "cerradas":
			print("Chequeo exitoso")
			return True
		else:
			print("Chequeo NO exitoso")
			return False



miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("---------------- OTRO OBJETO ---------------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.__ruedas = 2 ## No tiene efecto alguno porque la propiedad está encapsulada
miCoche2.estado()


