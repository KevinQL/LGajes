
## pythoon es CASE SENSITIVE
## se hacen uso de las funciones lower() y upper()


print("ASIGNATURAS OPCIONALES PARA EL AÑO 2018")
print("ASIGNATURAS: INFORMÁTICA GRÁFICA - PRUEBAS DE SOFTWARE  - USABILIDAD Y ACCESIBILIDAD")

opcion = input("INGRESE ASIGNATURA: ")

asignatura = opcion.upper()  ## lower() -> MINUSCULAS /// upper() -> MAYUSCULAS 

if asignatura in ["INFORMÁTICA GRÁFICA","PRUEBAS DE SOFTWARE","USABILIDAD Y ACCESIBILIDAD",0]:   ## () ó []
	print("Matricula abierta para " + asignatura)
else:
	print("ASIGNATURA NO CONTEMPLADA!")