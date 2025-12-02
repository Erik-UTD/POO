"""
1)Implementacion de mvc
2)Paradigma POO
3)interfaces:
    3.1 menu_principal()
    3.2 menu_acciones () dependiendo del tipo de coche
    3.3 insertar_autos()
"""
from tkinter import *
from tkinter import messagebox
from controller import controlador1
from model import model
class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.geometry("500x500")
        ventana.title(".:: Coches system ::.")
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for i in ventana.winfo_children():
            i.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=".:: Menú Principal ::.")
        lbltit.pack(pady=10)

        btn_autos=Button(ventana,text="1.- Autos",command=lambda:View.menu_acciones(ventana,"autos"))
        btn_autos.pack(pady=5)
        btn_camionetas=Button(ventana,text="2.- Camionetas",command=lambda:View.menu_acciones(ventana, "camionetas")) ### botones con lambda para pasar ventana y se llaman con self
        btn_camionetas.pack(pady=5)
        btn_camiones=Button(ventana,text="3.- camiones",command=lambda:View.menu_acciones(ventana,"camiones")) ### botones con lambda para pasar ventana y se llaman con self
        btn_camiones.pack(pady=5)
        btnsal=Button(ventana,text="4.- Salir",command=ventana.quit)
        btnsal.pack(pady=5)

    @staticmethod
    def menu_acciones(ventana,tipo):
        if tipo == "autos":
            View.borrar_pantalla(ventana)
            lbltit=Label(ventana,text=f".:: Menú de {tipo} ::.")
            lbltit.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_autos(ventana))
            btn_insertar.pack(pady=5)
            btn_consultar=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_autos(ventana)) 
            btn_consultar.pack(pady=5)
            btn_actualizar=Button(ventana,text="3.- Actualizar",command=lambda:View.cambiar_autos(ventana)) 
            btn_actualizar.pack(pady=5)
            btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:View.borrar_autos(ventana)) 
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
            btn_volver.pack(pady=5)

        elif tipo == "camionetas":
            View.borrar_pantalla(ventana)
            lbltit=Label(ventana,text=f".:: Menú de {tipo} ::.")
            lbltit.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_camionetas(ventana))
            btn_insertar.pack(pady=5)
            btn_consultar=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_camionetas(ventana)) 
            btn_consultar.pack(pady=5)
            btn_actualizar=Button(ventana,text="3.- Actualizar",command=lambda:View.cambiar_camionetas(ventana)) 
            btn_actualizar.pack(pady=5)
            btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:View.borrar_camionetas(ventana)) 
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
            btn_volver.pack(pady=5)

        elif tipo == "camiones":
            View.borrar_pantalla(ventana)
            lbltit=Label(ventana,text=f".:: Menú de {tipo} ::.")
            lbltit.pack(pady=10)
            btn_insertar=Button(ventana,text="1.- Insertar",command=lambda:View.insertar_camiones(ventana))
            btn_insertar.pack(pady=5)
            btn_consultar=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_camiones(ventana)) 
            btn_consultar.pack(pady=5)
            btn_actualizar=Button(ventana,text="3.- Actualizar",command=lambda:View.cambiar_camiones(ventana)) 
            btn_actualizar.pack(pady=5)
            btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:View.borrar_camiones(ventana)) 
            btn_eliminar.pack(pady=5)
            btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
            btn_volver.pack(pady=5)


    @staticmethod
    def insertar_autos(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Vamos a añadir un auto ::.")
        lbltit.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Color").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        velocidad=IntVar()
        lbl_velocidad=Label(ventana,text="Velocidad", textvariable=velocidad).pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)
        btn_crear=Button(ventana,text=f"Crear auto",command=lambda: controlador1.Controlador.crear_auto(txt_marca.get(),txt_color.get(),txt_modelo.get(),txt_velocidad.get(),txt_caballaje.get(),txt_plazas.get()))
        btn_crear.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def insertar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Vamos a añadir un auto ::.")
        lbltit.pack(pady=10)

        lbl_marca=Label(ventana,text="Marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Color").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        lbl_traccion=Label(ventana,text="Traccion").pack(pady=5)
        txt_traccion=Entry(ventana)
        txt_traccion.pack(pady=5)

        lbl_cerrada=Label(ventana,text="Cerrada").pack(pady=5)
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=5)



        btn_crear=Button(ventana,text=f"Crear camioneta",command=lambda: controlador1.Controlador.crear_coche(txt_marca.get(),txt_color.get(),txt_modelo.get(),txt_velocidad.get(),txt_caballaje.get(),txt_plazas.get()))
        btn_crear.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana):
            lbl_marca=Label(ventana,text="Marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Color").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            lbl_eje=Label(ventana,text="Eje").pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_capCarga=Label(ventana,text="Capacidad de Carga").pack(pady=5)
            txt_capCarga=Entry(ventana)
            txt_capCarga.pack(pady=5)

            btn_crear=Button(ventana,text=f"Crear camion",command= controlador1)
            btn_crear.pack(pady=5)




# :::::::::::::::::: MENUS DE CONSULTAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @staticmethod
    def consultar_autos(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son los autos disponibles ::.")
        lbltit.pack(pady=10)
        lbl_contenido=Label(ventana,text=f"En el entry de abajo se veran los autos disponibles ").pack(pady=5)
        txt_contenido=Entry(ventana)
        txt_contenido.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    def consultar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son las camionetas disponibles ::.")
        lbltit.pack(pady=10)
        lbl_contenido=Label(ventana,text=f"En el entry de abajo se veran los autos disponibles ").pack(pady=5)
        txt_contenido=Entry(ventana)
        txt_contenido.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    def consultar_camiones(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son los camiones disponibles ::.")
        lbltit.pack(pady=10)
        lbl_contenido=Label(ventana,text=f"En el entry de abajo se veran los autos disponibles ").pack(pady=5)
        txt_contenido=Entry(ventana)
        txt_contenido.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)



# :::::::::::::::::: MENUS DE CAMBIAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    @staticmethod
    def cambiar_autos(ventana):
        View.borrar_pantalla(ventana)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.config(state="readonly")
        txt_id.pack(pady=5)

        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)



        btn_cambiar=Button(ventana,text=f"Cambiar auto",command= controlador1)
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def cambiar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        lbl_traccion=Label(ventana,text="Nueva Traccion").pack(pady=5)
        txt_traccion=Entry(ventana)
        txt_traccion.pack(pady=5)

        lbl_cerrada=Label(ventana,text="Nuevo Cerrada").pack(pady=5)
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=5)

        btn_cambiar=Button(ventana,text=f"Cambiar camioneta",command= controlador1)
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def cambiar_camiones(ventana):
        View.borrar_pantalla(ventana)
        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=5)

        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
        txt_caballaje=Entry(ventana)
        txt_caballaje.pack(pady=5)

        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana)
        txt_plazas.pack(pady=5)

        lbl_eje=Label(ventana,text="Nuevo Eje").pack(pady=5)
        txt_eje=Entry(ventana)
        txt_eje.pack(pady=5)

        lbl_capCarga=Label(ventana,text="Nueva Capacidad de Carga").pack(pady=5)
        txt_capCarga=Entry(ventana)
        txt_capCarga.pack(pady=5)

        btn_cambiar=Button(ventana,text=f"Cambiar camiones",command= controlador1)
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

# :::::::::::::::::: MENUS DE BORRAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @staticmethod
    def borrar_autos(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menu de eliminacion de autos ::.")
        lbltit.pack(pady=10)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana).pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar",command=lambda:View.id_consultar(ventana))
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menu de eliminacion de camionetas ::.")
        lbltit.pack(pady=10)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana).pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar",command=lambda:View.id_consultar(ventana))
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrar_camiones(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menu de eliminacion de camiones ::.")
        lbltit.pack(pady=10)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana).pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar",command=lambda:View.id_consultar(ventana))
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)





"""


    @staticmethod
    def menu_acciones(ventana,tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menú de {tipo} ::.")
        lbltit.pack(pady=10)
        btn_insertar=Button(ventana,text="1.- Insertar",command=lambda:View.menu_insertar(ventana, tipo))
        btn_insertar.pack(pady=5)
        btn_consultar=Button(ventana,text="2.- Consultar",command=lambda:View.consultar_coches(ventana, tipo)) 
        btn_consultar.pack(pady=5)
        btn_actualizar=Button(ventana,text="3.- Actualizar",command=lambda:View.id_consultar(ventana,tipo)) 
        btn_actualizar.pack(pady=5)
        btn_eliminar=Button(ventana,text="4.- Eliminar",command=lambda:View.borrar_coches(ventana,tipo)) 
        btn_eliminar.pack(pady=5)
        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def menu_insertar(ventana, tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Vamos a añadir un coche tipo {tipo} ::.")
        lbltit.pack(pady=10)
        if tipo == "autos":

            lbl_marca=Label(ventana,text="Marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Color").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)



            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command=lambda: controlador1.Controlador.crear_coche(txt_marca.get(),txt_color.get(),txt_modelo.get(),txt_velocidad.get(),txt_caballaje.get(),txt_plazas.get()))
            btn_crear.pack(pady=5)

        elif tipo == "camionetas":
            lbl_marca=Label(ventana,text="Marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Color").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            lbl_traccion=Label(ventana,text="Traccion").pack(pady=5)
            txt_traccion=Entry(ventana)
            txt_traccion.pack(pady=5)

            lbl_cerrada=Label(ventana,text="Cerrada").pack(pady=5)
            txt_cerrada=Entry(ventana)
            txt_cerrada.pack(pady=5)

            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command= controlador1)
            btn_crear.pack(pady=5)

        elif tipo == "camiones":
            lbl_marca=Label(ventana,text="Marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Color").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            lbl_eje=Label(ventana,text="Eje").pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_capCarga=Label(ventana,text="Capacidad de Carga").pack(pady=5)
            txt_capCarga=Entry(ventana)
            txt_capCarga.pack(pady=5)

            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command= controlador1)
            btn_crear.pack(pady=5)




        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def consultar_coches(ventana, tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son los {tipo} disponibles ::.")
        lbltit.pack(pady=10)
        lbl_contenido=Label(ventana,text=f"En el entry de abajo se veran los {tipo} disponibles ").pack(pady=5)
        txt_contenido=Entry(ventana)
        txt_contenido.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def id_consultar(ventana, tipo):
        View.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=f".:: Menu de modificacion de {tipo} ::.")
        lbltit.pack(pady=10)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana).pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar",command=model.Model)
        btn_buscar.pack(pady=5)



    @staticmethod
    def cambiar_coches(ventana, tipo):
        View.borrar_pantalla(ventana)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.config(state="readonly")
        txt_id.pack(pady=5)
        

        if tipo == "autos":

            lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)



            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command= controlador1)
            btn_crear.pack(pady=5)

        elif tipo == "camionetas":
            lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            lbl_traccion=Label(ventana,text="Nueva Traccion").pack(pady=5)
            txt_traccion=Entry(ventana)
            txt_traccion.pack(pady=5)

            lbl_cerrada=Label(ventana,text="Nuevo Cerrada").pack(pady=5)
            txt_cerrada=Entry(ventana)
            txt_cerrada.pack(pady=5)

            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command= controlador1)
            btn_crear.pack(pady=5)

        elif tipo == "camiones":
            lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
            txt_marca=Entry(ventana)
            txt_marca.focus()
            txt_marca.pack(pady=5)

            lbl_color=Label(ventana,text="Nuevo olor").pack(pady=5)
            txt_color=Entry(ventana)
            txt_color.pack(pady=5)

            lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
            txt_modelo=Entry(ventana)
            txt_modelo.pack(pady=5)

            lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
            txt_velocidad=Entry(ventana)
            txt_velocidad.pack(pady=5)

            lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
            txt_caballaje=Entry(ventana)
            txt_caballaje.pack(pady=5)

            lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
            txt_plazas=Entry(ventana)
            txt_plazas.pack(pady=5)

            lbl_eje=Label(ventana,text="Nuevo Eje").pack(pady=5)
            txt_eje=Entry(ventana)
            txt_eje.pack(pady=5)

            lbl_capCarga=Label(ventana,text="Nueva Capacidad de Carga").pack(pady=5)
            txt_capCarga=Entry(ventana)
            txt_capCarga.pack(pady=5)

            btn_crear=Button(ventana,text=f"Crear coche tipo {tipo}",command= controlador1)
            btn_crear.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrar_coches(ventana, tipo):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Menu de eliminacion de {tipo} ::.")
        lbltit.pack(pady=10)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana).pack(pady=5)
        btn_buscar=Button(ventana,text="Buscar",command=lambda:View.id_consultar(ventana,tipo))
        btn_buscar.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana, tipo))
        btn_volver.pack(pady=5)

"""


