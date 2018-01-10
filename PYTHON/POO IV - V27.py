
"""
	ESTADO INICIAL
		CONSTRUCTOR: Es un método especial que le da estado inicial a los objetos
	

	ENCAPSULAR: Proteger una propiedad o método para que no se pueda modificar desde fuera de la clase
		utilizar __ 


"""

class Coche():

	def __init__(self):			## constructor de la clase
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4		## Encapsulado propiedad. Se podrá modicar sólo desde dentro de la clase
		self.__enMarcha = False

	def arrancar(self, arrancamos):
		self.__enMarcha = arrancamos
		if self.__enMarcha:
			return "El coche está en marcha"
		else:
			return "El coche está parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
			self.__largoChasis)



miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("---------------- OTRO OBJETO ---------------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.__ruedas = 2 ## No tiene efecto alguno porque la propiedad está encapsulada
miCoche2.estado()


