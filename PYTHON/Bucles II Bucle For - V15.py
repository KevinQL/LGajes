

"""
	BUCLE FOR:
		Recorriendo strings
		Tipo range
		Notaciones espaciales con print


"""




for i in ["kevin","unajma",21]:
	print("hello", end="  ")
	### hello  hello  hello  



for x in "unajmakev@gmail.com":
	print("Hi",end="")
	### HiHiHiHiHiHiHiHiHiHiHiHiHiHiHiHiHiHiHi



print()
print("ES CORREO?")
email = False
correo = "unajmakev@gmail.com"""
for x in ".@":
	if x in correo and 0<correo.count("@") < 2:
		email = True
if email:
	print("SI es un correo")
else:
	print("NO es un correo")




for i in range(5):
	print(i, end="")
	### 01234
	
	