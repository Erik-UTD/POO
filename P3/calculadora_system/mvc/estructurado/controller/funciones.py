from tkinter import messagebox


# def alert(titulo, operacion, numero1, numero2, resultado):
#     mostrar=messagebox.showinfo(title=titulo, icon="info", message=f"{numero1} {operacion} {numero2} = {resultado}")
#     return mostrar

def operaciones(n1,n2,signo):
    if signo=="+":
        ope=n1+n2
        tipo_ope="Suma"
    elif signo=="-":
        ope=n1-n2
        tipo_ope="Resta"
    elif signo=="*":
        ope=n1*n2
        tipo_ope="Multiplicacion"
    elif signo=="/":
        ope=n1/n2
        tipo_ope="Division"
    messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1} {signo} {n2} ={ope}")


    
"""
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
    

    """