from tkinter import ttk
from tkinter import *

class Haze:
    def __init__(self, window):
        # Inicio

        #ancho y alto de la ventana
        ancho = 800
        alto = 600

        #Asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #Asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #Opción para centrar el contenido 
        self.wind.columnconfigure(0, weight=1)

        #Damos un titulo a la ventana
        self.wind.title('División')

        #Creamos un contenedor
        frame = LabelFrame(self.wind, text = 'División de 2 valores que no contengan 0', background= "pink")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Creamos un etiqueta
        Label(frame, text = 'Ingrese su Primer Número: ', background="pink").grid(row = 1, column = 0)

        #Creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        #De la misma manera que la forma anterior una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Ingrese su Segundo Número: ', background ="pink").grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #Creamos un botón para ejecutar la Division
        Button(frame, text = 'Presione para Dividir', background ="lightblue", command = self.dividir).grid(row = 3, columnspan = 2, sticky = W + E)
        #Colocamos un área para mensajes
        self.message = Label(text = '', fg = 'blue', background= "pink")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    #Creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0

    #Esta es la función que ejecuta la división
    def dividir(self):
        if(float(self.var2.get()) == 0):
            self.message['text'] = 'No es posible dividir por 0.'
        else:    
            if self.validation():
                resultado = float( self.var1.get() ) / float( self.var2.get() )
                resultado2 = float( self.var1.get() ) % float( self.var2.get())
                if(resultado2 == 0):
                    self.message['text'] = 'La division realizada es exacta y su cociente es: {}'.format(resultado)
                else:
                    self.message['text'] = 'La division realizada es inexacta y su cociente es: {}'.format(resultado)
            else:
                self.message['text'] = 'los campos son requeridos'                        

#Validamos si estamos en la aplicación inicial
if __name__ == '__main__':

    #Establecemos la propiedad de tkinter a la variable window
    window = Tk()

    #En la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Hazel(window)

    #Ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()