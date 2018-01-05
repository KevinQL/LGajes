

print("Verificación de acceso")

edad_usuario = int(input("INGRESE EDAD "))

if edad_usuario<18 and edad_usuario>0:
	print("No puedes pasar :/ ")
elif edad_usuario<60 and edad_usuario>=18:
	print("Puedes pasar :)")
elif edad_usuario <= 100:
	print("No deberías pasar :( ")
else:
	print("La edad no se corresponde a algo lógico :|")



print("EL PROGRAMA HA FINALIZADO")