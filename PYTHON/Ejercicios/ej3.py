"""
3) Pide un numero por teclado y guarda en una lista su tabla de multiplicar
 hasta el 10. Por ejemplo, si pide el 5 la lista 
 tendrá: 5,10,15,20,25,30,35,40,45,50

"""

numero = int(input("INGRESE NÚMERO: "))

multiplos = []  ## necesario crear lista

for x in range(1, 11):
	multiplos.append(numero*x)

print(multiplos[:])