from coches import *

#Solicitar los datos que posteriormente serna los atribujos del objeto

num_coches=int(input("Cuantos coches tienes? "))
for i in range(0,num_coches):
    print(f"\n\t...Datos del Automovil # {i+1}...")
    marca=input("Ingresar la marca del auto: ").upper()
    color=input("Ingresar el color del auto: ").upper()
    modelo=input("Ingresar el modelo del auto: ").upper()
    velocidad=int(input("Ingresar la velocidad del auto: "))
    potencia=int(input("Ingresar la potencia auto: "))
    plazas=int(input("Ingresar el # de plazas auto: "))


    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}")





"""
coche1=Coches("V2","Banco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)
coche1.num_serie="B01928192"

coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Numero de Serie: {coche1.num_serie} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()}")

print(coche3.marca2)

"""