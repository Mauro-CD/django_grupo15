from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Course, UserCourse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm  # Importa il AuthenticationForm
import json
from django.shortcuts import render
from .forms import CourseFilterForm, ContactoForm, DireccionForm
from datetime import datetime
from django.contrib.auth.models import User #agregado 22 octubre
from django.contrib import messages #AGREGADO 22 OCTUBRE
from .forms import UserRegistrationForm#agregado 22 octubre
from .models import ContactMessage, Direccion, Estudiante, Direccion, Docente
from .forms import ContactoForm, EstudianteForm, CursosForm, DocenteForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def index(request):
    current_date = datetime.now()
    text_date = 'Fecha actual:'
    text_hour = 'Hora:'
    return render(request, 'index.html', {'date': current_date, 'text_date': text_date, 'text_hour': text_hour})

def contacto_form(request):
    print(request.POST)    
    if request.method == 'POST':
       formulario = ContactoForm(request.POST)
       if formulario.is_valid():
           return redirect('')
    else:
        formulario = ContactoForm()        
    contexto = {
        'contacto_form': formulario
    }
    return render(request, "contacto.html", contexto)


@login_required
def abm_user(request):
  abm_user = User.objects.all()
  return render(request, 'abm_user.html', {'abm_user': abm_user})

def signup(request):
    # Gestiona la logica de registraciòn
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#inicio 22 octubre
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password == password2:
                # Controla si el usuario ya existe
                if User.objects.filter(username=email).exists():
                    messages.error(request, 'Este usuario ya existe.')
                    messages.info(request, 'Este usuario ya existe INFO.')
                    # return redirect('login')
                else:
                    # Crea el usuario
                    user = Estudiante.objects.create_user(username=email, email=email, password=password, matricula=0, activo=True)
                    user.first_name = name
                    user.last_name = lastname
                    user.matricula = user.id + 5000
                    user.save()
                    direccion = Direccion(usuario_id=user.id)
                    direccion.save()

    #             Direccion(models.Model):
    # calle = models.CharField(max_length=100)
    # altura = models.IntegerField()
    # ciudad = models.CharField(max_length=100)
    # pais = models.CharField(max_length=100)
    # usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


                    messages.success(request, 'Usuario registrado exitosamente.')
                    return redirect('login')  # Redirecciona a otra pàagina una vez que se registra
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})
#----------fin22 octubre
#inicio 23 octubre contacto form
def contact(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']
            contact_message = ContactMessage(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
            contact_message.save()
            return redirect('contact')  # Replace 'success_page' with the name of the success page
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'contacto_form': form})
#fin 23 octubre

def user_login(request):
    # Gestiona la logica de login
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirecciona si el login fue bueno
            return redirect('courseAvailable')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# @login_required
def course_list(request):
    # Devuelve lista cursos
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# # @login_required
# def course_edit(request):
#     # Devuelve lista cursos
#     courses = Course.objects.all()
#     return render(request, 'edit-course-listv2.html', {'courses': courses})

# @login_required
def course_detail(request, course_id):
    # Devuelve detalles del curso
    course = Course.objects.get(pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

def course_foro(request):
    #  Devuelve detalles del curso
    foro = Course.objects.all()
    return render(request, 'foro.html', {'foro': foro})

def course_register(request):
    #  Devuelve detalles del curso
    register = Course.objects.all()
    return render(request, 'registro.html', {'register': register})

def course_contact(request):
    #  Devuelve detalles del curso
    contact = Course.objects.all()
    return render(request, 'contacto.html', {'contact': contact})

@login_required
def course_available(request):
    #  Devuelve detalles del curso
    courseAvailable = Course.objects.all()
    return render(request, 'cursos.html', {'courseAvailable': courseAvailable})


class estudianteListView(ListView):
    model = Estudiante
    template_name = 'abm_user.html'
    ordering = ['matricula']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Usuarios"
        # context['url_alta'] = reverse_lazy('estudiante_alta')
        return context

class estudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'abm_user_delete.html'
    success_url = reverse_lazy('abm_user')


class estudianteUpdate(UpdateView):
    model = Estudiante
    # fields = ["id"]
    form_class = EstudianteForm
    template_name = 'abm_user_update.html'
    success_url = reverse_lazy('abm_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Baja Usuario"
        return context

class docenteListView(ListView):
    model = Docente
    template_name = 'abm_docente.html'
    ordering = ['legajo']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Docentes"
        # context['url_alta'] = reverse_lazy('estudiante_alta')
        return context

class docenteDelete(DeleteView):
    model = Docente
    template_name = 'abm_docente_delete.html'
    success_url = reverse_lazy('abm_docente')


class docenteUpdate(UpdateView):
    model = Docente
    # fields = ["id"]
    form_class = DocenteForm
    template_name = 'abm_docente_update.html'
    success_url = reverse_lazy('abm_docente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Baja Docente"
        return context

class docenteCreateView(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'abm_docente_update.html'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Curso"
        return context

    def form_valid(self, form):
        # Agregar lógica de validación adicional aquí
        # Por ejemplo, puedes verificar si el formulario cumple con ciertas condiciones
        if form.is_valid():
            
                    # user = Estudiante.objects.create_user(username=email, email=email, password=password, matricula=0, activo=True)
                    # user.first_name = name
                    # user.last_name = lastname
                    # user.matricula = user.id + 5000
                    # user.save()
            


            # duracion = form.cleaned_data['duracion']
            # descripcion = form.cleaned_data['descripcion']
            # precio = form.cleaned_data['precio']
            # titulo = form.cleaned_data['titulo']
            # docente = Docente.objects.get(id=form.cleaned_data['docente'])
            # habilitado = form.cleaned_data['habilitado']
            # curso = Course(duracion=duracion, descripcion=descripcion, precio=precio, titulo=titulo, docente_id=docente.id,habilitado=habilitado)
            # curso.save()


            legajo = form.cleaned_data['legajo'] 
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            docente = Docente.objects.create_user(legajo=legajo, first_name=nombre, last_name=apellido, email=email, username=email)
            docente.save()                                   
            direccion = Direccion(usuario_id=docente.id)
            direccion.save()
        return redirect('abm_docente')


class course_edit(ListView):
    model = Course
    template_name = 'edit-course-listv2.html'
    ordering = ['titulo']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Usuarios"
        # context['url_alta'] = reverse_lazy('estudiante_alta')
        return context


class courseCreateView(CreateView):
    model = Course
    form_class = CursosForm
    template_name = 'edit-course-newv2.html'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Curso"
        return context

    def form_valid(self, form):
        # Agregar lógica de validación adicional aquí
        # Por ejemplo, puedes verificar si el formulario cumple con ciertas condiciones
        if form.is_valid():
            duracion = form.cleaned_data['duracion']
            descripcion = form.cleaned_data['descripcion']
            precio = form.cleaned_data['precio']
            titulo = form.cleaned_data['titulo']
            docente = Docente.objects.get(id=form.cleaned_data['docente'])
            habilitado = form.cleaned_data['habilitado']
            curso = Course(duracion=duracion, descripcion=descripcion, precio=precio, titulo=titulo, docente_id=docente.id,habilitado=habilitado)
            curso.save()
        return redirect('course_edit')

class cursoDelete(DeleteView):
    model = Course
    template_name = 'edit-course-deletev2.html'
    success_url = reverse_lazy('course_edit')


class cursoUpdate(UpdateView):
    model = Course
    # fields = ["id"]
    form_class = CursosForm
    template_name = 'edit-course-updatev2.html'
    success_url = reverse_lazy('course_edit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Curso"
        return context