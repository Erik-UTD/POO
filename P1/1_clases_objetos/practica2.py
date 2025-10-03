"""
Ejercicio práctico # "Moldear y DIagramar en POO"
"""

import os

os.system("cls")

#Crear una clase 
class Coches:
    #Método constructor que inicializa los valores de los atributos cuando se instancie un objeto de la clase
    def __init__(self,color,marca,velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad

    def acelerar(self,incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self,decremento):
        self.velocidad=self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "PIIIII"
    
#Instanciar objetos de la clase Coches

coche1=Coches("Rojo","Toyota", 120)
coche2=Coches("Azul","Nissan", 180)


"""
print(f"Los valores del coche 1 son:{coche1.color},{coche1.marca}, {coche1.velocidad} ")
print(f"La velocidad original del coche 1 es: {coche1.velocidad} y cambio a {coche1.acelerar(50)}")
print(f"Los valores del coche 2 son:{coche2.color},{coche2.marca}, {coche2.velocidad} ")
print(f"La velocidad original del coche 1 es: {coche2.velocidad} y cambio a {coche2.frenar(100)}")
"""
