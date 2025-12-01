"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 Botones para las operaciones
3.- Mostrar el resultado en una alerta

"""

from tkinter import *
from tkinter import messagebox
#Control App ó Controller
def alert(titulo, operacion, numero1, numero2, resultado):
     mostrar=messagebox.showinfo(title=titulo, icon="info", message=f"{numero1} + {numero2} = {resultado}")
     return mostrar

    

def sumar(numero1,numero2):
    resultado=numero1+numero2
    titulo="suma"
    operacion= "+"
    alerta=alert(titulo,operacion, numero1,numero2,resultado)
    return alerta


def restar(numero1,numero2):
    resultado=numero1-numero2
    titulo="suma"
    operacion= "-"
    alerta=alert(titulo,operacion, numero1,numero2,resultado)
    return alerta
    

def multiplicar(numero1,numero2):
    resultado=numero1*numero2
    titulo="suma"
    operacion= "*"
    alerta=alert(titulo,operacion, numero1,numero2,resultado)
    return alerta

def dividir(numero1,numero2):
    resultado=numero1/numero2
    titulo="suma"
    operacion= "/"
    alerta=alert(titulo,operacion, numero1,numero2,resultado)
    return alerta


#Interfaz o VIEW
ventana=Tk()
ventana.geometry("500x500")
ventana.title("Calculadora")
ventana.resizable(False,False)

n1=IntVar()
n2=IntVar()
numero1=Entry(ventana, textvariable=n1,width=5, justify="right")
numero1.pack(side="top", anchor="center")
numero2=Entry(ventana, textvariable=n2, width=5, justify="right")
numero2.pack(side="top", anchor="center")



suma=Button(ventana, text="+", command=lambda: sumar(n1.get(),n2.get()))
suma.pack()

resta=Button(ventana, text="-", command=lambda: restar(n1.get(),n2.get()))
resta.pack()

multi=Button(ventana, text="*", command=lambda: multiplicar(n1.get(),n2.get()))
multi.pack()

division=Button(ventana, text="/", command=lambda: dividir(n1.get(),n2.get()))
division.pack()

salir=Button(ventana, text="Salir",command=ventana.quit)
salir.pack()









ventana.mainloop()
