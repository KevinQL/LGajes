from io import open


texto_archivo = open("archivo.txt","r") ## abriendo en memoría

texto = texto_archivo.readlines()	## read()/readlines()

texto_archivo.close()				## cerrando de memoria

print(texto[1],texto[0])
