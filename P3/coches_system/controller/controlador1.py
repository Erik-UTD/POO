from tkinter import *
from tkinter import messagebox
from view import interfaces
from model import model

class Controlador:
    @staticmethod
    def respuesta_sql(respuesta): 
        if respuesta:
            messagebox.showinfo(title="Autos",message=f"...¡Accion realizada con exito!...")
            
        else:
            messagebox.showerror(title="Notas",message=f"...¡No fue posible realizar la accion, intente de nuevo!...")


    def crear_auto(marca, color, modelo,velocidad, caballaje,plazas):
        respuesta=model.Model.crear(marca, color, modelo,velocidad ,caballaje, plazas)
        Controlador.respuesta_sql(respuesta)

"""
    @staticmethod
    def mostrarnota(usuario_id):
        respuesta=nota.Nota.mostrar(usuario_id)
        if respuesta:
            return respuesta
        else:
            respuesta=""
            messagebox.showwarning(message="No hay registros para mostrar",title="Notas")
            return respuesta

    @staticmethod
    def actualizarnota(id,tit,desc):
        respuesta=nota.Nota.actualizar(id,tit,desc)
        Controlador.respuesta_sql(respuesta)
        
    @staticmethod
    def eliminarnota(id):
        respuesta=nota.Nota.eliminar(id) 
        Controlador.respuesta_sql(respuesta)"""  