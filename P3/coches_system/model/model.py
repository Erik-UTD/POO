from conexionBD import *

class Model:
  
    @staticmethod
    def crear(marca, color, modelo, velocidad, caballaje, plazas):
        try:
          cursor.execute(
            "insert into autos values(NULL,%s,%s,%s,%s,%s)",
            (marca, color, modelo, velocidad,caballaje, plazas)
          )
          conexion.commit()
          return True
        except:
          return False

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
    def actualizar(id, titulo, descripcion):
      try:
        cursor.execute(
            "update notas set titulo=%s,descripcion=%s where id=%s",
            (titulo,descripcion,id)
        )
        conexion.commit()
        if cursor.rowcount>0:
          return True
        else:
          return False
      except: 
        return False
    
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from notas where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False