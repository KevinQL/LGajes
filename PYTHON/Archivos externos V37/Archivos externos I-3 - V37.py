from io import open


texto_archivo = open("archivo.txt","a") ## abriendo en memoría

texto_archivo.write("\nFIN de los tiempos")

texto_archivo.close()

