"""
	Guardar datos de forma permanente en ficheros


"""

import pickle


class Persona:
	"""docstring for Persona"""
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona ",self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
	personas = []

	def __init__(self):
		listaDePersonas = open("ficheroExterno","ab+") ## ab+(Agregar información binaria)
		listaDePersonas.seek(0)

		try:
			self.personas = pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero está vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)


	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guaradarPersonaEnFicheroExterno()

	def mostrarPersonas(self):
		for x in self.personas:
			print(x)
	
	def guaradarPersonaEnFicheroExterno(self):
		listaDePersonas = open("ficheroExterno","wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)
	
	def eliminarPersona(self, codigo):
		#personax = []
		i = 0
		for nombre in self.personas:
			if codigo in str(nombre).split():
				self.personas.pop(i)
				print("entro",i)
			i = i + 1
		self.guaradarPersonaEnFicheroExterno()




miLista = ListaPersonas()

"""
persona = Persona("Kevin","M",30)
miLista.agregarPersonas(persona)
"""

miLista.eliminarPersona("Kevin")

miLista.mostrarPersonas()