

print("PROGRAMA DE BECAS AÑO 2018")

distancia_escuela=int(input("DISTANICIA EN KM : "))
print(str(distancia_escuela)+"KM")

numero_hermanos=int(input("NÚMERO DE HERMANANOS: "))
print(numero_hermanos)

salario_familiar = int(input("SALARIO FAMILIAR: "))
print(str(salario_familiar) + " SOLES")


if distancia_escuela>40 and numero_hermanos>2 or salario_familiar <= 4000:  ## de izquierda a derecha
	print("Tienes derecho a una BECA")
else:
	print("No tienes derecho a BECA")