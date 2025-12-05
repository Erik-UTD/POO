from conexionBD import *

class Model:
  
    @staticmethod
    def crear_auto(marca, color, modelo, velocidad, caballaje, plazas):
        try:
          cursor.execute(
            "insert into autos values(NULL,%s,%s,%s,%s,%s,%s)",
            (marca, color, modelo, velocidad,caballaje, plazas)
          )
          conexion.commit()
          return True
        except:
          return False
        
    @staticmethod
    def crear_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
          cursor.execute(
            "insert into camionetas values(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",
            (marca, color, modelo, velocidad,caballaje, plazas, traccion, cerrada)
          )
          conexion.commit()
          return True
        except:
          return False
        
    @staticmethod
    def crear_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, cap_carga):
        try:
          cursor.execute(
            "insert into camiones values(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",
            (marca, color, modelo, velocidad,caballaje, plazas, eje, cap_carga)
          )
          conexion.commit()
          return True
        except:
          return False
        

    @staticmethod
    def consultar_autos():
        try:
            cursor.execute("Select * from autos")
            
            return cursor.fetchall()
        except:
            return []
        

    @staticmethod
    def consultar_camionetas():
        try:
            cursor.execute("Select * from camionetas")
            
            return cursor.fetchall()
        except:
            return []
            


    @staticmethod
    def consultar_camiones():
        try:
            cursor.execute("Select * from camiones")
            
            return cursor.fetchall()
        except:
            return []
            
            





    @staticmethod
    def mostrar(usuario_id):
        try:
          cursor.execute(
            "select * from notas where usuario_id=%s",
            (usuario_id,)
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar_auto(marca, color, modelo, velocidad, caballaje, plazas, id):
      try:
        cursor.execute(
            "update autos set marca=%s,color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s where id=%s",
            (marca, color, modelo, velocidad, caballaje, plazas, id)
        )
        conexion.commit()
        return True
      except:   
        return False

    @staticmethod
    def actualizar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
      try:
        cursor.execute(
            "update camionetas set marca=%s,color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s where id=%s",
            (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
        )
        conexion.commit()
        return True
      except:   
        return False     
      


      
    @staticmethod
    def actualizar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, cap_Carga, id):
      try:
        cursor.execute(
            "update camiones set marca=%s,color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s where id=%s",
            (marca, color, modelo, velocidad, caballaje, plazas, eje, cap_Carga, id)
        )
        conexion.commit()
        return True
      except:   
        return False     


    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from autos where id=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar_camioneta(id):
        try:
            cursor.execute(
                "delete from camionetas where id=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar_camion(id):
        try:
            cursor.execute(
                "delete from camiones where id=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False



        
    @staticmethod
    def check(id):
        try:
            cursor.execute(
                "select * from autos where id=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False
        
    @staticmethod
    def check_camioneta(id):
        try:
            cursor.execute(
                "select * from camionetas where id=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False
        

    @staticmethod
    def check_camion(id):
        try:
            cursor.execute(
                "select * from camiones where id=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False