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
    #nombre = forms.CharField(label='Nombre:', required=True)
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


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre',  required=True)
    email = forms.EmailField(label='Correo Electrónico',  required=True)
    telefono = forms.CharField(label='Telefono:', required=True)
    mensaje = forms.CharField(label='mensaje:', widget=forms.TextInput,  required=True)