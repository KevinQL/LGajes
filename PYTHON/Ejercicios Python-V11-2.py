
"""
	Ejercicio 2:
		* Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
		  Esos tres datos deberán ser almacenados en una lista y mostrar en consola 
		  el mensaje: “Los datos personales son: nombre apellido teléfono”
		  (Se mostrarán los datos introducidos por teclado).
"""


nombre = input("Ingrese NOMBRE: ")
direccion = input("Ingrese DIRECCIÓN: ")
tfno = int(input("Ingrese TELEFONO: "))

L_Datos = [nombre,direccion,tfno]

print("Los datos personales son:")
print("NOMBRE: " + L_Datos[0])
print("DIRECCIÓN: " + L_Datos[1])
print("TELEFONO: " + str(L_Datos[2]))