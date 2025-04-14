from tkinter import *
#funciones de procesamiento
def procesar():
    Saludo = "Hola: " + nombre.get() + ", tu edad es: " + str(2025 - edad.get())
    etiqueta_respuesta.config(text=Saludo)  # Actualiza el texto del Label

#Instancia de la clase Tk
ventana = Tk()
ventana.title('Saludador')

#Variables que almacenarán los datos
nombre = StringVar()
edad = IntVar()

#generación de widgets
#nombre
etiqueta_nombre = Label(ventana, text='Nombre:')
entrada_nombre = Entry(ventana, textvariable=nombre)
etiqueta_nombre.grid(row=1, column=1)
entrada_nombre.grid(row=1, column=2)

#edad
etiqueta_edad = Label(ventana, text='Año de nacimiento: ')
entrada_edad = Entry(ventana, textvariable=edad)
etiqueta_edad.grid(row=2, column=1)
entrada_edad.grid(row=2, column=2)

#Respuesta
etiqueta_respuesta = Label(ventana, text='', fg='blue')  # Etiqueta para la respuesta
etiqueta_respuesta.grid(row=3, column=1, columnspan=2)

#boton
boton = Button(ventana, text='Procesar', command=procesar, width=20)
boton.grid(row=6, column=1, columnspan=2)

#ejecución de ventana
ventana.mainloop()