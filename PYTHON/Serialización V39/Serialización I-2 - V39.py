import pickle

fichero=open("lista_nombres","rb")  ## leer binario

lista = pickle.load(fichero)   ## cargar la información

print(lista)

fichero.close()