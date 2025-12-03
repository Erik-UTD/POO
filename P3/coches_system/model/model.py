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
    def consultar_autos():
        try:
            cursor.execute("Select * from autos")
            
            return cursor.fetchall()
        except:
            print("\n\t..::No hay autos registrados::..")
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
    def check(id):
        try:
            cursor.execute(
                "select * from autos where id=%s",(id,)
            )
            return cursor.fetchone()
        except:
            return False