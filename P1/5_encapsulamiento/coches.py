"""
COPIA CON ENCAPSULAMIENTO
"""


import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #..::Metodo Constructor para inicializar los valores de los atributos a la hora de crear o instanciar un objeto por primera vez de la clase::..

    def __init__(self,marca, color, modelo, velocidad, caballaje, plazas):

      self.__marca=marca
      self.__color=color
      self.__modelo=modelo
      self.__velocidad=velocidad
      self.__caballaje=caballaje
      self.__plazas=plazas

    #Crear los metodos setters y getters, estos metodos son importantes y ncesesarios en todas las clases para que el programador interactue con los valores de los atributos a través de estos métodos...digamos que esta es la manera mas adecuada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto.
    #En teoria se deberia crear un metodo Getters y Setters por cada atributo que contenga la clase

    #Los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return

    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión

    #1er forma
    def getMarca(self):
       return self.__marca
    
    def setMarca(self,marca):
       self.__marca=marca

    #2da Forma
    @property
    def marca2(self):
       return self.__marca
    
    @marca2.setter
    def marca2(self, marca):
       self.__marca=marca




    def getColor(self):
       return self.__color
    
    def setColor(self,color):
       self.__color=color

    def getModelo(self):
       return self.__modelo
    
    def setModelo(self,modelo):
       self.__modelo=modelo

    def getVelocidad(self):
       return self.__velocidad
    
    def setVelocidad(self,velocidad):
       self.__velocidad=velocidad

    def getCaballaje(self):
       return self.__caballaje
    
    def setCaballaje(self,caballaje):
       self.__caballaje=caballaje

    def getPlazas(self):
       return self.__plazas
    
    def setPlazas(self,plazas):
       self.__plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      return "Estas acelerando"

    def frenar(self):
      return "Estas acelerando"

#Fin definir clase

#Crear un objetos o instanciar la clase


