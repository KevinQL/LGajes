
##LISTAS EN PYTHON

miLista = ["Kevin","quispe","lima",21,"andahuaylas"]


print(miLista[:])
### ['Kevin', 'quispe', 'lima', 21, 'andahuaylas']

print(miLista[0])
### Kevin

#print(miLista[8])
### Error!!! IndexError: list index out of range

print(miLista[-1])
### andahuaylas 

print(miLista[1:2]) ## desde_inclusivo : hasta_exclusivo
###	['quispe']

print(miLista[2:])
###	['lima', 21, 'andahuaylas']

print(miLista[:2])
###	['Kevin', 'quispe']


miLista.append("PERÚ")  # Agrega un elemento en la última posición
print(miLista[:])
### ['Kevin', 'quispe', 'lima', 21, 'andahuaylas', 'PERÚ']


miLista.insert(2,"MENSAJE##")
print(miLista[:])
### ['Kevin', 'quispe', 'MENSAJE##', 'lima', 21, 'andahuaylas', 'PERÚ']


miLista.extend(["$$$","&&&&"])
print(miLista[:])
### ['Kevin', 'quispe', 'MENSAJE##', 'lima', 21, 'andahuaylas', 'PERÚ', '$$$', '&&&&']


print(miLista.index("MENSAJE##"))
### 2


print("lololo" in miLista)
### False
print("MENSAJE##" in miLista)
###	True



miLista.remove("MENSAJE##")
print(miLista[:])
### ['Kevin', 'quispe', 'lima', 21, 'andahuaylas', 'PERÚ', '$$$', '&&&&']



miLista.pop()		# Elimina el último elemento
print(miLista[:])
### ['Kevin', 'quispe', 'lima', 21, 'andahuaylas', 'PERÚ', '$$$']




tuLista = ["kkkk","ddddd"]
laLista = miLista + tuLista
print(laLista[:])
### ['Kevin', 'quispe', 'lima', 21, 'andahuaylas', 'PERÚ', '$$$', 'kkkk', 'ddddd']



print(tuLista*3)
###	['kkkk', 'ddddd', 'kkkk', 'ddddd', 'kkkk', 'ddddd']
