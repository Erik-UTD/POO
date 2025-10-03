"""
COPIA CON CONSTRUCTOR
"""


import os
os.system("clear")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #..::Metodo Constructor para inicializar los valores de los atributos a la hora de crear o instanciar un objeto por primera vez de la clase::..

    def __init__(self,marca, color, modelo, velocidad, caballaje, plazas):

      self.marca=marca
      self.color=color
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas

    #Crear los metodos setters y getters, estos metodos son importantes y ncesesarios en todas las clases para que el programador interactue con los valores de los atributos a través de estos métodos...digamos que esta es la manera mas adecuada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto.
    #En teoria se deberia crear un metodo Getters y Setters por cada atributo que contenga la clase

    #Los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return

    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión

    #1er forma
    def getMarca(self):
       return self.marca
    
    def setMarca(self,marca):
       self.marca=marca

    #2da Forma
    @property
    def marca2(self):
       return self.marca
    
    @marca2.setter
    def marca2(self, marca):
       self.marca=marca




    def getColor(self):
       return self.color
    
    def setColor(self,color):
       self.color=color

    def getModelo(self):
       return self.modelo
    
    def setModelo(self,modelo):
       self.modelo=modelo

    def getVelocidad(self):
       return self.velocidad
    
    def setVelocidad(self,velocidad):
       self.velocidad=velocidad

    def getCaballaje(self):
       return self.caballaje
    
    def setCaballaje(self,caballaje):
       self.caballaje=caballaje

    def getPlazas(self):
       return self.plazas
    
    def setPlazas(self,plazas):
       self.plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase


coche1=Coches("V2","Banco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="B01928192"

coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Numero de Serie: {coche1.num_serie} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} \n Numero de Serie: {coche2.num_serie} ")

print(coche3.marca2)
