"""

	HERENCIA: Uso de dos funciones más utilizadas en python
		super()
		isinstance(9)


	Vocabulario:
		principio de sustentación ::: clasPadre "Es siempre un/a" clasHija ## isinstance(objeto, Clase)

"""



class Persona():
	def __init__(self, nombre, edad, lugarResidencia):
		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion(self):
		print("NOMBRE:",self.nombre, "\nEDAD:", self.edad, "\nRESIDENCIA:", self.lugarResidencia)


class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre, edad, ciudad):
		super().__init__(nombre, edad, ciudad)
		self.salario = salario
		self.antiguedad = antiguedad
	
	def descripcion(self):
		super().descripcion()
		print("SALARIO:",self.salario,"\nANTIGÜEDAD:",self.antiguedad, "años",end="\n***\n")



Kevin = Empleado(2500, 15,     "Kevin",22,"Andahuaylas")

Kevin.descripcion()


print(isinstance(Kevin, Empleado))
### True
print(isinstance(Kevin, Persona))
### True
