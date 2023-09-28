from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Course, UserCourse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm  # Import the AuthenticationForm
import json
from django.shortcuts import render
from .forms import CourseFilterForm

def index(request):
    return render(request, 'index.html')



def signup(request):
    # Handle user registration logic here
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    # Handle user login logic here
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page, e.g., course list
            return redirect('courseAvailable')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# @login_required
def course_list(request):
    # Retrieve a list of courses
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# @login_required
def course_detail(request, course_id):
    # Retrieve course details
    course = Course.objects.get(pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

def course_foro(request):
    # Retrieve course details
    foro = Course.objects.all()
    return render(request, 'foro.html', {'foro': foro})

def course_register(request):
    # Retrieve course details
    register = Course.objects.all()
    return render(request, 'registro.html', {'register': register})

def course_contact(request):
    # Retrieve course details
    contact = Course.objects.all()
    return render(request, 'contacto.html', {'contact': contact})

@login_required
def course_available(request):
    # Retrieve course details
    courseAvailable = Course.objects.all()
    return render(request, 'cursos.html', {'courseAvailable': courseAvailable})

