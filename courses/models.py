# courses/models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User #agregado 22 octubre


class Docente(User):
    legajo = models.IntegerField()

#### relacion uno a mucho: Docente -> Course 
class Course(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)


#### relacion mucho a mucho mediante inscripcion: Estudiante -> CursoInscripto 
class CursoInscripto(Course):
    habilitado =  bool()

class Estudiante(User):
    matricula = models.IntegerField()
    Activo = bool()
    cursoInscripto = models.ManyToManyField(CursoInscripto, through="inscripcion")

class inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(CursoInscripto, on_delete=models.CASCADE)
    

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name=models.CharField(max_length=100,null=False,default='name')
    views=models.IntegerField(default=0,null=False)
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

#### relacion uno a mucho: User -> Foro
class Foro(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

#### relacion uno a uno: User -> Direccion
class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
 

