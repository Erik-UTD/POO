class Profesores:
    def __init__(self,nombre,experiencia,num_profesor):
        self._nombre=nombre
        self._experiencia=int(experiencia)
        self._num_profesor=num_profesor

    def Impartir(self):
        return str
        
    def Evaluar(self):
        return str
    
profesor1=Profesores("Carlos Carlos", 14, "6181234455")
profesor2=Profesores("Fragoso", 21, "6183235051")



class Curso:
    def __init__(self,nombre,codigo,creditos):
        self._nombre=nombre
        self._codigo=codigo
        self._creditos=int(creditos)

    def Asignar(self):
        return str

curso1=Curso("AWS", "123ABC", 3)
curso2=Curso("Tkinter", "ABC123", 4)




class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self._nombre=nombre
        self._edad=int(edad)
        self._matricula=matricula

    def Inscribirse(self):
        return str

    def Estudiar(self):
        return str
    
alumno1=Alumnos("Erik Bueno", 19, "31410192")
alumno2=Alumnos("Diego Moreno", 19, "3141240505")