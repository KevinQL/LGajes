"""

12) Crea una lista vacía (pongamos 10 posiciones),
	pide sus valores y devuelve la suma y la media de los números.

"""


lista = []
suma = 0
for x in range(3):
	numero = int(input("INGRESE NÚMERO: "))
	lista.extend([numero])

for x in lista:
	suma += x

promedio = suma / len(lista)

print("PROMEDIO: " + str(promedio))