
## Ctrl + C 	.- Sale de un bucle infinito

## Continue		.- Pasa al siguiente ciclo. no ejecuta las instrucciones después de esta instrucción
## pass			.- Devuelve un null. es como si el bucle no se ejecutara. NO EXISTIECEN. bucles o clases nulas
## else			.- Tienen misma caracteristica con los eleses condicionales. se ejecutará, siempre que se termine el bucle sin interrupciones (break)



letra = "python"

for x in letra:
	if x=="h":
		continue
	print("viendo letra " + x)

###
"""
viendo letra p
viendo letra y
viendo letra t
viendo letra o
viendo letra n
"""

nombre = "kevin quispe "
contador = 0
for i in nombre:
	if i == " ":
		continue
	contador += 1

print("Caracteres con espacios " + str(len(nombre)))
##Caracteres con espacios 13
print("Caracteres sin espacios " + str(contador))
##Caracteres sin espacios 11


"""

## Un bucle NULO
while True:
	pass  

## Una Clase NULA
class MiClase:
	pass 	# para implementarlo más tarde.

"""




## ELSE. 

mail = "unajmakev@gmail.com"
esMail = False
for i in mail:
	if i == "@":
		esMail = True
		break	## una interrupción como el break, no permite ejecutar el else del FOR
else:
	print("BUCLE terminado sin interrupciones")  ## se ejecuta cada vez que el bucle for termina sin interrupciones. 

print(esMail)