"""
	
	self: hace referencia a la instancia perteneciente a la clase 

"""


class Coche():
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enMarcha = False

	def arrancar(self):
		self.enMarcha = True

	def estado(self):
		if self.enMarcha:
			return "El coche está en marcha"
		else:
			return "El coche está parado"


miCoche = Coche()	## Instanciar una clase. No new


print("El largo del coche es: ",miCoche.largoChasis)
### El largo del coche es:  250
print("El cohce tiene ",miCoche.ruedas," ruedas")
### El cohce tiene  4  ruedas

print(miCoche.estado())
### El coche está parado

miCoche.arrancar()
print(miCoche.estado())
### El coche está en marcha

