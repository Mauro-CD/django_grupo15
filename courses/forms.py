# forms.py

import re 
#from typing import Any
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


# class ContactoForm(forms.Form):
#     nombre = forms.CharField(label='Nombre',  required=True)
#     email = forms.EmailField(label='Correo Electrónico',  required=True)
#     telefono = forms.CharField(label='Telefono:', required=True)
#     mensaje = forms.CharField(label='mensaje:', widget=forms.TextInput(attrs={'class': 'mensaje_form'}),  required=True)


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    apellido =forms.CharField(label="Apellido de contacto",widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ), required=True)
    edad = forms.IntegerField(label="Edad",widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo números'}  ), max_value=80)
    # mail = forms.EmailField(label="E-Mail", widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'ejemplo@email.com'}),required=True)
    mail = forms.EmailField(label='E-mail',max_length=100,required=True,error_messages={'required': 'Por favor completa el campo'},widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'ejemplo@email.com'}))
    mensaje =  forms.CharField(widget=forms.Textarea)

    def clean_edad(self): # Eje implementacion basica 
        if self.cleaned_data["edad"] < 5 and self.cleaned_data["edad"] <80:
            raise ValidationError("El usuario no puede tener menos de 5 años")
        
        return self.cleaned_data["edad"]
    
    def custom_validate_email(mail):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, mail):
          raise ValidationError('Correo electrónico no válido')

