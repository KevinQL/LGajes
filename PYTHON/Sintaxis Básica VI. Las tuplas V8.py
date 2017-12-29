##
##
## 	Las tuplas son listas inmutables, es decir, no se pueden modificar después de su creación
## 		No permiten añadir, eliminar, mover elementos etc (no append, extend, remove)
## 		Si permiten extraer porciones, pero el resultado de la es una tupla nueva
##		no permiten búsquedas (no index). "ANTES DE LAS VERSIONES PYTHON 2.6 O .7"
##		Si permiten comprobar si un elemento se encuentra en la tupla
##	¿Qué utilidad o ventaja tienen respecto a las listas?
##		más rápidas
##		menos espacios (mayor optimización)
##		Formatean Strings
##		Pueden utilizarse como claves en un diccionario. (Las listas NO)
##
##	Sintaxis de las tuplas
##		nombreLista = (elem1, elem2, elem3,...)
##		Se pueden omitir las parentesis



miTupla = ("kevin", "quispe","lima",21,False)
print(miTupla[:])
### ('kevin', 'quispe', 'lima', 21, False)
print(miTupla)
### ('kevin', 'quispe', 'lima', 21, False)


print(miTupla[0])
### kevin


miLista=list(miTupla)	## convirtiendo Tupla en Lista
print(miLista)
### ['kevin', 'quispe', 'lima', 21, False]


tuTupla = tuple(miLista)	## convierte de Lista a Tupla
print(tuTupla)
###	('kevin', 'quispe', 'lima', 21, False)


print("kevin" in miTupla)
### True
print("lalalsa" in miTupla)
### Flase


print(miTupla.count(21))		## cuantas veces se encuentra un elemento
### 1


print(len(miTupla))		## CUANTOS elementos posee la tupla. Distinto de indices
###	5


laTupla = ("unico",)## tuplas UNITARIAS. sin la coma(,) no es tupla UNITARIA
print(laTupla)
### ('unico',)
print(len(laTupla))
### 1



tupla2 = "leo",2,21,True  ## tupla prescindiendo de las parentesis. "EMPAQUETADO DE TUPLA"
print(tupla2)
### ('leo', 2, 21, True)


tupla3 = ("kevin",22,9,1996) 		
nombre, dia, mes, agno = tupla3		## "DES-EMPAQUETADO DE TUPLA"
print(nombre)
### kevin
print(dia)
### 22
print(mes)
### 9
print(agno)
### 1996



print(miTupla.index("quispe"))  ##versión resiente si funciona
### 1

