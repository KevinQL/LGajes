"""
	
	Punteros en texto, dentro de un fichero de texto

	Método.
		seek(5) : posiciona el puntero o cursor después del caracter 5

"""

from io import open


archivo_texto=open("archivo.txt","r")

print(archivo_texto.read())

## en este punto, el puntero está en el último caracter
archivo_texto.seek(0)

print(archivo_texto.read(11))  ## hace una lectura hasta el caracter 11

print("----------",archivo_texto.read())

archivo_texto.close()