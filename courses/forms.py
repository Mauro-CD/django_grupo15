# forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from courses.models import Estudiante, Course, Docente, Inscripcion
from datetime import date
from django.db import connection


def table_exists(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT to_regclass('{table_name}')")
        return cursor.fetchone()[0] is not None

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

def obtener_estudiantes():
    lista_estudiante=[None,None]
    if table_exists('courses_estudiante'):
        estudiantes = Estudiante.objects.all()
        lista_estudiante = [(estudiante.id, estudiante) for estudiante in estudiantes]
    return lista_estudiante


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

def obtener_docentes():
    lista_docentes=[None,None]
    if table_exists('courses_docente'):
        docentes = Docente.objects.all()
        lista_docentes = [(docente.id, docente) for docente in docentes]
    return lista_docentes

################################################# Curso ################################################################### 
class CursosForm(forms.ModelForm):
    habilitado_choices = (
        (True, 'Habilitado'),
        (False, 'Deshabilitado')
    )

    titulo = forms.CharField(label="Titulo",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    duracion = forms.CharField(label="Duracion",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    descripcion = forms.CharField(label="Descripcion",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    imagen=forms.CharField(label="Imagen",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo string url'}  ),required=True)#13nov agregado
    # docente = forms.CharField(label="Docente",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    precio = forms.IntegerField(label="Precio",   widget=forms.NumberInput(attrs={'class': 'formulario'}  ),required=True)
    habilitado = forms.ChoiceField(label="Estado",  choices=habilitado_choices )
    # docente = forms.ChoiceField(label="Docente", choices=[(docente.id, docente ) for docente in Docente.objects.all()], widget=forms.Select, required=True)
    docente = forms.ChoiceField(label="Docente", choices=obtener_docentes(), widget=forms.Select, required=True)

    class Meta:
        model=Course
        fields=['titulo','duracion','descripcion','precio','habilitado','docente']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'duracion': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'imagen': forms.TextInput(attrs={'class':'form-control'}),
            'docente': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'habilitado': forms.NumberInput(attrs={'class':'form-control'})
        }

    def clean_docente(self):
        if Docente.objects.filter(id=self.cleaned_data['docente']).exists():
            self.cleaned_data['docente']=Docente.objects.filter(id=self.cleaned_data['docente'])[0]
        else:
            raise ValidationError("El docente no existe")
        return self.cleaned_data['docente']

    def __init__(self, *args, **kwargs):
        super(CursosForm, self).__init__(*args, **kwargs)
        self.fields['docente'].choices = obtener_docentes()

    # def clean_docente(self):
    #     if not Docente.objects.filter(id=self.cleaned_data['docente']).exists():
    #         raise ValidationError("El docente no existe")
    #     return self.cleaned_data['docente']
    
    # def clean_email(self):
    #     if User.objects.filter(username=self.cleaned_data['email']).exists():
    #         raise ValidationError("El usuario ya existe")
    #     return self.cleaned_data['email']

def obtener_cursos():
    lista_cursos=[None,None]
    if table_exists('courses_course'):
        cursos = Course.objects.all()
        lista_cursos = [(curso.id, curso) for curso in cursos]
    return lista_cursos

class CursoFiltroForm(forms.Form):
    curso = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Selecciona un curso",
    )


################################################# Inscripcion ################################################################### 

class InscripcionForm(forms.ModelForm):
    # habilitado_choices = (
    #     (True, 'Habilitado'),
    #     (False, 'Deshabilitado')
    # )

    fecha = forms.DateField (label="Fecha", initial=date.today(), widget=forms.DateInput(attrs={'class': 'formulario disabled', 'readonly': 'readonly'}   ))
    # estudiante = forms.CharField(label="Estudiante",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # curso = forms.CharField(label="Curso",   widget=forms.TextInput(attrs={'class': 'formulario','placeholder': 'Solo letras'}  ),required=True)
    # estudiantes = forms.CharField(label="Estudiantes",   choices=[(cursos.id, cursos ) for cursos in Course.objects.all()], widget=forms.Select, required=True)
    # estudiante = forms.ChoiceField(label="Estudiantes", choices=[(estudiante.id, estudiante ) for estudiante in Estudiante.objects.all()], widget=forms.Select, required=True)
    # curso = forms.ChoiceField(label="Curso", choices=[(curso.id, curso ) for curso in Course.objects.all()], widget=forms.Select, required=True)
    estudiante = forms.ChoiceField(label="Estudiantes", choices=obtener_estudiantes(), widget=forms.Select, required=True)
    curso = forms.ChoiceField(label="Curso", choices=obtener_cursos(), widget=forms.Select, required=True)

    

    class Meta:
        model=Inscripcion
        fields=['fecha','curso','estudiante']
        widgets = {
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
            'curso': forms.TextInput(attrs={'class':'form-control'}),
            'estudiante': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_estudiante(self):
        if Estudiante.objects.filter(id=self.cleaned_data['estudiante']).exists():
            self.cleaned_data['estudiante']=Estudiante.objects.filter(id=self.cleaned_data['estudiante'])[0]
        else:
            raise ValidationError("El estudiante no existe")
        return self.cleaned_data['estudiante']
    
    def clean_curso(self):
        if Course.objects.filter(id=self.cleaned_data['curso']).exists():
            self.cleaned_data['curso']=Course.objects.filter(id=self.cleaned_data['curso'])[0]
        else:
            raise ValidationError("El curso no existe")
        return self.cleaned_data['curso']

    def clean(self):
        if Inscripcion.objects.filter(estudiante_id=self.cleaned_data['estudiante'].id,curso_id=self.cleaned_data['curso'].id).exists():
            print("El estudiante ya se encuentra inscripto")
            raise ValidationError("El estudiante ya se encuentra inscripto")
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(InscripcionForm, self).__init__(*args, **kwargs)
        self.fields['estudiante'].choices = obtener_estudiantes()
        self.fields['curso'].choices = obtener_cursos()