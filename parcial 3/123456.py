from tkinter import *
from datetime import date
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr #leer funcion introducida

class area():
    def integrar():
        try:
            print(funcion.get())
            x=symbols('x')
            f_escrita=funcion.get()
            s=lims.get()
            i=limi.get()
            f=parse_expr(f_escrita)
            intregal=integrate(f,(x,i,s))
            resultado.configure(text=intregal)
            print(intregal)

        except:
            resultado.configure(text='ingresa la funcion correctamente')

    def graficar():
        x,y=symbols('x y')
        g=funcion.get()
        s=lims.get()
        i=limi.get()
        #f=parse_expr(f_escrita)
        plot((g,(x,i,s)),title='GRAFICA DE LA FUNCION',xlabel='eje x',ylabel='eje y')
           




    global ventana
    ventana=Tk()
    ventana.title('calculo integral')
    ventana.geometry('750x300')
    now=date.today()

    anuncio=Label(ventana, text=now, font=('Arial',15),fg='blue')
    titulo=Label(ventana, text='AREA BAJO LA CURVA', font=('Arial',15),fg='blue')
    anuncio1=Label(ventana, text='introduce una funcion de x:', font=('Arial',15),fg='blue')
    anuncio3=Label(ventana, text='limite superior:', font=('Arial',15),fg='blue')
    anuncio2=Label(ventana, text='limite inferior:', font=('Arial',15),fg='blue')

    anuncio4=Label(ventana, text='resultado:', font=('Arial',15),fg='red')
    global resultado
    resultado=Label(ventana, text='', font=('Arial',15),fg='blue')
    
    
    global funcion, lims, limi
    
    funcion=Entry(ventana,font=('Arial',15))
    lims=Entry(ventana,font=('Arial',15))
    limi=Entry(ventana,font=('Arial',15))


    boton1= Button(ventana, text='integrar',font=('Arial',15),command=integrar)
    boton2= Button(ventana, text='graficar',font=('Arial',15),command=graficar)
    boton3= Button(ventana, text='salir',font=('Arial',15),command=lambda:ventana.destroy())


    anuncio.grid(row= 0, column= 4)
    titulo.grid(row= 1, column=2)
    anuncio1.grid(row= 3, column= 0)
    anuncio2.grid(row= 4, column= 0)
    anuncio3.grid(row= 5, column= 0)
    anuncio4.grid(row= 6, column= 0)
    resultado.grid(row= 6, column= 2)

    funcion.grid(row= 3, column= 2)
    lims.grid(row= 5, column= 2)
    limi.grid(row= 4, column= 2)
    

    boton1.grid(row= 7, column= 1)
    boton2.grid(row= 7, column= 2)
    boton3.grid(row= 8, column= 0)
    







    ventana.mainloop()

