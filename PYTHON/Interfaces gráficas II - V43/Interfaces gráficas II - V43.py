"""

## Documentación Tkinter python
	https://docs.python.org/3/library/tk.html
	Revizando. Handy reference, primera opción: setting options:
		https://docs.python.org/3/library/tkinter.html#setting-options


ESTRUCTURA DE VENTANA Tkinter
	Raíz(Tk)	# tanbién llamdo contenedor
		frame	# tanbién llamdo contenedor
			widgets #Se le denomina a todos. a la raiz, al frame, a todo


"""

from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(True, False) ## por default es true en los dos parámetros

raiz.iconbitmap("../Interfaces gráficas I - V42/kev.ico")

#raiz.geometry("650x350") ## no es necesario porque la raiz se acomoda a las dimesiones del frame

raiz.config(bd="10")  # tamaño borde

raiz.config(relief="groove")

raiz.config(bg="blue")

miFrame = Frame()

miFrame.pack()  # enpaquetando el frame

miFrame.pack(fill="y",side="left") #el frame se expande con respecto a las dimensiones de la raiz

#miFrame.pack(expand=1)

miFrame.config(bg="green")

miFrame.config(width="650", height="350")

miFrame.config(bd="45") # borde

miFrame.config(relief="sunken") # forma de borde. actua con la configuración 'bd="45"'

miFrame.config(cursor="pirate")

raiz.mainloop()



