from tkinter import ttk
from tkinter import *
class Dividir:
    def __init__(self, window):
        # Inicio

        #ancho y alto de la ventana
        ancho = 400
        alto = 400

        #Colocamos a la ventana una variable de la clase llamada "wind"
        self.wind = window

        #Colocamos el ancho y el alto a la ventana con la propiedad "Geometry"
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #Opción para centrar el contenido 
        self.wind.columnconfigure(0, weight=1)

        #Asignamos un titulo a la ventana
        self.wind.title('División')

        #Creamos un contenedor
        frame = LabelFrame(self.wind, text = 'División de 2 valores',background ="#307d99")
        frame.grid(row = 0, column = 0, columnspan = 10, pady = 100)

        #Creamos un etiqueta
        Label(frame, text = 'Escriba el Primer Número: ',background ="#307d99").grid(row = 1, column = 0)

        #Creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)

        #Al igual que la forma anterior colocamos una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'Escriba el Segundo Número: ',background = "#307d99").grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #Creamos un boton para ejecutar la Division
        Button(frame, text = 'Dividir', background ="#307d99", command = self.dividir).grid(row = 3, columnspan = 2, sticky = W + E)
      
        #Establecemos un área para mensajes
        self.message = Label(text = '', fg = 'blue', background="#1fa388")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        self.message2 = Label(text = '', fg = 'blue', background="#1fa388")
        self.message2.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)

    #Creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0

    #Esta es la función que ejecuta la división
    def dividir(self):
        if self.validation():
            resultado = int( self.var1.get() ) / int( self.var2.get() )
            resultado2 = int( self.var1.get() ) % int( self.var2.get())
            if(resultado2 == 0):
                self.message['text'] = 'La división realizada es exacta y su cociente es: {}'.format(resultado)
            else:
                self.message['text'] = 'La división realizada es inexacta su cociente es: {}'.format(int(resultado)) 
                self.message2['text'] = 'Su residuo es: {}'.format(resultado2)
        else:
            self.message['text'] = 'los campos son necesarios.'                        
            
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':

    #asignamos la propiedad de tkinter a la variable window
    window = Tk()

    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Dividir(window)
   
    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()