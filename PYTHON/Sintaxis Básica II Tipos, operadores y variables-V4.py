Python 3.4.4rc1 (v3.4.4rc1:04f3f725896c, Dec  6 2015, 17:06:10) [MSC v.1600 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 5+7
12
>>> 10%3 ##MODULO
1
>>> 3**2 ##POTENCIA
9
>>> 9//2   ##DIVISÓN ENTERA
4
>>> name = "keivn quspe lima"
>>> name 
'keivn quspe lima'
>>> NAME
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NAME' is not defined
>>> mi_nombre = "tu nombre"
>>> mi_nombre
'tu nombre'
>>>  ##contenedor y contenido
... 
>>> 
>>> ## variables, operadores(aritméticos, etc). tipos de datos. 
... 
>>> type(name)
<class 'str'>
>>> 
>>> num = 4
>>> type(num)
<class 'int'>
>>> num = 2.3
>>> type(num)
<class 'float'>
>>> mensaje = """esto es un mensaje 
... con tres saltos 
... de linea """
>>> 
>>> mensaje
'esto es un mensaje \ncon tres saltos \nde linea '
>>> ### las tres comilla para realizar saltos de linea
... 
>>> 
>>> print(mensaje)
esto es un mensaje 
con tres saltos 
de linea 
>>> 
>>> 
>>> 
>>> numero1=5
>>> numero2=6
>>> 
>>> if numero1>numero2:
... print("num1 es mayor")
  File "<stdin>", line 2
    print("num1 es mayor")
        ^
IndentationError: expected an indented block
>>> if numero1>numero2:
... 	print("num1 is high")
... 
>>> 
>>> if numero1>numero2:
... 	print(numero1 is high)
... else:
... 	print(num2 is high)
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
NameError: name 'num2' is not defined
>>> if numero1>numero2:
... 	print("num2 is high!")
... else:
... 	print("numero1 is high")
... 
numero1 is high
>>> ## operadores de comparación, asignación
... 
>>> 
>>> 