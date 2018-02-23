
from io import open


archivo_texto=open("archivo.txt","r+") ## Lectura y escritura

archivo_texto.seek(len(archivo_texto.readline()))  ## se ubica después de la primera linea de texto

print(archivo_texto.read())