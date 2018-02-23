from io import open


archivo_texto=open("archivo.txt","r+")

#archivo_texto.write("COMIENZO PYTHON")

lista_texto = archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluida desde código \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto) ## esta instrucción pide como parametro una lista


print(archivo_texto.readlines())


archivo_texto.close()

