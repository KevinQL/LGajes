"""
	
	Cómo trabajar con ficheros externos de texto con el MÓDULO IO.

	ARCHIVOS EXTERNOS
		OBJETIVOS: persistencia de datos 
		DOS ALTERNATIVAS:
			Manejo de archivos externos.
			Trabajo con BBDD.

	MANEJO ARCHIVOS EXTERNOS
		Fases necesarios para guardar información en archivos externos.
		CREACIÓN -> APERTURA -> MANIPULACIÓN -> CIERRE


	Abrir documentación - librery referens - io ### para trabajar con el módulo IO
	url = https://docs.python.org/3/library/io.html

	Para usar el método open(). debemos saber que podemos realizar tres actividades:
	lectura, escritura y apppend (para agregar información a un archivo con información ya
	existente)

"""

from io import open

archivo_texto = open("archivo.txt","w") ## abriendo archivo en modo WRITE/ESCRITURA

frase = "Hay tres tristes tigres comuiendo trigo...\ncontinuara..."

archivo_texto.write(frase)


archivo_texto.close()