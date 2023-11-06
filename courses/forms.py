# forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from courses.models import Estudiante, Course, Docente


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

    habilitado_choices = (
            (True, 'Habilitado'),
            (False, 'Deshabilitado')
        )
    # username = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    first_name = forms.CharField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    activo = forms.ChoiceField(label="Estado",  choices=habilitado_choices )

    class Meta:
        model = Estudiante
        fields = ["matricula", "first_name",'last_name','activo']
        widgets = {
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'activo': forms.TextInput(attrs={'class':'form-control'})
        }

    # username = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # first_name = forms.IntegerField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # activo = forms.BooleanField(label="activo")

    #     habilitado_choices = (
    #     (True, 'Habilitado'),
    #     (False, 'Deshabilitado')
    # )

    # username = forms.CharField(label="Usuario",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # first_name = forms.IntegerField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # # activo = forms.ChoiceField(label="Estado",  choices=habilitado_choices )


    # class Meta:
    #     model = Estudiante
    #     fields = ["matricula", "first_name",'last_name' ],
    #     widgets = {
    #         'matricula': forms.TextInput(attrs={'class':'form-control'}),
    #         'first_name': forms.TextInput(attrs={'class':'form-control'}),
    #         'last_name': forms.TextInput(attrs={'class':'form-control'}),
    #         # 'activo' : forms.TextInput(attrs={'class':'form-control'})
    #     }


################################################# Docente ################################################################### 
class DocenteAltaForm(forms.ModelForm):
    legajo =  forms.IntegerField(label="Legajo",   widget=forms.NumberInput(attrs={'class': 'formulario','placeholder': 'Solo numeros'}  ),required=True)
    first_name = forms.CharField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    pais = forms.CharField(label="Pais",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    ciudad = forms.CharField(label="Ciudad",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    calle = forms.CharField(label="Calle",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    altura = forms.IntegerField(label="Altura",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True, max_value=100000)

    class Meta:
        model=Docente
        fields=['legajo','last_name','first_name', 'email']
        widgets = {
            'legajo': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_legajo(self):
        if Docente.objects.filter(legajo=self.cleaned_data['legajo']).exists():
            raise ValidationError("El legajo ya existe")
        return self.cleaned_data['legajo']
    
    def clean_email(self):
        if Docente.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError("El mail ya existe")
        return self.cleaned_data['email']

class DocenteForm(forms.ModelForm):
    legajo =  forms.IntegerField(label="Legajo",   widget=forms.NumberInput(attrs={'class': 'formulario disabled', 'readonly': 'readonly'}  ),required=True)
    first_name = forms.CharField(label="Nombre",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    last_name = forms.CharField(label="Apellido",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    email = forms.EmailField(label='Correo Electrónico',  required=True)

    class Meta:
        model=Docente
        fields=['legajo','last_name','first_name', 'email']
        widgets = {
            'legajo': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }

    # def clean_legajo(self):
    #     if Docente.objects.filter(legajo=self.cleaned_data['legajo']).exists():
    #         raise ValidationError("El legajo ya existe")
    #     return self.cleaned_data['legajo']


################################################# Curso ################################################################### 
class CursosForm(forms.ModelForm):
    habilitado_choices = (
        (True, 'Habilitado'),
        (False, 'Deshabilitado')
    )
    titulo = forms.CharField(label="Titulo",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    duracion = forms.CharField(label="Duracion",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    descripcion = forms.CharField(label="Descripcion",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # docente = forms.CharField(label="Docente",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    precio = forms.IntegerField(label="Precio",   widget=forms.NumberInput(attrs={'class': 'formulario'}  ),required=True)
    habilitado = forms.ChoiceField(label="Estado",  choices=habilitado_choices )
    # docente = forms.ChoiceField(label="Docente", choices=[(docente.id, docente ) for docente in Docente.objects.all()], widget=forms.Select, required=True)

    class Meta:
        model=Course
        fields=['titulo','duracion','descripcion','precio','habilitado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'duracion': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            #'docente': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'habilitado': forms.NumberInput(attrs={'class':'form-control'})
        }



    # def clean_docente(self):
    #     if not Docente.objects.filter(id=self.cleaned_data['docente']).exists():
    #         raise ValidationError("El docente no existe")
    #     return self.cleaned_data['docente']
    
    # def clean_email(self):
    #     if User.objects.filter(username=self.cleaned_data['email']).exists():
    #         raise ValidationError("El usuario ya existe")
    #     return self.cleaned_data['email']


class CursoFiltroForm(forms.Form):
    curso = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Selecciona un curso",
    )