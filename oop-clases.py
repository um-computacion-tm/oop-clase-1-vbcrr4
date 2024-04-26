import unittest

class Profesor:

    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_cargo(self):
        return self.__cargo__
    
    def obtener_legajo(self):
        return self.__legajo__

class Materia:

    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def obtener_alumnos(self):
        return self.__alumnos__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

#materia_comp = Materia("computacion",profesores=("elio","daniel","gab","walter"))

class Alumno():
    def __init__(self,nombre,edad,legajo,mail):
        self.__nombre__ = nombre
        self.__edad__ = edad
        self.__legajo__ = legajo
        self.__mail__ = mail
        self.__inasistencias__ = 0

    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_legajo(self):
        return self.__legajo__
    
    def obtener_edad(self):
        return self.__edad__
    
    def obtener_mail(self):
        return self.__mail__
    
    def obtener_inasistencias(self):
        return self.__inasistencias__
    
    def cambiar_edad(self,edad):
        self.__edad__ = edad

    def cambiar_inasistencia(self,inasistencias):
        self.__inasistencias__ = inasistencias

    
    

#alumno = Alumno(nombre=("lana"),legajo=123,edad=22,mail=None)
#print("clase alumno", Alumno)
#print(alumno)
#print("el alumno",alumno.__nombre__ , "es" , )
class TestMateria (unittest.TestCase):

    def test_init(self):
        profesores = ["elio", "daniel", "gab", "walter"]
        alumnos = Alumno("Lana", 21, 222, None)
        materia = Materia("computacion", profesores, alumnos)
        self.assertEqual(materia.__nombre__, "computacion")
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos )

    def test_obtener_profesores(self):
        profesores = ["elio", "daniel", "gab", "walter"]
        alumnos = Alumno("Lana", 21, 222, None)
        materia = Materia("computacion", profesores, alumnos)
        self.assertEqual(materia.obtener_profesores(), profesores)
    
    def test_cambiar_nombre(self):
        profesores = ["elio", "daniel", "gab", "walter"]
        alumnos = Alumno("Lana", 21, 222, None)
        materia = Materia("computacion", profesores, alumnos)
        materia.cambiar_nombre("matematica")
        self.assertEqual(materia.__nombre__, "matematica")

    def test_obtener_alumnos(self):
        profesores = ["elio", "daniel", "gab", "walter"]
        alumnos = Alumno("Lana", 21, 222, None)
        materia = Materia("computacion", profesores, alumnos)
        self.assertEqual(materia.obtener_alumnos(), alumnos)

class TestProfesor(unittest.TestCase):

    def test_init(self):
        profesor = Profesor("elio", "ayudante de catedra", 333)
        self.assertEqual(profesor.obtener_nombre(), "elio")
        self.assertEqual(profesor.obtener_cargo(), "ayudante de catedra")
        self.assertEqual(profesor.obtener_legajo(), 333)
    
    def test_obtener_nombre(self):
        profesor = Profesor("elio", "ayudante de catedra", 333)
        self.assertEqual(profesor.obtener_nombre(), "elio")
    
    def test_obtener_cargo(self):
        profesor = Profesor("elio", "ayudante de catedra", 333)
        self.assertEqual(profesor.obtener_cargo(), "ayudante de catedra")
    
    def test_obtener_legajo(self):
        profesor = Profesor("elio", "ayudante de catedra", 333)
        self.assertEqual(profesor.obtener_legajo(), 333)

class TestAlumno(unittest.TestCase):

    def test_init(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_nombre(), 'Lana')
        self.assertEqual(alumno.obtener_edad(), 21)
        self.assertEqual(alumno.obtener_legajo(), 222)
        self.assertEqual(alumno.obtener_mail(), 'lana@alumno.um.edu.ar')
        self.assertEqual(alumno.obtener_inasistencias(), 0)

    def test_obtener_nombre(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_nombre(), 'Lana')

    def test_obtener_edad(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_edad(), 21)

    def test_obtener_legajo(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_legajo(), 222)
    
    def test_obtener_mail(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_mail(), 'lana@alumno.um.edu.ar')

    def test_obtener_inasistencias(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        self.assertEqual(alumno.obtener_inasistencias(), 0)
        print(alumno.obtener_inasistencias())

    def test_cambiar_edad(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        alumno.cambiar_edad(22)
        self.assertEqual(alumno.__edad__, 22)
    def test_cambiar_inasistencia(self):
        alumno = Alumno ('Lana', 21, 222,'lana@alumno.um.edu.ar' )
        alumno.cambiar_inasistencia(1)
        self.assertEqual(alumno.__inasistencias__,1)
        print(alumno.obtener_inasistencias())

unittest.main()