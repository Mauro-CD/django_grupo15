# forms.py

from django import forms
from django.core.exceptions import ValidationError


class CourseFilterForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
    # Add more filter fields as needed

class Estilos(forms.TextInput):
    CSS = {'all': ('red_estilos.css')}

class EstilosInput():
    attrs={'class': 'formInput'}

class RegistrarForm(forms.Form):
    user = forms.CharField(label='Usuario',  required=True)
    nombre = forms.CharField(label='Nombre',  required=True)
    apellido = forms.CharField(label='Apellido:',  required=True)
    email = forms.EmailField(label='Correo Electrónico',  required=True)
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput,   required=True)
    passwordConfirm = forms.CharField(label='Confirmar Contraseña:', widget=forms.PasswordInput,  required=True)


    def clean_user(self):
        if self.cleaned_data['user'] == "carlos":
            raise ValidationError("El usuario ya existe")
        return self.cleaned_data['user']
    
    def clean(self):
        if self.cleaned_data['password'] !=  self.cleaned_data['passwordConfirm']:
             print("clave incorrecta")
             raise ValidationError("La contraseña no coincide")
        return self.cleaned_data

#agregado 22 octubre, actualmente este registra el usuario y lo envìa a la tabla default del db (auth_user)
class UserRegistrationForm(forms.Form):
    name = forms.CharField(label='Nombre', min_length=2)
    lastname = forms.CharField(label='Apellido', min_length=2)
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, min_length=6)


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    email = forms.EmailField(label='E-mail',max_length=100,required=True,error_messages={'required': 'Por favor completa el campo'},widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'ejemplo@email.com'}))
    telefono =  forms.IntegerField(label="Teléfono",widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo números'}  ), min_value=0)
    mensaje = forms.CharField(widget=forms.Textarea)