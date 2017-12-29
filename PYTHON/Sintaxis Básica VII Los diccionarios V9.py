
## DICCIONARIOS ¿Qué son?
##
"""
	* 	Estructuras de datos que nos permiten almancenar valores de diferentes tipos
		(enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios.

	*	La principal caracteristica de los diccionarios es que los datos se almacenan 
		asociado a una clave de tal forma que se crea una asociación de tipo "CLAVE:VALOR"
		para cada elemento almacenado.
	
	* 	Los elementos almacenados no estás ordenados. El orden es indiferente a la hora de
		almacenar información en un diccionario. 
"""
##



miDiccionario = {"ALEMANIA":"Berlin", "FRANCIA":"Paris", "REINO UNIDO":"Londres", "ESPAÑA":"Madrid"}
print(miDiccionario)
### {'ALEMANIA': 'Berlin', 'REINO UNIDO': 'Londres', 'FRANCIA': 'Paris', 'ESPAÑA': 'Madrid'}

#print(miDiccionario[:])
### TypeError: unhashable type: 'slice'


print(miDiccionario["ALEMANIA"])
###	Berlin
print(miDiccionario["ESPAÑA"])
###	Madrid


miDiccionario["ITALIA"] = "Lisboa"
print(miDiccionario)
### {'REINO UNIDO': 'Londres', 'ESPAÑA': 'Madrid', 'ITALIA': 'Lisboa', 'ALEMANIA': 'Berlin', 'FRANCIA': 'Paris'}

miDiccionario["ITALIA"] = "Roma"  ## sobre escribiendo valor
print(miDiccionario)
###	{'REINO UNIDO': 'Londres', 'ESPAÑA': 'Madrid', 'ITALIA': 'Roma', 'ALEMANIA': 'Berlin', 'FRANCIA': 'Paris'}


del miDiccionario["ITALIA"]  ## Eliminando elemento del diccionario
print(miDiccionario)
### {'ALEMANIA': 'Berlin', 'FRANCIA': 'Paris', 'REINO UNIDO': 'Londres', 'ESPAÑA': 'Madrid'}





miDiccionario = {"NOMBRE":"kevin quispe lima", 1996:"Año nacimiento"}
print(miDiccionario)
### {1996: 'Año nacimiento', 'NOMBRE': 'kevin quispe lima'}






miTupla = ("ALEMANIA", "FRANCIA", "REINO UNIDO", "ESPAÑA")
miDiccionario = {miTupla[0]:"Berlin",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Madrid"}
print(miDiccionario)
### {'REINO UNIDO': 'Londres', 'ESPAÑA': 'Madrid', 'FRANCIA': 'Paris', 'ALEMANIA': 'Berlin'}
print(miDiccionario["FRANCIA"])
### Paris



miDiccionario2 = {"PERSONAX":{"NOMBRE":"X","EDAD":100,"EXISTE":False}, "PERSONA1":["KEVIN",22,9,1996], "PERSONA2":("JHON",13,8,1995)}
print(miDiccionario2)
### {'PERSONA2': ('JHON', 13, 8, 1995), 'PERSONA1': ['KEVIN', 22, 9, 1996], 'PERSONAX': {'NOMBRE': 'X', 'EDAD': 100, 'EXISTE': False}}
print(miDiccionario2["PERSONA1"])
### ['KEVIN', 22, 9, 1996]
print(miDiccionario2["PERSONA2"])
### ('JHON', 13, 8, 1995)
print(miDiccionario2["PERSONAX"])
### {'NOMBRE': 'X', 'EDAD': 100, 'EXISTE': False}
print(miDiccionario2["PERSONAX"]["NOMBRE"])
### X

print(miDiccionario2.keys())
### dict_keys(['PERSONAX', 'PERSONA2', 'PERSONA1'])
print(miDiccionario2.values())
### dict_values([{'EDAD': 100, 'EXISTE': False, 'NOMBRE': 'X'}, ('JHON', 13, 8, 1995), ['KEVIN', 22, 9, 1996]])
print(len(miDiccionario2))
### 3


