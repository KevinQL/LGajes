"""

	
	Cómo crear paquetes distribuibles y reutilizables.

	Instalamos paquete dentro del propio python del s.o para que lo pueda leer y acceder a el 
	desde cualquier sitio.
	Abrimos
		View / Side Bar / show side bar    ## Despliega un mini explorador a la izquierda

	1) Creamos un archivo 'setup.py'. en la carpeta raíz 
	El continido del archivo: descripción del paquete que vamos a distribuir. versión, nombre paquete
	quieres escribieron el paquete, etc. 

	2)Abrimos la LINEA DE COMANDOS en la carpeta raiz donde se encuentra archivo setup.py
		shif + antiClick / abrir linea de comanados en esta ruta.
	3)Luego escribimos:
		> python setup.py sdist 
		Enter
	Instalando. dentro de la carpeta 'dist'
		> pip3/pip install [nombrePaquete.zip]


	Pasos:
		(1) Crear paquetes
		(2) Instalar paquetes

	Desinstalar el paquete: abrimos linea de consola
		> pip3 uninstall [nombre de paquete]. ejemp 'paquetecalculos'
			# > pip uninstall paquetecalculos
		Enter

"""


#from paquetesV35.calculo.redondea_potencia.redondea_potencia import * 
from paquetesV35.calculo.calculos_generales import * 

potencia(2,3)

sumar(3,3)