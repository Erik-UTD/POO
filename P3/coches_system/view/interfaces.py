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
    def checar_cerrada(cerrada):
        if cerrada=="SI":
            cerrada=True
        else:
            cerrada=False  
        return cerrada

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
        lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.pack(pady=5)

        btn_crear=Button(ventana,text=f"Crear auto",command=lambda: controlador1.Controlador.crear_auto(txt_marca.get(),txt_color.get(),txt_modelo.get(),velocidad.get(),caballaje.get(),plazas.get()))
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

        velocidad=IntVar()
        lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.pack(pady=5)

        lbl_traccion=Label(ventana,text="Traccion").pack(pady=5)
        txt_traccion=Entry(ventana)
        txt_traccion.pack(pady=5)

        cerrada=IntVar()
        lbl_cerrada=Label(ventana,text="Cerrada 0-no / 1-si").pack(pady=5)
        txt_cerrada=Entry(ventana, textvariable=cerrada)
        txt_cerrada.pack(pady=5)




        btn_crear=Button(ventana,text=f"Crear camioneta",command=lambda: controlador1.Controlador.crear_camioneta(txt_marca.get(),txt_color.get(),txt_modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), txt_traccion.get(),cerrada.get() ))
        btn_crear.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Vamos a añadir un camion ::.")
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
        lbl_velocidad=Label(ventana,text="Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.pack(pady=5)

        eje=IntVar()
        lbl_eje=Label(ventana,text="Eje").pack(pady=5)
        txt_eje=Entry(ventana, textvariable=eje)
        txt_eje.pack(pady=5)

        cap_carga=IntVar()
        lbl_capCarga=Label(ventana,text="Capacidad de Carga").pack(pady=5)
        txt_capCarga=Entry(ventana, textvariable=cap_carga)
        txt_capCarga.pack(pady=5)


        btn_crear=Button(ventana,text=f"Crear camion",command=lambda: controlador1.Controlador.crear_camion(txt_marca.get(),txt_color.get(),txt_modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), eje.get(), cap_carga.get()))
        btn_crear.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)




# :::::::::::::::::: MENUS DE CONSULTAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @staticmethod
    def consultar_autos(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son los autos disponibles ::.")
        lbltit.pack(pady=10)
        registros=controlador1.Controlador.mostrar_autos()
        filas=""
        num_auto=1
        if registros:
            for i in registros:
                filas=filas+f"Auto: {num_auto} \n ID: {i[0]}.- Marca: {i[1]} Color: {i[2]} Modelo: {i[3]} Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]} \n\n "
                num_auto=num_auto+1
        else:
            messagebox.showerror(title="Autos",message=f"...¡No se encontraron autos registrados, intente de nuevo!...")

        lblnotas=Label(ventana,text=f"{filas}")
        lblnotas.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    def consultar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son las camionetas disponibles ::.")
        lbltit.pack(pady=10)
        registros=controlador1.Controlador.mostrar_camionetas()
        filas=""
        num_auto=1
        if registros:
            for i in registros:
                filas=filas+f"Camioneta: {num_auto} \n ID: {i[0]}.- Marca: {i[1]} Color: {i[2]} Modelo: {i[3]} Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]} Traccion: {i[7]} Cerrada: {i[8]}  \n\n "
                num_auto=num_auto+1
        else:
            messagebox.showerror(title="Autos",message=f"...¡No se encontraron autos registrados, intente de nuevo!...")

        lblnotas=Label(ventana,text=f"{filas}")
        lblnotas.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    def consultar_camiones(ventana):
        View.borrar_pantalla(ventana)
        lbltit=Label(ventana,text=f".:: Estos son los camiones disponibles ::.")
        lbltit.pack(pady=10)
        registros=controlador1.Controlador.mostrar_camiones()
        filas=""
        num_auto=1
        if registros:
            for i in registros:
                filas=filas+f"Camioneta: {num_auto} \n ID: {i[0]}.- Marca: {i[1]} Color: {i[2]} Modelo: {i[3]} Velocidad: {i[4]} Caballaje: {i[5]} Plazas: {i[6]} Eje: {i[7]} Capacidad de carga: {i[8]}  \n\n "
                num_auto=num_auto+1
        else:
            messagebox.showerror(title="Camiones",message=f"...¡No se encontraron camiones registrados, intente de nuevo!...")

        lblnotas=Label(ventana,text=f"{filas}")
        lblnotas.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)




# :::::::::::::::::: MENUS DE CAMBIAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @staticmethod
    def cambiar_autos(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Modificar un auto::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID del auto registrado: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_actualizar_auto(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def cambiar_autos_2(ventana,respuesta, id):
        View.borrar_pantalla(ventana)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.insert(0, id)
        txt_id.config(state="readonly")
        txt_id.pack(pady=5)

        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.insert(0, respuesta[1])
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo color").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.insert(0, respuesta[2])
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.insert(0, respuesta[3])
        txt_modelo.pack(pady=5)

        velocidad=IntVar()
        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.insert(0, respuesta[4])
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Nuevo aballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.insert(0, respuesta[5])
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.insert(0, respuesta[6])
        txt_plazas.pack(pady=5)



        btn_cambiar=Button(ventana,text=f"Cambiar auto",command=lambda:controlador1.Controlador.actualizar_auto(txt_marca.get(),txt_color.get(),txt_modelo.get(),velocidad.get(),caballaje.get(),plazas.get(), id))
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text=" Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)




    @staticmethod
    def cambiar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Modificar una camioneta::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID de la camioneta registrada: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_actualizar_camioneta(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)




    @staticmethod
    def cambiar_camionetas_2(ventana, respuesta, id):
        View.borrar_pantalla(ventana)
        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.insert(0, id)
        txt_id.config(state="readonly")
        txt_id.pack(pady=5)

        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.insert(0, respuesta[1])
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo color").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.insert(0, respuesta[2])
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.insert(0, respuesta[3])
        txt_modelo.pack(pady=5)

        velocidad=IntVar()
        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.insert(0, respuesta[4])
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Nuevo caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.insert(0, respuesta[5])
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.insert(0, respuesta[6])
        txt_plazas.pack(pady=5)



        lbl_traccion=Label(ventana,text="Nueva Traccion").pack(pady=5)
        txt_traccion=Entry(ventana)
        txt_traccion.insert(0, respuesta[7])
        txt_traccion.pack(pady=5)


        cerrada=IntVar()
        lbl_cerrada=Label(ventana,text="Cerrada? 0 = no, 1 = si").pack(pady=5)
        txt_cerrada=Entry(ventana, textvariable=cerrada)
        txt_cerrada.insert(0, respuesta[8])
        txt_cerrada.pack(pady=5)

        btn_cambiar=Button(ventana,text=f"Cambiar auto",command=lambda:controlador1.Controlador.actualizar_camioneta(txt_marca.get(),txt_color.get(),txt_modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),txt_traccion.get(), cerrada.get(), id))
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def cambiar_camiones(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Modificar un camion::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID del camion registrada: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_actualizar_camion(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)



    @staticmethod
    def cambiar_camiones_2(ventana, respuesta, id):
        View.borrar_pantalla(ventana)

        lbl_id=Label(ventana,text=f"ID: ")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.insert(0, id)
        txt_id.config(state="readonly")
        txt_id.pack(pady=5)


        lbl_marca=Label(ventana,text="Nueva marca").pack(pady=5)
        txt_marca=Entry(ventana)
        txt_marca.insert(0, respuesta[1])
        txt_marca.focus()
        txt_marca.pack(pady=5)

        lbl_color=Label(ventana,text="Nuevo color").pack(pady=5)
        txt_color=Entry(ventana)
        txt_color.insert(0, respuesta[2])
        txt_color.pack(pady=5)

        lbl_modelo=Label(ventana,text="Nuevo Modelo").pack(pady=5)
        txt_modelo=Entry(ventana)
        txt_modelo.insert(0, respuesta[3])
        txt_modelo.pack(pady=5)

        velocidad=IntVar()
        lbl_velocidad=Label(ventana,text="Nueva Velocidad").pack(pady=5)
        txt_velocidad=Entry(ventana, textvariable=velocidad)
        txt_velocidad.insert(0, respuesta[4])
        txt_velocidad.pack(pady=5)

        caballaje=IntVar()
        lbl_caballaje=Label(ventana,text="Nuevo caballaje").pack(pady=5)
        txt_caballaje=Entry(ventana, textvariable=caballaje)
        txt_caballaje.insert(0, respuesta[5])
        txt_caballaje.pack(pady=5)

        plazas=IntVar()
        lbl_plazas=Label(ventana,text="Nuevas Plazas").pack(pady=5)
        txt_plazas=Entry(ventana, textvariable=plazas)
        txt_plazas.insert(0, respuesta[6])
        txt_plazas.pack(pady=5)

        eje=IntVar()
        lbl_eje=Label(ventana,text="Nuevo Eje").pack(pady=5)
        txt_eje=Entry(ventana, textvariable=eje)
        txt_eje.insert(0, respuesta[7])
        txt_eje.pack(pady=5)

        cap_carga=IntVar()
        lbl_capCarga=Label(ventana,text="Nueva Capacidad de Carga").pack(pady=5)
        txt_capCarga=Entry(ventana, textvariable= cap_carga)
        txt_capCarga.insert(0, respuesta[8])
        txt_capCarga.pack(pady=5)

        btn_cambiar=Button(ventana,text=f"Cambiar auto",command=lambda:controlador1.Controlador.actualizar_camion(txt_marca.get(),txt_color.get(),txt_modelo.get(),velocidad.get(),caballaje.get(),plazas.get(),eje.get(), cap_carga.get(), id))
        btn_cambiar.pack(pady=5)

        btn_volver=Button(ventana,text="5.- Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

# :::::::::::::::::: MENUS DE BORRAR :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @staticmethod
    def borrar_autos(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Borrar un auto::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID del auto registrado: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_eliminar_auto(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrar_autos_2(ventana,id):
        View.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=".::Borrar un auto::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::Click en eliminar para confirmar accion ::.")
        lblind.pack(pady=5)
        btneli=Button(ventana,text="Eliminar",command=lambda:controlador1.Controlador.eliminar_auto(id))
        btneli.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)





    @staticmethod
    def borrar_camionetas(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Borrar una camioneta ::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID de la camioneta registrada: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_eliminar_camioneta(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def borrar_camionetas_2(ventana,id):
        View.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=".::Borrar una camioneta::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::Click en eliminar para confirmar accion ::.")
        lblind.pack(pady=5)
        btneli=Button(ventana,text="Eliminar",command=lambda:controlador1.Controlador.eliminar_camioneta(id))
        btneli.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def borrar_camiones(ventana):
        View.borrar_pantalla(ventana)
        id=IntVar()
        lbltit=Label(ventana,text=".::Borrar un camion ::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::ID del camion registrado: ::.")
        lblind.pack(pady=5)
        cajaid=Entry(ventana,width=5,textvariable=id,justify="right")
        cajaid.focus()
        cajaid.pack(pady=5)
        btneli=Button(ventana,text="Buscar",command=lambda:controlador1.Controlador.check_eliminar_camion(ventana, id.get()))
        btneli.pack(pady=5)
        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)


    @staticmethod
    def borrar_camiones_2(ventana,id):
        View.borrar_pantalla(ventana)

        lbltit=Label(ventana,text=".::Borrar un camion::.")
        lbltit.pack(pady=5)
        lblind=Label(ventana,text=".::Click en eliminar para confirmar accion ::.")
        lblind.pack(pady=5)
        btneli=Button(ventana,text="Eliminar",command=lambda:controlador1.Controlador.eliminar_camion(id))
        btneli.pack(pady=5)

        btn_volver=Button(ventana,text="Volver",command=lambda:View.menu_principal(ventana))
        btn_volver.pack(pady=5)



    @staticmethod
    def checar_cerrada(cerrada):
        if cerrada=="SI" or cerrada=="1" or cerrada=="si" or cerrada=="Si":
            cerrada=True
        else:
            cerrada=False  

        return cerrada


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


