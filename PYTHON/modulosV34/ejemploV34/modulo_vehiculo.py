
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


class Furgoneta(Vehiculo):
	
	def carga(self,cargar):
		self.cargado= cargar
		if self.cargado:
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"



class Moto(Vehiculo):  ## Ejemplo de Heredación de la clase padre Vehiculo.
	hcaballito = ""
	def caballito(self):		# métodos propios de la clase Moto
		self.hcaballito = "voy haciendo el caballito"

	def estado(self):		# sobreescritura de ,étodos
		print("Marca: ", self.marca, "\nModelo: ",self.modelo,
			"\nEn Marcha?: ",self.enmarcha,"\nAcelera?: ",self.acelera,
			"\nFrena?: ",self.frena,"\nCaballito: ",self.hcaballito)

class VElectricos(Vehiculo):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia = 100

	def cargaEnergia(self):
		self.cargando = True


class BicicletaElectrica(VElectricos, Vehiculo):	## Ejemplo de Herencia multiple
	pass
		
		

	
