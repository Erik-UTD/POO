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

    @staticmethod
    def crear_auto(marca, color, modelo,velocidad, caballaje,plazas):
        respuesta=model.Model.crear_auto(marca, color, modelo,velocidad ,caballaje, plazas)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def mostrar_autos():
        respuesta=model.Model.consultar_autos()
        return respuesta
    


    @staticmethod
    def actualizar_auto2(ventana,respuesta,id):
        interfaces.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=".::Cambiar una Operacion::.")
        lbltit.pack(pady=5)

        cajaid=Entry(ventana, width=6)
        cajaid.insert(0,id)
        cajaid.config(state='readonly')
        cajaid.pack()

        num2=StringVar()
        velocidad=StringVar()
        res=StringVar()
        lbl_marca=Label(ventana,text="Marca:")
        lbl_marca.pack(pady=5)

        caja1=Entry(ventana, width=6)
        caja1.insert(0,respuesta[1])
        caja1.focus()
        caja1.pack(pady=5)

        lbl_color=Label(ventana,text="Color:")
        lbl_color.pack(pady=5)
        caja2=Entry(ventana,width=6)
        caja2.insert(0,respuesta[2])
        caja2.pack(pady=5)

        lbl_modelo=Label(ventana,text="Modelo:")
        lbl_modelo.pack(pady=5)
        caja2=Entry(ventana,width=6)
        caja2.insert(0,respuesta[3])
        caja2.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Velocidad:")
        lbl_velocidad.pack(pady=5)
        caja3=Entry(ventana,textvariable=velocidad,width=6)
        caja3.insert(0,respuesta[4])
        caja3.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Velocidad:")
        lbl_velocidad.pack(pady=5)
        caja3=Entry(ventana,textvariable=velocidad,width=6)
        caja3.insert(0,respuesta[4])
        caja3.pack(pady=5)

        lbl_resultado=Label(ventana,text="Resultado")
        lbl_resultado.pack(pady=5)
        caja4=Entry(ventana,textvariable=res,width=6)
        caja4.insert(0,respuesta[5])
        caja4.pack(pady=5)

        btnenv=Button(ventana,text="Guardar",command=lambda:Controlador)
        btnenv.pack()
        btn_volver=Button(ventana,text="5.- Volver",command=lambda:interfaces.View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def check_actualizar_auto(ventana,id): 
        respuesta=model.Model.check(id)
        if respuesta:
            interfaces.View.cambiar_autos_2(ventana,respuesta,id)
        else:
            messagebox.showinfo(message=f"ID no encontrada")

    @staticmethod
    def check_eliminar_auto(ventana,id): 
        respuesta=model.Model.check(id)
        if respuesta:
            interfaces.View.borrar_autos_2(ventana,id)
        else:
            messagebox.showinfo(message=f"ID no encontrada")


    @staticmethod
    def eliminar_auto(id):
        respuesta=model.Model.eliminar(id)
        Controlador.respuesta_sql(respuesta)

    @staticmethod
    def actualizar_auto(marca, color, modelo, velocidad, caballaje, plazas, id):
        respuesta=model.Model.actualizar_auto(marca, color, modelo, velocidad, caballaje, plazas, id)
        Controlador.respuesta_sql(respuesta)


"""
    @staticmethod
    def enviar_actualizacion(num1,num2,simb,res,id):
            respuesta=operaciones.Operaciones.actualizar(num1,num2,simb,res,id)
            funcionesc.respuesta_sql(respuesta)

    @staticmethod
    def crear_camioneta(marca, color, modelo,velocidad, caballaje, plazas, traccion, cerrada):
        respuesta=model.Model.crear_camioneta(marca, color, modelo,velocidad ,caballaje, plazas, traccion, cerrada)
        Controlador.respuesta_sql(respuesta)

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