# forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from courses.models import Estudiante


class CourseFilterForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
    # Add more filter fields as needed

# class Estilos(forms.TextInput):
#     CSS = {'all': ('red_estilos.css')}

# class EstilosInput():
#     attrs={'class': 'formInput'}

# class RegistrarForm(forms.Form):
#     user = forms.CharField(label='Usuario',  required=True)
    # nombre = forms.CharField(label='Nombre',  required=True)
    # apellido = forms.CharField(label='Apellido:',  required=True)
    # email = forms.EmailField(label='Correo Electrónico',  required=True)
    # password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput,   required=True)
    # passwordConfirm = forms.CharField(label='Confirmar Contraseña:', widget=forms.PasswordInput,  required=True)


    # def clean_user(self):
    #     if self.cleaned_data['user'] == "carlos":
    #         raise ValidationError("El usuario ya existe")
    #     return self.cleaned_data['user']
    
    # def clean(self):
    #     if self.cleaned_data['password'] !=  self.cleaned_data['passwordConfirm']:
    #          print("clave incorrecta")
    #          raise ValidationError("La contraseña no coincide")
    #     return self.cleaned_data


################################################# Usuario ###################################################################
#agregado 22 octubre, actualmente este registra el usuario y lo envìa a la tabla default del db (auth_user)
class UserRegistrationForm(forms.Form):
    name = forms.CharField(label='Nombre', min_length=2)
    lastname = forms.CharField(label='Apellido', min_length=2)
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, min_length=6)
    
    def clean_email(self):
        if User.objects.filter(username=self.cleaned_data['email']).exists():
            raise ValidationError("El usuario ya existe")
        return self.cleaned_data['email']
    
    def clean(self):
        if self.cleaned_data['password'] !=  self.cleaned_data['password2']:
             print("clave incorrecta")
             raise ValidationError("La contraseña no coincide")
        return self.cleaned_data



################################################# CONTACTO ###################################################################
class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    email = forms.EmailField(label='E-mail',max_length=100,required=True,error_messages={'required': 'Por favor completa el campo'},widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'ejemplo@email.com'}))
    telefono = forms.IntegerField(label="Teléfono",widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo números'}  ), min_value=0)
    mensaje = forms.CharField(widget=forms.Textarea)


################################################# Foro ###################################################################
class ForoForm(forms.Form):
    # usuario = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    titulo = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    fecha = forms.DateField(label="Fecha")
    contenido = forms.CharField(widget=forms.Textarea)


################################################# Direccion ###################################################################
class DireccionForm(forms.Form):
    calle = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    altura = forms.IntegerField(label="altura",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True, max_value=100000)
    ciudad = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    pais = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)


################################################# Estudiante ###################################################################

class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = ["matricula", "first_name",'last_name']
        widgets = {
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

    # username = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # first_name = forms.IntegerField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # activo = forms.BooleanField(label="activo")


################################################# Docente ################################################################### 


################################################# Curso ################################################################### 


################################################# CursoInscripto ################################################################### 