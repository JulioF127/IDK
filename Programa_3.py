from tkinter import ttk
from tkinter import *

class Años:
    def __init__(self, window):
        # Inicio

        #ancho y alto de la ventana 
        ancho = 400
        alto = 400

        #Asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #Le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #Opción para centrar el contenido 
        self.wind.columnconfigure(0, weight=1)

        #Le asignamos un titulo a la ventana
        self.wind.title('Diferencia de Años')

        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Intervalo de tiempo', background="#b2185b")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 40)

    
        # creamos un etiqueta
        Label(frame, text = 'Ingrese el año actual: ', background="#b2185b").grid(row = 1, column = 0)

        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Ingrese cualquier año: ', background="#b2185b").grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #Creamos un boton para ejecutar la Operación
        Button(frame, text = 'Resultado',  background="#a3497a",command = self.restar).grid(row = 3, columnspan = 2, sticky = W + E)
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'white', background="#d66898")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0


    # esta es la función que ejecuta la resta
    def restar(self):
        if(float(self.var2.get()) == 0):
            self.message['text'] = 'No es posible realizar la operacion con 0.'
        else:    
            if self.validation():
                resultado = float( self.var2.get() ) - float( self.var1.get() )
                resultado2 = float( self.var1.get() ) - float( self.var2.get() )
                if(resultado2 > 0):
                    self.message['text'] = 'Han pasado: {} ''años'.format(int(resultado2))
                else:
                    self.message['text'] = 'Faltan: {} ''años'.format(int(resultado))
            else:
                self.message['text'] = 'los campos son requeridos'  
                                
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':

    #asignamos la propiedad de tkinter a la variable window
    window = Tk()

    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Años(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()