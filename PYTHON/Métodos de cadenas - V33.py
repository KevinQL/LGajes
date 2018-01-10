""""
	

	Uso de métodos de cadenas. objetos String
		upper() - convierte en mayuscula un strings 
		lower() - pasa a minusculas un string
		capitalize() - poner la primera letra en mayuscula 
		count() - contar cuantas veces aparece una letra o cadena dentro de un mensaje, frase
		find() - Representar el índice, la posición de un caracter dentro de un texto
		isdigit() -	true/flase. si el valor introducido es un número o no lo es
		isalum() - true/flase. son alfa numéricos (1,2,...9, A, B, C .... Z)
		isalpha() -	true/flase. si hay solo letras. los espacios no cuentam 
		split() -	Separa por palabras utilizando espacios
		strip() -	borra los espacios sobrantes al principio y al final
		replace() - cambia una palabra o letra por otra, dentro de un string
		rfind() -	representar el indice de un caracter, contando desde atras

	asistir a la siguiente web: 
		http://pyspanishdoc.sourceforge.net/


"""



nombre = "kevin"
apellido = "qUispe LIMA"
edad = "22"
numero = 983677639	# no funcionarán con números


print("------- OBJETO STRING----------")

print(nombre.upper())
### KEVIN

print(apellido.lower())
### quispe lima

print(apellido.capitalize())
### Quispe lima

print(nombre.count("e"))
### 1

print(nombre.find("i"))
### 3


print(edad.isdigit())
### True
print(nombre.isdigit())
### False


print(edad.isalnum())  # los números del 1-9 y las letras del alfabeto son alfanumérico.:D
### True
print(apellido.isalnum()) 	# espacios no cuenta
### False
print(nombre.isalnum()) # no hay espacios
### True


print(apellido.isalpha())  # hay espacio
### False
print(nombre.isalpha())  # No hay espacio
### True
print(edad.isalpha())  # hay número
### False


print(apellido.split("U"))
### ['q', 'ispe LIMA']

palabra = "  espacios final  "
print(palabra)
###   espacios final  
print(palabra.strip())
### espacios final



