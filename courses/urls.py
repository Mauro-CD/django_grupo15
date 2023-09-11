# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('foro/', views.course_foro, name='foro'),
    path('register/', views.course_register, name='register'),
    path('contact/', views.course_contact, name='contact'),
    path('', views.index, name='index'),
]
