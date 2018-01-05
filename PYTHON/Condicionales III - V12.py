"""
	CONFIGURACIÓN PARA EJECUTAR "Python-RUN current file"
	#### Preferents/ Key Bindings - user
	# agregar este códgio y guardas:	
	---
		{ "keys": ["ctrl+alt+b"],"command":"run_existing_window_command","args":
		{
			"id":"repl_python_run",
			"file":"config/Python/Main.sublime-menu"	
		}}
	---	

	#### ctrl+alt+b -> abrir 
	#### ctrl+w 	-> cerrar

"""


## 	la instrucción SWITCH, no existe en python.
##  hay otras alternativas. 
##		Concatenación de operadores de comparación.
## 		Operadores lógicos "and" y "or".
## 		Operador "in".



edad = -7

if 0<edad<100:		## Concatenación de operadores
	print("BIEN")
else:
	print("MAL")

### MAL




salario_presidente = int(input("Introduce salario presidente"))
print("Salario presidente: "+ str(salario_presidente))

salario_director = int(input("Introduce salario director"))
print("Salario director: "+ str(salario_director))

salario_jefe_area = int(input("Introduce salario jefe_area"))
print("Salario jefe_area: "+ str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario admiinistrativo"))
print("Salario administrativo: "+ str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo correcto")
else:
	print("Algo falla en la empresa")









