"""

9) Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.

"""

def mayorNum(tuplaNum):
	num = 0
	mayor = True
	fijar = False

	for x in tuplaNum:
		for i in tuplaNum:
			if fijar:
				continue
			num = x
			if x < i:
				mayor = False
				fijar = True
				#break
		if mayor:
			break
		mayor = True
		fijar = False
	return num

def menorNum(tuplaNum):
	num = 0
	menor = True
	fijar = False

	for x in tuplaNum:
		for i in tuplaNum:
			if fijar:
				continue
			num = x
			if x > i:
				menor = False
				fijar = True
				#break
		if menor:
			break
		menor = True
		fijar = False
	return num


numeros = (1,2,3,4,5,7,8,9,10,1,2,3,4,5,7,8,9,10,0, 100,-34)

print("Mayor numero: "+str(mayorNum(numeros)))
print("Menor numero: "+str(menorNum(numeros)))

