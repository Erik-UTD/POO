"""
COPIA CON herencia
"""

import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #..::Metodo Constructor para inicializar los valores de los atributos a la hora de crear o instanciar un objeto por primera vez de la clase::..

    def __init__(self,marca, color, modelo, velocidad, caballaje, plazas):

      self._marca=marca
      self._color=color
      self._modelo=modelo
      self._velocidad=velocidad
      self._caballaje=caballaje
      self._plazas=plazas

    #Crear los metodos setters y getters, estos metodos son importantes y ncesesarios en todas las clases para que el programador interactue con los valores de los atributos a través de estos métodos...digamos que esta es la manera mas adecuada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto.
    #En teoria se deberia crear un metodo Getters y Setters por cada atributo que contenga la clase

    #Los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return

    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión

    #1er forma
    def getMarca(self):
       return self._marca
    
    def setMarca(self,marca):
       self._marca=marca

    #2da Forma
    @property
    def marca2(self):
       return self._marca
    
    @marca2.setter
    def marca2(self, marca):
       self._marca=marca



    @property
    def color(self):
       return self._color
    
    @marca2.setter
    def color(self,color):
       self._color=color

    @property
    def modelo(self):
       return self._modelo
    
    @modelo.setter
    def modelo(self,modelo):
       self._modelo=modelo
    
    @property
    def velocidad(self):
       return self._velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
       self._velocidad=velocidad

    @property
    def caballaje(self):
       return self._caballaje
    
    @caballaje.setter
    def caballaje(self,caballaje):
       self._caballaje=caballaje

    @property
    def plazas(self):
       return self._plazas
    
    @plazas.setter
    def plazas(self,plazas):
       self._plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      return "Estas acelerando el coche"

    def frenar(self):
      return "Estas frenando el coche"

#Fin definir clase

#Ejemplo de herencia, Coches hereda a Camiones
class Camiones(Coches):
   def __init__(self,marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):

      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)

      self._eje=eje
      self._capacidadCarga=capacidadCarga

   def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga
      return tipo_carga

   def acelerar(self):
      return "Estas acelerando el camion"

   def frenar(self):
      return "Estas frenando el camion"

   @property
   def eje(self):
      return self._eje
   
   @eje.setter
   def eje(self, eje):
      self._eje=eje

   @property
   def capacidadCarga(self):
      return self._capacidadCarga
   
   @eje.setter
   def capacidadCarga(self, capacidadCarga):
      self._capacidadCarga=capacidadCarga


print(f"Datos del camion: \n Marca:{Camiones.marca2} \n color: {Camiones.color} \n Modelo: {Camiones.modelo} \n velocidad: {Camiones.velocidad} \n caballaje: {Camiones.caballaje} \n plazas: {Camiones.plazas}\n eje: {Camiones.eje} \n Capacidad de Carga: {Camiones.caballaje}")



class Camionetas(Coches):
   def __init__(self,marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
      super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
      self._traccion=traccion
      self._cerrada=cerrada

   def transportar(self,num_pasajeros):
      self.num_pasajeros=num_pasajeros
      return num_pasajeros

   def acelerar(self):
      return "Estas acelerando la caioneta"

   def frenar(self):
      return "Estas frenando el camioneta"

   @property
   def traccion(self):
      return self._traccion
   
   @traccion.setter
   def traccion(self, traccion):
      self._traccion=traccion

   @property
   def cerrada(self):
      return self._cerrada
   
   @cerrada.setter
   def cerrada(self, cerrada):
      self._cerrada=cerrada


print(f"Datos de la camioneta: \n Marca:{Camionetas.marca2} \n color: {Camionetas.color} \n Modelo: {Camionetas.modelo} \n velocidad: {Camionetas.velocidad} \n caballaje: {Camionetas.caballaje} \n plazas: {Camionetas.plazas}\n Traccion: {Camionetas.traccion} \n Cerrada: {Camionetas.cerrada}")



