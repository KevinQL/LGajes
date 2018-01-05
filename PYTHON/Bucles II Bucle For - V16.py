

for x in range(4):
	print(x,end="")
	### 0123

print()


for i in range(3,7):
	print("",i, end="")
	###  3 4 5 6


print()


for i in range(0,10,2):
	print("",i, end="")
	###  0 2 4 6 8


print()


## EJERCICIO SIMPLE
respuesta = False
email = "unajmakev@gmail.com"

for i in range(len(email)):
	if email[i]=="@":
		respuesta = True
		
if respuesta:
	print("Email CORRECTO")
else:
	print("email INCORRECTO")



