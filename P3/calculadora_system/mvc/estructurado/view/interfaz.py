from tkinter import *
from tkinter import messagebox
from controller import funciones

#Interfaz o VIEW
def interfaz_principal():
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



    suma=Button(ventana, text="+", command=lambda: funciones.operaciones(n1.get(),n2.get(), signo="+"))
    suma.pack()

    resta=Button(ventana, text="-", command=lambda: funciones.operaciones(n1.get(),n2.get(), signo="-"))
    resta.pack()

    multi=Button(ventana, text="*", command=lambda: funciones.operaciones(n1.get(),n2.get(),signo="*"))
    multi.pack()

    division=Button(ventana, text="/", command=lambda: funciones.operaciones(n1.get(),n2.get(),signo="/"))
    division.pack()

    salir=Button(ventana, text="Salir",command=ventana.quit)
    salir.pack()









    ventana.mainloop()