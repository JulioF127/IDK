from tkinter import ttk
from tkinter import *

class Años:
    def __init__(self, window):
        # Inicio

        #ancho y alto de la ventana 
        ancho = 800
        alto = 600

        #Asignamos a la ventana a una variable de la clase llamada wind
        self.wind = window

        #Le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #opción para centrar el contenido 
        self.wind.columnconfigure(0, weight=1)

        #asignamos un titulo a la ventana
        self.wind.title('Diferencia de Años')

        #Creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Diferencia de años', background="#7a071a", fg='White')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 40)


        #Creamos un etiqueta
        Label(frame, text = 'Ingrese el año actual: ',background="#7a071a", fg='white').grid(row = 1, column = 0)

        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        #Al igual que el anterior creamos una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Ingrese cualquier año: ',background="#7a071a", fg='white').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #Creamos un boton para ejecutar la Operación
        Button(frame, text = 'Resultado', background="#ba2840",command = self.restar).grid(row = 3, columnspan = 2, sticky = W + E)
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'blue',background="pink")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0


    # esta es la función que ejecuta la resta
    def restar(self):  
        if(int(self.var1.get()) == int(self.var2.get())):
            self.message['text'] = 'los años ingresados son iguales'   
        else:    
            if self.validation():
                resultado = int( self.var1.get() ) - int( self.var2.get() )
                if(resultado > 0):
                    self.message['text'] = 'Han pasado: {} ''años'.format(int(resultado))
                else:
                    resultado2 = int( self.var2.get() ) - int( self.var1.get() )
                    self.message['text'] = 'Faltan: {} ''años'.format(int(resultado2))                
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