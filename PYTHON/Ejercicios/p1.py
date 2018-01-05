"""
hola! necesito codificar cadenas en base a un diccionario, 
es decir si tengo el diccionario {1:’h’, 2:’o’, 3:’l’, 4:’a’}
 e ingreso la cadena ‘hola’ me devuelva como resultado ‘1234’, 
 intenté hacerlo con un for ” in ”: …print (), pero creo no va por ahí, 
 y la verdad es que soy bastante novata en esto de la programación. 
 Espero puedan ayudarme pronto! Gracias!!!

"""

diccionario = {1:'h', 2:'o', 6:'l', 4:'a'}

letra = []
numeros = []

letra = diccionario.values()

numeros = diccionario.keys()

codigo = []
ingreso = "hola"

for i in ingreso:
	if i in letra:
		for x in numeros:
			if i == diccionario[x]:
				codigo.append(x)
				break;

print(codigo)
