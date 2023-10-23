# courses/models.py
from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model): # formulario contacto
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=150, verbose_name="E-mail") 
    edad = models.CharField(verbose_name="Edad")
    # dni = models.CharField(verbose_name="DNI")

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name=models.CharField(max_length=100,null=False,default='name')
    views=models.IntegerField(default=0,null=False)
    
    def __str__(self):
        return self.name
