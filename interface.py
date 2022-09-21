from tkinter import *

# Inicio de la ventana
raiz = Tk()
# Titulo de la ventana
raiz.title("Interfaz Grafica de Mineria de Datos")
# Fondo azul de la ventana
raiz.config(bg="blue")
# Generamos un frame
miFrame = Frame()
miFrame.pack()
miFrame.pack(side="left")
miFrame.config(bg="red")
miFrame.config(bd=35)
miFrame.config(width="650", height="300")
# Generamos la ventana
raiz.mainloop()