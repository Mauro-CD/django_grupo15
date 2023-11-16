# courses/models.py
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User #agregado 22 octubre
from django.urls import reverse_lazy


# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)


#### relacion uno a mucho: Docente -> Course 
class Docente(User):
    legajo = models.IntegerField()

    class Meta():
        verbose_name_plural = 'Docentes'
        # dbidable = 'nombre_tabla'

    def __str__(self):
        return f"{self.legajo} - {self.first_name} {self.last_name}"
    
    def baja_docente(self):
        return reverse_lazy('baja_docente', args=[self.id])

    def modificar_docente(self):
        return reverse_lazy('modificar_docente', args=[self.id])
    
    @staticmethod
    def obtener_docentes():
        docentes = Docente.objects.all()
        lista_docentes = [(docente.id, docente) for docente in docentes]
        return lista_docentes


class Estudiante(User):
    matricula = models.IntegerField()
    activo = models.BooleanField()
    # Course = models.ManyToManyField(Course, through="Comision")
    def __str__(self):
        return f"{self.matricula} - {self.first_name} {self.last_name}"

    def baja_estudiante(self):
        return reverse_lazy('baja_estudiante', args=[self.id])

    def modificar_estudiante(self):
        return reverse_lazy('modificar_estudiante', args=[self.id])
    
    class Meta():
        verbose_name_plural = 'Estudiantes'
        # db_table = 'nombre_tabla'


class Course(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255)#13nov agregado
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=False)
    estudiantesInscripto = models.ManyToManyField(Estudiante, through='Inscripcion')

    def __str__(self):
        return f"{self.titulo} - Docente: {self.docente.first_name}  {self.docente.last_name}"

    def baja_curso(self):
        return reverse_lazy('baja_curso', args=[self.id])

    def modificar_curso(self):
        return reverse_lazy('modificar_curso', args=[self.id])
    
    
    
    

#### relacion mucho a mucho mediante inscripcion: Estudiante -> Course 
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Course, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.estudiante.matricula} {self.estudiante.username}- {self.curso.titulo} "

    class Meta():
        verbose_name_plural = 'Inscripciones'


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name=models.CharField(max_length=100,null=False,default='name')
    views=models.IntegerField(default=0,null=False)
    
    def __str__(self):
        return self.name

#### relacion uno a mucho: Estudiante -> Foro
class Foro(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

#### relacion uno a uno: Estudiante -> Direccion
class Direccion(models.Model):
    calle = models.CharField(default="Completar")
    altura = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=100, default="Completar")
    pais = models.CharField(max_length=100, default="Completar")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return f"{self.calle} {self.altura} {self.ciudad} {self.pais} {self.usuario}"
 


class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.email} {self.telefono} {self.mensaje}"
    
# class UserList(User):
#     def __str__(self):
#         return f"{self.username} {self.email} {self.is_active} {self.first_name} {self.last_name}"
