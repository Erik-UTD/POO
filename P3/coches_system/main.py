
"""
1)Implementacion de mvc
2)Paradigma POO
3)interfaces:
    3.1 menu_principal()
    3.2 menu_acciones () dependiendo del tipo de coche
    3.3 insertar_autos()
    3.4 consultar_autos()
    3.5 cambiar_autos()
    3.6 borrar_autos()

productos entregables:
- estructura de proyecto mvc
- modulo principal "main" funcionando
- interaccion con las interfaces

***Nombre del commit: commit_01_12_25"***
-----------------------------------------------------------------------
2 DICIEMBRE
1)Interfaces
    1.1 insertar_camionetas()
    1.2 consultar_camionetas()
    1.3 cambiar_camionetas()
    1.4 borrar_camionetas()
    2.1 insertar_camiones()
    2.2 consultar_camiones()
    2.3 cambiar_camiones()
    2.4 borrar_camiones()
Productos Entregables:
**Interaccion con todas las interfaces
**Nombre del Commit: "commit_02_12_25"
"""

from tkinter import *
from view import interfaces

class APP:
    def __init__(self,ventana):
        view=interfaces.View(ventana) 


if __name__=="__main__":
    ventana=Tk()
    app=APP(ventana)
    ventana.mainloop()   